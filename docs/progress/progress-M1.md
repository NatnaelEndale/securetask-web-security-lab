## M1 — Infrastructure and Hosting

**Status:** Completed  
**Completion date:** November 6, 2026

### 1. Preparation and Planning 

#### Completed

- [x] Defined project objectives.
- [x] Selected technology stack.
- [x] Designed initial architecture.
- [x] Created GitHub repository.
- [x] Created project directory structure.
- [x] Selected GitHub Markdown documentation.
- [x] Established milestone-based workflow.

#### Completed

- [x] Populate project documentation.
- [x] Verify GitHub synchronization.
- [x] Prepare Ubuntu Server ISO.
- [x] Verify available VM resources.
- [x] Finalize VM network configuration.

#### Notes

Development will take place on the Ubuntu host.
Deployment will take place on Ubuntu Server VM.
Security assessment will use Kali Linux VM.

### 2. Ubuntu Server Installation

**Completed:**
- [x] Downloaded Ubuntu Server 26.04.1 LTS ISO.
- [x] Verified ISO SHA-256 checksum.
- [x] Created Ubuntu Server VM using VirtualBox.
- [x] Allocated 4 GB RAM, 2 CPUs, and 30 GB dynamically allocated storage.
- [x] Installed Ubuntu Server successfully.

### 3. Network Configuration

**Completed:**
- [x] Configured NAT adapter for internet access.
- [x] Created VirtualBox Host-only network (`vboxnet0`).
- [x] Configured Ubuntu Server Host-only interface.
- [x] Configured Kali Host-only interface.
- [x] Assigned static IPv4 addresses.
- [x] Verified communication between the host, Ubuntu Server, and Kali.

**Network configuration:**

| Machine | Interface | IP address |
|---|---|---|
| Ubuntu Host | vboxnet0 | 192.168.56.1 |
| Ubuntu Server | enp0s3 (NAT) | 10.0.x.x |
| Ubuntu Server | enp0s8 (Host-only) | 192.168.56.10 |
| Kali Linux | eth0 (NAT) | 10.0.x.x |
| Kali Linux | eth1 (Host-only) | 192.168.56.20 |

**What I learned:**
- Differences between NAT and Host-only networking.
- Linux network interfaces and IPv4 addressing.
- Static IP configuration using Netplan and NetworkManager.
- VirtualBox networking and DHCP fundamentals.

---

**Status:** Completed  
**Completion date:** November 7, 2026

### 4. SSH Configuration

**Completed:**
- [x] Installed OpenSSH Server.
- [x] Enabled and started SSH service.
- [x] Verified SSH service status.
- [x] Successfully connected to Ubuntu Server from the physical Ubuntu host.

**Verification:**
- SSH port: TCP 22.
- Server IP: 192.168.56.10.
- SSH connection: Successful.

**What I learned:**
- SSH remote administration.
- Secure remote communication.
- SSH service management using systemd.

### 5. Nginx Installation

**Completed:**
- [x] Installed Nginx.
- [x] Enabled and started Nginx.
- [x] Verified Nginx is listening on TCP port 80.
- [x] Tested HTTP response using curl.
- [x] Accessed the Nginx welcome page from Ubuntu host.

**Verification:**
- HTTP response: 200 OK.
- Server IP: 192.168.56.10.
- Port: TCP 80.

**What I learned:**
- Nginx acts as a web server.
- HTTP requests use TCP port 80 by default.
- curl can inspect HTTP responses.
- Nginx serves static files from its document root.

### 6. UFW Firewall Configuration

**Completed:**
- [x] Configured default incoming policy to DENY.
- [x] Configured default outgoing policy to ALLOW.
- [x] Allowed SSH from the Host-only subnet.
- [x] Allowed HTTP from the Host-only subnet.
- [x] Enabled UFW.
- [x] Verified firewall rules and status.

**Firewall rules:**

| Service | Port | Source | Action |
|---|---|---|---|
| SSH | TCP 22 | 192.168.56.0/24 | ALLOW |
| HTTP | TCP 80 | 192.168.56.0/24 | ALLOW |
| Other incoming traffic | All | Other sources | DENY by default |

**What I learned:**
- Firewall policies and traffic filtering.
- Managing firewall rules using UFW.
- Restricting access based on network interfaces and source subnets.
- The importance of allowing SSH before enabling a firewall.

### 7. First HTML Page Deployment

**Completed:**
- [x] Created the first SecureTask HTML webpage.
- [x] Created its CSS stylesheet.
- [x] Transferred files to Ubuntu Server using SCP.
- [x] Deployed website files into `/var/www/html/`.
- [x] Configured file ownership and permissions.
- [x] Verified HTTP response using curl.
- [x] Accessed the custom webpage from Ubuntu host and Kali.

**Deployment details:**

- Frontend files: `frontend/index.html`, `frontend/styles.css`.
- Server document root: `/var/www/html/`.
- Web server: Nginx.
- Server IP: `192.168.56.10`.
- HTTP port: `80`.

**Verification:**
- HTTP response: 200 OK.
- Website accessible from the physical Ubuntu host.
- Website accessible from Kali Linux.

**What I learned:**
- HTML and CSS deployment.
- Nginx document root configuration.
- Secure file transfer using SCP.
- Linux file ownership and permissions.
- How a web server delivers static content to browsers.

### 8. Challenges and Troubleshooting

- Encountered a VirtualBox Host-only network configuration error (`NS_ERROR_NOT_IMPLEMENTED`).
- Investigated VirtualBox kernel modules and manually configured the Host-only interface.
- Ubuntu Server did not initially receive an IPv4 address on its Host-only interface; configured a static IP using Netplan.
- Kali did not initially receive an IPv4 address; configured a persistent NetworkManager connection.
- Corrected unintended UFW DENY rules before enabling the firewall.

### 9. M1 Final Result

**M1 — Infrastructure and Hosting: COMPLETED**

Successfully established an operational Ubuntu Server environment with:

- NAT and Host-only networking.
- Remote SSH administration.
- Nginx web server.
- UFW firewall.
- A deployed SecureTask HTML/CSS webpage.
- Verified connectivity from the host and Kali Linux.

**Next milestone:** M2 — Frontend Development.


