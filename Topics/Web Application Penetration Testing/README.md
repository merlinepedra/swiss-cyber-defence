# Web Application Penetration Testing

## ⭐️ Useful Tools

* [sqlmap](../../Tools/sqlmap/README.md) - Detecting and exploiting SQL injection flaws and taking over of database servers
* [nikto - web vulns scanner](../../Tools/nikto/README.md)
* [nmap](../../Tools/nmap/README.md)
* [Gobuser](../../Tools/gobuster/README.md) - Directory enumeration

---

## Remote Code Execution

##### Cheat Sheet's

- [Command Injection Cheatsheet - HackersOnlineClub](https://hackersonlineclub.com/command-injection-cheatsheet/)

##### Payloads

**Use ping and attach '<mark>ls</mark>' dictionary listing**

```
http://10.10.217.166:8081/ping?ip=10.10.217.166`ls`
```

**Escape Docker Container**

```
docker run -v /:/mnt --rm -it bash chroot /mnt sh 
```

---

## Access control vulnerabilities

---

## Cross-origin resource sharing (CORS)

---

## Cross-site scripting

##### Payload

* [XSS Vectors Cheat Sheet](https://gist.github.com/kurobeats/9a613c9ab68914312cbb415134795b45)

---

## Cross-site request forgery (CSRF)

---

## Insecure deserialization

---

## DOM-based vulnerabilities

---

## Directory traversal

---

## File upload vulnerabilities

---

## HTTP Host header attacks

---

## Information disclosure

---

## Business logic vulnerabilities

---

## OAuth authentication

---

## HTTP request smuggling

---

## Server-side template injection

* [SSTI Payloads on GitHub](https://github.com/payloadbox/ssti-payloads)

---

## SQL injection

##### Cheat Sheet's

* [PortSwigger's SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

##### Payload

* [SQL Injection Payload List on GitHub](https://github.com/payloadbox/sql-injection-payload-list)

##### Tools

* ➡️ [sqlmap](../../Tools/sqlmap/README.md)

##### Articles

* [SQL injection UNION attacks @ portswigger.net](https://portswigger.net/web-security/sql-injection/union-attacks)
* [SQL injection UNION attack @ medium.com](https://medium.com/@nyomanpradipta120/sql-injection-union-attack-9c10de1a5635) 

---

## Server-side request forgery (SSRF)

---

## Authentication

---

## Web cache poisoning

---

## XML external entity (XXE) injection

##### Payloads

* [XXE Injection Payload List on GitHub](https://github.com/payloadbox/xxe-injection-payload-list)

* ![](assets/16515949907459.png)
