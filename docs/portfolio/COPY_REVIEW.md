# Purpose, typography and gallery review

Review only; not deployed. Based on the approved Rheon source `b899d7c`, currently published at Pages commit `396dc13`.

Equivalent project names and purpose headlines share a white sans-serif treatment. Pantograph, Whip Docs, Rheon and Kenoma show one original image at a time, with manual Previous/Next controls and a count. A 150 ms fade respects reduced motion; there is no autoplay. Original proportions, captions, full-size dialogs and keyboard/history focus are preserved. Lanternwake is a text row beneath the books.

## Exact revised project copy

### Pumas Library

**Manage local models once.**

Rust infrastructure for local AI deployment: find and download models, organize files and metadata, and share configuration across apps without duplicating model files.

Inference plugins support development and testing.

### Pantograph

**Build workflows. Keep the evidence.**

Node-based AI workflows across inference backends, with retained data and execution history you can return to and inspect.

Resource-aware scheduling that looks ahead across the graph is in development.

### Chrema

**Compose agents you can inspect.**

Build agents from reusable components, with a design that makes their inputs, decisions and outputs visible to people and other agents.

The composition layer in a wider design: Pumas manages models, Pantograph runs workflows, and Chrema assembles agents. Cross-project integrations remain in development.

### Tuldok

**Shape data for model training.**

Create and curate model-training datasets, review the data, and follow workflows through to training results.

### Eidetic

**Shape context over time.**

A clip-based knowledge graph for deciding what contributes to context and output. The aim is to move, trim, split and rearrange clips to control which graph information is included over time.

### Whip Docs

**See the code. Guide the work.**

A visual workspace in development for understanding code structure and collaborating with coding agents. The goal is to inspect their designs and proposed changes, then guide the work through the same interface.

Today’s prototype combines a 3D file-and-symbol view with an intent journal.

### Rheon

**Simulate fluids. Train surrogates.**

A general 3D fluid-physics solver in development, intended to generate training data for faster AI surrogate simulation.

### Kenoma

**Study how bodies move.**

Soft- and rigid-body physics research toward anatomically detailed muscle and skeleton simulation, including contracting soft bodies.

The current posing and held-arm prototypes explore parts of that larger goal.

### Coding Standards

**Model knowledge. Study interaction.**

Its graph-memory engine supports domain modeling and agent-interface research: how agents find, use and change structured knowledge.

In the current engine, typed MCP tools expose navigation and retained workflow state. The wider aim is observability that stays transparent to the agent, so people can inspect interactions and improve the interface.

### Lanternwake

**Explore stories with local AI.**

A Godot/C# 3D visual novel exploring guided and adaptive storytelling with local AI.

An authored island mystery provides the story; local-AI conversations are optional. Qualification of the current model deployment and real microphone input is still pending.

### Cooking the Cat

A personal account of Puma’s development approach.

Assembled by an agent analyzing engineering conversations.

## Sources and boundaries

- Project purposes follow the owner’s voice-call descriptions. Existing prototype-limit disclosures and all original images remain unchanged. The Chrema entry links to the owner-specified repository, https://github.com/MrScripty/Chrema. GitHub reports it public and the repository page returned HTTP 200 without authentication on 12 October 2026. Repository visibility was not changed by this review.
- Coding Standards current public main is [`188beda1`](https://github.com/MrScripty/Coding-Standards/tree/188beda1fa477d21d576c233dd8c7f4c4c267d23). Its engine README, MCP server and tool catalog confirm typed navigation, structured results, runtime/contract inspection and retained workflow status. The broader agent-transparent observability is framed as a research aim, not a completed general tracing system.
- Lanternwake current public main is [`76b8428e`](https://github.com/MrScripty/Lanternwake/tree/76b8428ee6bbe0c03d80b7df0520370df1a1b3a7). Its README distinguishes authored story, optional local AI, historical inference tests and pending current-deployment/physical-microphone qualification. No screenshot or shipped-product claim was added.
- The separate local Cooking the Cat draft is preserved exactly. Only the owner-authorized short portfolio description changes; no book manuscript, cover or separate book site is published here.
