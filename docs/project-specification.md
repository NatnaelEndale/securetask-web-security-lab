# SecureTask — Project Specification

## 1. Overview

SecureTask is a hands-on web application engineering
and cybersecurity project.

The goal is to build, deploy, assess, and secure a
web application in a controlled virtualized environment.

## 2. Objectives

- Understand Linux server administration.
- Configure and manage a web server.
- Develop a frontend using HTML, CSS, and JavaScript.
- Build backend services using Python and FastAPI.
- Integrate PostgreSQL for persistent data storage.
- Develop and test REST APIs.
- Understand authentication and authorization.
- Identify common web application vulnerabilities.
- Implement security remediations.
- Verify security improvements through retesting.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Server OS | Ubuntu Server |
| Web Server | Nginx |
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Security Testing | Kali Linux |
| Testing Tools | Burp Suite, Nmap, curl |
| Virtualization | VirtualBox |
| Version Control | Git, GitHub |

## 4. Application Features

SecureTask will be a task management application.

Initial features:

- User registration.
- User authentication.
- User logout.
- Task creation.
- Task retrieval.
- Task modification.
- Task deletion.
- Task completion status.
- User-specific task management.

## 5. Project Scope

Included:
- Infrastructure configuration.
- Frontend and backend development.
- Database integration.
- REST API development.
- Web application security assessment.
- Vulnerability remediation.
- Server hardening.

Excluded from the initial version:
- Public production deployment.
- Mobile applications.
- Cloud infrastructure.
- Distributed architecture.

## 6. Security Assessment Scope

The application will be assessed for:

- SQL Injection.
- Cross-Site Scripting (XSS).
- IDOR / Broken Object Level Authorization.
- Broken Authentication.
- Broken Access Control.
- Cross-Site Request Forgery (CSRF).
- Path Traversal.
- Security Misconfiguration.

Testing will be restricted to the project-owned
application and isolated lab infrastructure.

## 7. Completion Criteria

The project is complete when:

1. The application is successfully deployed.
2. Frontend and backend communicate correctly.
3. Database operations work correctly.
4. Security weaknesses are documented.
5. Identified vulnerabilities are remediated.
6. Security tests pass after remediation.
7. Technical documentation is complete.
