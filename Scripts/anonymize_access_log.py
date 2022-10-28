#!/usr/bin/env python3
import re
import os

def process_logs():
  #Make a list of unique IPs
  uniqueip = []

  abspath = os.path.abspath(__file__)
  dname = os.path.dirname(abspath)
  os.chdir(dname)


  with open("access.log", 'r') as access_log:
    for l in access_log:
      firstfield=l.split()
      thisIP = firstfield[0];
      if thisIP not in uniqueip:
        uniqueip.append(thisIP)

  with open("access.log", 'r') as access_log:
    filecontent=access_log.read()
    position=0
    for ip in uniqueip:
      position += 1

      #Replace IP with an anonymized token
      filecontent=filecontent.replace(ip,"ANONIP"+str(position))

    #remove login and session parameters from log
    filecontent = re.sub(r'\blogin.php\S+\b', 'login', filecontent)
    filecontent = re.sub(r'\bsession=\S+\b', 'anonsess', filecontent)

  #Write anonymized/pseudonymized data back to file
  with open("anonymized_access.log", "w") as cleanAccessLog:
    cleanAccessLog.write(filecontent)


if __name__ == '__main__':
  process_logs()
