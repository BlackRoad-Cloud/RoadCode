<!-- BlackRoad SEO Enhanced -->

# RoadCode

> Part of **[BlackRoad OS](https://blackroad.io)** — Sovereign Computing for Everyone

[![BlackRoad OS](https://img.shields.io/badge/BlackRoad-OS-ff1d6c?style=for-the-badge)](https://blackroad.io)
[![BlackRoad-Cloud](https://img.shields.io/badge/Org-BlackRoad-Cloud-2979ff?style=for-the-badge)](https://github.com/BlackRoad-Cloud)

**RoadCode** is part of the **BlackRoad OS** ecosystem — a sovereign, distributed operating system built on edge computing, local AI, and mesh networking by **BlackRoad OS, Inc.**

### BlackRoad Ecosystem
| Org | Focus |
|---|---|
| [BlackRoad OS](https://github.com/BlackRoad-OS) | Core platform |
| [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc) | Corporate |
| [BlackRoad AI](https://github.com/BlackRoad-AI) | AI/ML |
| [BlackRoad Hardware](https://github.com/BlackRoad-Hardware) | Edge hardware |
| [BlackRoad Security](https://github.com/BlackRoad-Security) | Cybersecurity |
| [BlackRoad Quantum](https://github.com/BlackRoad-Quantum) | Quantum computing |
| [BlackRoad Agents](https://github.com/BlackRoad-Agents) | AI agents |
| [BlackRoad Network](https://github.com/BlackRoad-Network) | Mesh networking |

**Website**: [blackroad.io](https://blackroad.io) | **Chat**: [chat.blackroad.io](https://chat.blackroad.io) | **Search**: [search.blackroad.io](https://search.blackroad.io)

---


> Canonical RoadCode workspace and automation hub for BlackRoad-Cloud.

Part of the [BlackRoad OS](https://blackroad.io) ecosystem — [BlackRoad-Cloud](https://github.com/BlackRoad-Cloud)

---

# BlackRoad-Cloud — RoadCode

> Infrastructure & Edge Computing division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Cloud infrastructure, edge routing, DNS, TLS termination, and sync services. The networking layer that connects 7 nodes into one coherent system. Your device, your data, your agents.

**Domain**: [blackroad.network](https://blackroad.network)

## Products & Services

| Product | What It Does |
|---------|-------------|
| **RoadSync** | File + database sync across the Pi fleet and droplets |
| **Terraform Modules** | Infrastructure-as-code for the entire BlackRoad stack |
| **K8s Operators** | Custom Kubernetes operators for fleet orchestration |
| **Edge Router** | Caddy on Gematria — TLS for 151 domains via Let's Encrypt |

## The Stack

| Layer | Technology | Where |
|-------|-----------|-------|
| **TLS Edge** | Caddy | Gematria (DO nyc3) |
| **DNS** | PowerDNS | Lucidia + Gematria (ns1/ns2) |
| **VPN** | WireGuard | All 7 nodes (12/12 connections) |
| **Object Storage** | MinIO | Cecilia (4 buckets, S3-compatible) |
| **Database** | PostgreSQL | Alice, Cecilia, Octavia |
| **Cache** | Redis | Alice |
| **PaaS** | Deploy API | Octavia :3500 |
| **Workers** | workerd (15) | Octavia :9001-9015 |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Cloud (Infrastructure & Edge)
      ├── RoadCode                    ← this repo (workspace + automation)
      ├── roadsync                     ← fleet sync engine
      ├── blackroad-terraform-modules  ← IaC modules
      ├── k8s-operators                ← custom K8s operators
      └── operator                     ← CLI + infra scripts
```

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — the physical nodes this runs on
- **Security**: [BlackRoad-Security](https://github.com/BlackRoad-Security) — WireGuard audit + TLS verification
- **Total cost**: $38/mo for the entire 7-node fleet

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
