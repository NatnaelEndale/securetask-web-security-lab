# SecureTask — Network Architecture

## 1. Overview

The lab uses VirtualBox to create an isolated
environment for application development,
hosting, and security testing.

## 2. Virtual Machines

### Host Machine
Operating System: Ubuntu Desktop

Responsibilities:
- Application development.
- Git and GitHub management.
- Documentation.
- VM administration.
- Browser-based testing.

### VM 1 — SecureTask Server
Operating System: Ubuntu Server

Responsibilities:
- Nginx web server.
- FastAPI application.
- PostgreSQL database.
- SSH administration.
- Firewall configuration.

### VM 2 — Security Testing Machine
Operating System: Kali Linux

Responsibilities:
- Network reconnaissance.
- HTTP traffic inspection.
- Vulnerability assessment.
- Security testing.

## 3. Network Configuration

The lab will use two VirtualBox network types.

### NAT Adapter

Purpose:
- Internet access for package installation.
- Downloading updates and dependencies.

### Host-only Adapter

Purpose:
- Communication between the host and VMs.
- Communication between Ubuntu Server and Kali.
- Isolated security testing.

## 4. Network Communication

Expected communication:

Host -> Ubuntu Server:
HTTP and SSH

Kali -> Ubuntu Server:
HTTP and authorized security testing

Ubuntu Server -> Internet:
Package downloads and updates through NAT

## 5. Expected Ports

| Port | Service | Purpose |
|---|---|---|
| 22 | SSH | Remote administration |
| 80 | HTTP | Web access |
| 443 | HTTPS | Encrypted web access |
| 8000 | FastAPI | Backend application |
| 5432 | PostgreSQL | Database |

Ports 8000 and 5432 should not be exposed
to the host-only network unnecessarily.

FastAPI will initially bind to localhost,
and PostgreSQL will remain accessible only
to the local server application.

## 6. Security Considerations

- Do not expose vulnerable services publicly.
- Restrict SSH access.
- Apply firewall rules.
- Keep database access private.
- Separate development and hosting environments.
- Use isolated networking for security testing.
