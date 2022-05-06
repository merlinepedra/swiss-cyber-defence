#!/usr/bin/env python3

import os


print("""\


  dP            dP                         dP                
  88            88                         88                
d8888P .d8888b. 88d888b. .d8888b. 88d888b. 88  .dP           
  88   Y8ooooo. 88'  `88 88'  `88 88'  `88 88888"            
  88         88 88    88 88.  .88 88       88  `8b.          
  dP   `88888P' dP    dP `88888P8 dP       dP   `YP          
															 
															 
dP   dP   dP oo                                           dP 
88   88   88                                              88 
88  .8P  .8P dP d888888b d888888b .d8888b. 88d888b. .d888b88 
88  d8'  d8' 88    .d8P'    .d8P' 88'  `88 88'  `88 88'  `88 
88.d8P8.d8P  88  .Y8P     .Y8P    88.  .88 88       88.  .88 
8888' Y88'   dP d888888P d888888P `88888P8 dP       `88888P8 



""")



pcap = input("Path to pcap: ");
print(pcap)

print("1. Show all URL's")
print("2. Show all URL's which contains .exe")
print("3. Show http URLs")

command = input("Select Option:");


if command == "1":
	os.system('tshark -r ' + pcap + '  -Y http.request -T fields -e http.host -e ip.dst -e http.request.full_uri ')



if command == "2": 
	print()
	print("All .exe URL's")
	os.system('tshark -r ' + pcap + '  -Y http.request -T fields -e http.host -e ip.dst -e http.request.full_uri | grep .exe')


if command == "3": 
	print()
	print("Show http URLs")
	os.system('tshark -r ' + pcap + '  -Y "frame contains http:"')




