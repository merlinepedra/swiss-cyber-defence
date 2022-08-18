### Exam Simulation Web Apps

2022-08-18 - 14:15 - 

Go to Lab and start Exam Simulation Web lab

Provide vulnerabilities you found with the format provided below:

- **Vulnerability**: explanation of the vulnerability in maximum 2 sentences

Allows XSS Code Injection

```
skipLink.innerHTML = 'Skip to content';
```

- **Exploit**: description of the steps on how an attacker could exploit the vulnerability

http://10.0.54.178/wp-content/plugins/wp-stats-manager/js/wsm_new.js

- **Detection**: description of a way to detect an attack in maximum 2 sentences

- **Mitigation**: recommendation to mitigate the issue with non-infrastructure measures

P.S wpscan is your friend. It will show you the door but do not trust it a lot :)
