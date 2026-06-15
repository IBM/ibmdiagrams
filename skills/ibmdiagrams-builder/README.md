# IBM Diagrams Builder Skill

A portable AI skill that turns any AI agent into an expert IBM architecture diagram engineer.
It uses the **ibmdiagrams MCP server** to generate IBM Design Language-compliant architecture
diagrams from Terraform state files, JSON input, or Python diagram-as-code.

```text
      +-------------------+        +--------------------------+        +------------------------+
      |   AI Agent/User   | -----> | skill: ibmdiagrams-builder | -----> | MCP: ibmdiagrams       |
      +-------------------+        +--------------------------+        +------------------------+
                                              |                              |
                                              v                              v
                                    +------------------+           +----------------------+
                                    | protocols/rules  |           | generate_from_file   |
                                    | + guardrails     |           | server_info          |
                                    +------------------+           +----------------------+
```

---

## Distribution

The skill is distributed as a single directory:

```
ibmdiagrams-builder/
├── SKILL.md
├── README.md
└── references/
    └── (future reference files)
```

**To install:** copy or move the `ibmdiagrams-builder/` directory to the appropriate path
for your client (see [Installation](#installation) below).

When a new version is released, replace the `ibmdiagrams-builder/` directory in all
locations where you installed it. Start a new agent session to pick up the changes.

---

## Contents

```
ibmdiagrams-builder/
├── SKILL.md     ← Skill entry point (shared across all clients)
├── README.md    ← This file
└── references/  ← Future reference files for detailed protocols
```

---

## Prerequisites

Before using this skill, configure the **ibmdiagrams MCP server** in your agent. The skill
relies on two tools the server exposes:

| Tool                | Purpose                                                                   |
| ------------------- | ------------------------------------------------------------------------- |
| `generate_from_file` | Generate diagrams from `.tfstate` or `.json` files                        |
| `server_info`        | Get metadata about the MCP server capabilities                            |

### MCP Server Configuration

Add to your MCP configuration file (e.g., `.bob/mcp.json` for IBM Bob):

```json
{
  "mcpServers": {
    "ibmdiagrams": {
      "command": "ibmdiagrams",
      "args": ["--mcp"]
    }
  }
}
```

Or using `uv` for development:

```json
{
  "mcpServers": {
    "ibmdiagrams-dev": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/path/to/ibmdiagrams",
        "ibmdiagrams",
        "--mcp"
      ]
    }
  }
}
```

See the [ibmdiagrams MCP documentation](../../docs/mcp.md) for detailed setup instructions.

---

## Single SKILL.md — Cross-client compatibility

This skill uses a single `SKILL.md` file across all clients. Different clients parse the
YAML frontmatter differently:

| Frontmatter field           | Claude Code             | IBM Bob                                   | Other clients        |
| --------------------------- | ----------------------- | ----------------------------------------- | -------------------- |
| `name`                      | ✅ skill identifier     | ✅ skill identifier                       | rendered as raw text |
| `title`                     | ignored (uses `name`)   | ignored (uses `name`)                     | rendered as raw text |
| `description`               | ✅ activation trigger   | ✅ activation trigger                     | rendered as raw text |
| `version`                   | ignored (informational) | ignored (informational)                   | rendered as raw text |
| `allowed-tools`             | ✅ enforced             | not enforced — Bob uses MCP server config | ignored              |
| `license`, `author`, `tags` | ignored                 | ignored                                   | rendered as raw text |

**Bob note:** `allowed-tools` has no effect in Bob. Tool access is governed by which tools
are registered in the MCP server configuration. The skill instructions constrain which
tools the agent calls.

**Other clients:** Clients that do not parse YAML frontmatter render the frontmatter block
as raw text. This is cosmetic only — all actionable instructions live below the delimiter.

**Reference files:** Claude Code and IBM Bob auto-load the `references/` directory on
demand. All other clients require the reference content to be manually inlined.

---

## Installation

### IBM Bob

IBM Bob supports skills natively. Place the skill in `.bob/skills/` at your project root
(project-scoped) or in `~/.bob/skills/` (global).

> **Requires Advanced mode.** By default Bob requests approval before activating a skill.
> Configure Auto-Approve in Bob's settings to suppress the confirmation prompt.

**Project-scoped:**

```bash
mkdir -p /path/to/your-project/.bob/skills
cp -r ibmdiagrams-builder /path/to/your-project/.bob/skills/
```

Commit `.bob/skills/ibmdiagrams-builder/` to your repository so the skill is shared across
the team without each developer needing to install it separately.

**Global:**

```bash
mkdir -p ~/.bob/skills
cp -r ibmdiagrams-builder ~/.bob/skills/
```

Bob reads `name` and `description` from `SKILL.md` to determine when to activate the skill.
The `references/` files are automatically available to Bob once the skill is active.

Verify the skill is visible by running `/list-skills` inside Bob.

---

### Claude Code

Claude Code discovers skills automatically from `.claude/skills/` at your project root.
No additional configuration is needed beyond having ibmdiagrams configured as an MCP server.

**Project-scoped (recommended for teams):**

```bash
mkdir -p /path/to/your-project/.claude/skills
cp -r ibmdiagrams-builder /path/to/your-project/.claude/skills/
```

Commit `.claude/skills/ibmdiagrams-builder/` to your repository so the skill is
version-tracked alongside the project and available to every developer on the team without
a separate install.

**Global (available in all projects on this machine):**

```bash
mkdir -p ~/.claude/skills
cp -r ibmdiagrams-builder ~/.claude/skills/
```

---

## Capabilities

| Capability                    | Description                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| Terraform visualization       | Auto-generate diagrams from `.tfstate` files with custom or general labels             |
| Diagram as Code               | Write Python code using the ibmdiagrams API for programmatic diagram creation          |
| IBM Design Language           | All diagrams follow IBM Design Language Technical Diagrams Guideline                   |
| Multi-format output           | Generate DrawIO files (editable) or Python code (customizable)                         |
| Custom labels                 | Show resource names, IPs, CIDRs (custom) or resource types only (general)              |
| Font support                  | IBM Plex Sans with global variants (Arabic, Devanagari, Hebrew, JP, KR, Thai)         |
| IBM Cloud services            | Full support for VPC, compute, network, storage, security, data, AI, containers        |
| Component library             | 100+ IBM Cloud components across 10+ categories                                        |
| Hierarchical structure        | Context manager pattern for clean, readable diagram code                               |
| Automatic layout              | IBM Design Language-compliant automatic positioning and styling                        |

---

## Activation Triggers

The skill activates when the user asks about:

- Creating architecture diagrams from Terraform state files
- Generating diagrams using Python diagram-as-code
- IBM Cloud infrastructure visualization
- DrawIO diagram generation
- IBM Design Language technical diagrams
- Converting infrastructure to visual diagrams
- Terraform to diagram conversion
- IBM Cloud components: VPC, compute, network, storage, security, data services, AI/Watson, containers

---

## Example Prompts

```
Generate a diagram from my Terraform state file at ./infrastructure.tfstate

Create a clean architecture diagram without IP addresses for a presentation

I want to customize the generated diagram — give me Python code instead

Help me create a diagram for a 3-zone VPC with web and database tiers

Show me how to add a load balancer to my existing diagram code

What IBM Cloud components are available for data services?

Generate a diagram with Japanese fonts for our Tokyo team

Convert my Terraform state to a diagram and save it in the docs folder
```

---

## Reference Files

The `references/` directory is reserved for future detailed protocols. Claude Code and IBM
Bob will load these automatically when available. For all other clients, inline the
relevant content into the client's instruction file.

---

## Updating

When a new version of the skill is released:

1. Replace the `ibmdiagrams-builder/` directory at each installed location
2. For project-scoped git installs: commit the updated directory
3. For adapted clients (Cursor, Copilot, Cline, etc.): re-run the inline steps
4. Start a new agent session — skills are loaded fresh each session

---

## Documentation

For detailed documentation, see:

- **[Setup Guide](../../docs/setup.md)** - Installation and configuration
- **[Diagram as Code Guide](../../docs/diagram-as-code.md)** - Python API reference
- **[Terraform Guide](../../docs/terraform.md)** - Terraform integration
- **[MCP Guide](../../docs/mcp.md)** - MCP server configuration
- **[Testing Guide](../../docs/testing.md)** - Visual regression testing

---

## License

Apache-2.0