#!/usr/bin/env python3
"""Measure pinned project source with Linguist and hash-checked authorship exclusions.

Requires Python 3, Git and Docker. Reads public clones; never runs project code,
changes project attributes, or writes to a remote repository.
"""
from pathlib import Path
import argparse,concurrent.futures,hashlib,json,os,subprocess
ROOT=Path(__file__).resolve().parents[1]
def run(args,**kwargs):return subprocess.check_output(args,**kwargs)
def sha256(data):return hashlib.sha256(data).hexdigest()
def checked_file(root,path,expected=None):
 p=root/path
 if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('Unsafe source path: '+path)
 data=p.read_bytes()
 if expected is not None and sha256(data)!=expected:raise ValueError('Source/evidence hash mismatch: '+path)
 return data

def measure(repo,policy,palette,cache):
 name=repo['repository'].split('/')[1];source=cache/name
 if not (source/'.git').exists():
  source.mkdir(parents=True,exist_ok=True)
  subprocess.run(['git','init','-q',str(source)],check=True)
  subprocess.run(['git','remote','add','origin','https://github.com/'+repo['repository']+'.git'],cwd=source,check=True)
  subprocess.run(['git','fetch','--depth','1','origin',repo['source_commit']],cwd=source,check=True,stdout=subprocess.DEVNULL)
  subprocess.run(['git','checkout','--detach','-q','FETCH_HEAD'],cwd=source,check=True)
 if run(['git','rev-parse','HEAD'],cwd=source,text=True).strip()!=repo['source_commit']:raise ValueError('Pinned revision mismatch: '+name)
 if run(['git','status','--porcelain'],cwd=source).strip():raise ValueError('Source checkout is not clean: '+name)
 command=['docker','run','--rm','--user',f'{os.getuid()}:{os.getgid()}','--network','none','--read-only','--tmpfs','/tmp','--mount',f'type=bind,source={source.resolve()},target=/repo,readonly','--workdir','/repo',policy['linguist']['image'],'github-linguist','--json','--breakdown']
 baseline=json.loads(run(command));excluded={e['path']:e for e in repo['exclusions']}
 if len(excluded)!=len(repo['exclusions']):raise ValueError('Duplicate exclusion: '+name)
 for item in repo['exclusions']:
  checked_file(source,item['path'],item['sha256'])
  for evidence in item['evidence']:checked_file(source,evidence['path'],evidence['sha256'])
 for item in repo['required_retained']+repo['retained_mixed_origin']:checked_file(source,item['path'],item['sha256'])
 records=[];totals={};before={};seen=set()
 for language,value in baseline.items():
  actual=0
  for path in value['files']:
   if path in seen:raise ValueError('Duplicate classified path: '+path)
   seen.add(path);data=checked_file(source,path);actual+=len(data);rule=excluded.get(path)
   records.append({'path':path,'language':language,'bytes':len(data),'sha256':sha256(data),'counted':rule is None,**({'exclusion_kind':rule['kind'],'reason':rule['reason']} if rule else {})})
   if not rule:totals[language]=totals.get(language,0)+len(data)
  if actual!=value['size']:raise ValueError('Linguist byte reconciliation failed: '+name+'/'+language)
  before[language]=actual
 for item in repo['required_retained']+repo['retained_mixed_origin']:
  if item['path'] not in seen or item['path'] in excluded:raise ValueError('Required maintained source omitted: '+item['path'])
 total=sum(totals.values())
 if total<=0:raise ValueError('No eligible source: '+name)
 languages=[{'name':language,'bytes':size,'percentage':size/total*100,'color':palette['colors'].get(language) or '#8b949e','color_source':'GitHub Linguist' if palette['colors'].get(language) else 'neutral fallback (no Linguist color)'} for language,size in sorted(totals.items(),key=lambda x:(-x[1],x[0]))]
 detail={'repository':repo['repository'],'source_commit':repo['source_commit'],'baseline_total_bytes':sum(before.values()),'authored_total_bytes':total,'baseline_languages':before,'authored_languages':totals,'files':sorted(records,key=lambda x:x['path']),'explicit_exclusions_already_omitted_by_linguist':sorted(set(excluded)-seen)}
 snapshot={'repository':repo['repository'],'source_url':repo['source_url'],'source_commit':repo['source_commit'],'retrieved_at':repo['retrieved_at'],'method':policy['method'],'total_bytes':total,'linguist_baseline_bytes':sum(before.values()),'additional_excluded_bytes':sum(before.values())-total,'counted_files':sum(r['counted'] for r in records),'languages':languages,'exclusions':repo['exclusions'],'retained_mixed_origin':repo['retained_mixed_origin']}
 print(name+': '+', '.join(f"{l['name']} {l['percentage']:.2f}%" for l in languages[:4]),flush=True)
 return snapshot,detail

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--cache-root',type=Path,required=True);parser.add_argument('--output',type=Path,default=ROOT/'assets/language-stats.json');parser.add_argument('--audit-dir',type=Path,default=ROOT/'language-audit');parser.add_argument('--policy',type=Path,default=ROOT/'tools/language-sources.json');parser.add_argument('--jobs',type=int,default=3);args=parser.parse_args()
 policy=json.loads(args.policy.read_text());palette=json.loads((ROOT/'tools/linguist-colors.json').read_text())
 version=run(['docker','run','--rm','--network','none','--read-only','--tmpfs','/tmp',policy['linguist']['image'],'github-linguist','--version'],text=True).strip()
 if version!='github-linguist '+policy['linguist']['version']:raise ValueError('Linguist version mismatch')
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:results=list(pool.map(lambda repo:measure(repo,policy,palette,args.cache_root),policy['repositories']))
 # Write only after every repository and exclusion passes verification.
 snapshot={'basis':'Authored source bytes: pinned Linguist statistics minus verified generated/dependency files; no language weighting.','method':policy['method'],'measurement_tool':policy['linguist'],'policy_sha256':sha256(args.policy.read_bytes()),'color_source':palette['source'],'repositories':[s for s,_ in results]}
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(snapshot,indent=2)+'\n');args.audit_dir.mkdir(parents=True,exist_ok=True)
 for _,detail in results:(args.audit_dir/(detail['repository'].split('/')[1]+'.json')).write_text(json.dumps(detail,indent=2)+'\n')
 if (args.audit_dir/'repository-api-before.json').exists():
  previous={r['repository']:r for r in json.loads((args.audit_dir/'repository-api-before.json').read_text())['repositories']};comparison=[]
  for s,d in results:
   old=previous.get(s['repository']);comparison.append({'repository':s['repository'],'source_commit':s['source_commit'],'previous_display':{'retrieved_at':old['retrieved_at'],'source_commit':None,'total_bytes':old['total_bytes'],'languages':{l['name']:l['bytes'] for l in old['languages']}} if old else None,'same_commit_linguist_total':d['baseline_total_bytes'],'same_commit_linguist_languages':d['baseline_languages'],'authored_total':d['authored_total_bytes'],'authored_languages':d['authored_languages']})
  (args.audit_dir/'comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
if __name__=='__main__':main()
