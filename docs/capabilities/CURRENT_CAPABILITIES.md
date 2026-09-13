# Current Capabilities

_Last reviewed: 2026-09-13_

This file is a sanitized operational snapshot, not a promise that every capability is permanently available. Tool surfaces, product tiers, permissions, and runtimes can change.

## Reasoning and Multimodal Work

DEDAL can currently perform:

- advanced reasoning and planning;
- coding, architecture, debugging, and review;
- document and data analysis;
- image understanding;
- image generation/editing through the available image tool;
- research synthesis with live web access when appropriate;
- creative writing and canon-sensitive worldbuilding.

## Connected Systems Currently Exposed

Current conversation tooling includes access to capabilities around:

- GitHub;
- Gmail;
- Google Drive;
- Figma;
- ChatGPT Files/Library;
- plugin discovery/management;
- web research and structured search;
- scheduled/conditional automations.

Availability and permissions must be checked before consequential use.

## Persistent File Capability

ChatGPT Library can act as a persistent document store. DEDAL can, when authorized and supported:

- search prior Library files;
- read and inspect them;
- create folders;
- upload generated artifacts;
- move, rename, and delete Library items;
- reuse stored documents across chats.

The `/DEDAL` Library folder is used for persistent DEDAL reference artifacts.

## Current Sandbox Snapshot

Observed on 2026-09-13:

- Linux: Debian GNU/Linux 13, x86-64;
- Python 3.13.x;
- Node.js 22.x / npm 10.x;
- Git 2.47.x;
- GCC/G++ 14.x;
- Clang 17;
- OpenJDK 21;
- Ruby 3.3.x;
- PHP 8.4;
- FFmpeg 7.1.x;
- Pandoc 3.1.x;
- LibreOffice 25.2;
- roughly 5.8 GiB RAM and 32 GB sandbox filesystem at time of inspection.

### Not Observed

- Flutter SDK: unavailable;
- Dart SDK: unavailable;
- guaranteed GPU: unavailable.

Sandbox environments are ephemeral and should be rechecked before relying on exact versions.

## Artifact Production

DEDAL can produce downloadable files such as:

- Markdown/text/code;
- DOCX;
- PDF;
- PPTX;
- XLSX/CSV;
- ZIP archives;
- charts and generated images.

## Automation

Current automation capability includes:

- one-time reminders;
- recurring tasks;
- scheduled summaries;
- condition watches.

Event-triggered integration capabilities may also be available for supported connected services, but must be confirmed per tool and account.

## Execution Strategy

Prefer the cheapest reliable execution surface:

1. native reasoning/tools;
2. sandbox execution;
3. connected app/API;
4. GitHub Actions or external runner;
5. Work/cloud computer when browser/computer autonomy justifies its quota cost.

## Important Limitation

DEDAL cannot directly rewrite its own underlying model weights. System-level improvement is achieved through better context, workflows, tools, persistent state, evaluation, and feedback loops.
