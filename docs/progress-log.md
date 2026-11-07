# SecureTask — Project Progress Log

## Project Information

Project: SecureTask
Repository: securetask-web-security-lab
Methodology: Milestone-based

---

## Phase 0 — Preparation and Planning

Status: In progress

### Completed

- [x] Defined project objectives.
- [x] Selected technology stack.
- [x] Designed initial architecture.
- [x] Created GitHub repository.
- [x] Created project directory structure.
- [x] Selected GitHub Markdown documentation.
- [x] Established milestone-based workflow.

### Completed

- [x] Populate project documentation.
- [x] Verify GitHub synchronization.
- [x] Prepare Ubuntu Server ISO.
- [x] Verify available VM resources.
- [x] Finalize VM network configuration.

### Notes

Development will take place on the Ubuntu host.
Deployment will take place on Ubuntu Server VM.
Security assessment will use Kali Linux VM.

---

## Future Milestones

- [x] M0 — Planning and preparation.
- [x] M1 — Infrastructure and hosting.
- [ ] M2 — Frontend development.
- [ ] M3 — Backend development.
- [ ] M4 — Database integration.
- [ ] M5 — Security assessment.
- [ ] M6 — Remediation and hardening.

---

#### M1 — Nginx Installation

**Completed:**
- [x] Installed Nginx.
- [x] Enabled and started Nginx.
- [x] Verified Nginx is listening on TCP port 80.
- [x] Tested HTTP response using curl.
- [x] Accessed the welcome page from Ubuntu host.

**Verification:**
- HTTP response: 200 OK
- Server IP: 192.168.56.10
- Port: 80

**What I learned:**
- Nginx acts as a web server.
- HTTP requests use TCP port 80 by default.
- curl can inspect HTTP responses.
