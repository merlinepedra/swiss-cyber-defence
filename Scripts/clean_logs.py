#!/usr/bin/python3

import re
import os

if __name__ == '__main__':
    logfile_name = "access.log"
    logfile_cleaned_name = "accesslog_cleaned.log"
    seen_ips = {}
    seen_users = {}
    seen_sessions = {}
    ip_idx = 0
    users_idx = 0
    session_idx = 0

    loginString = 'login='
    sessionString = 'session='

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open(logfile_cleaned_name, 'w') as logfile_cleaned:
        with open(logfile_name, 'r') as logfile:
            for line in logfile:
                if ('sqlmap' in line):
                    #print(line)
                    pass

                ipEnd = line.find(' ')
                ip = line[:ipEnd:]
                ip_replace = ''
                if ip not in seen_ips:
                    seen_ips[ip] = ip_idx
                    ip_replace = ip_idx
                    ip_idx += 1
                else:
                    ip_replace = seen_ips[ip]

                cleaned_line = ''.join(['ip{0}'.format(ip_replace), line[ipEnd::]])
                loginIdx = cleaned_line.find(loginString)

                if loginIdx != -1:
                    httpIdx = cleaned_line.find(' HTTP/1.1')
                    loginStart = loginIdx+len(loginString)
                    loginEnd = line.find('&')
                    login = cleaned_line[loginStart:loginEnd:]
                    login_replace = ''
                    if login not in seen_users:
                        seen_users[login] = users_idx
                        login_replace = users_idx
                        users_idx += 1
                    else:
                        login_replace = seen_users[login]
                    cleaned_line = ''.join([cleaned_line[:loginIdx+len(loginString):], 'user{0}'.format(login_replace), '&pass=', '<REMOVED>', cleaned_line[httpIdx::]])

                sessionIdx = cleaned_line.find(sessionString)
                if sessionIdx != -1:
                    httpIdx = cleaned_line.find(' HTTP/1.1')
                    sessionEnd = line.find(' ')
                    session = line[:ipEnd:]
                    session_replace = ''
                    if session not in seen_sessions:
                        seen_sessions[session] = session_idx
                        session_replace = session_idx
                        session_idx += 1
                    else:
                        session_replace = seen_sessions[session]

                    cleaned_line = ''.join([cleaned_line[:sessionIdx+len(sessionString):], 'session{0}'.format(session_replace), cleaned_line[httpIdx::]])
                #print(cleaned_line)
                logfile_cleaned.write(cleaned_line)