#!/usr/bin/env python3

import os
import argparse

print("""\

 █████   █████          ████             █████     ███  ████   ███   █████              
░░███   ░░███          ░░███            ░░███     ░░░  ░░███  ░░░   ░░███               
 ░███    ░███   ██████  ░███   ██████   ███████   ████  ░███  ████  ███████   █████ ████
 ░███    ░███  ███░░███ ░███  ░░░░░███ ░░░███░   ░░███  ░███ ░░███ ░░░███░   ░░███ ░███ 
 ░░███   ███  ░███ ░███ ░███   ███████   ░███     ░███  ░███  ░███   ░███     ░███ ░███ 
  ░░░█████░   ░███ ░███ ░███  ███░░███   ░███ ███ ░███  ░███  ░███   ░███ ███ ░███ ░███ 
	░░███     ░░██████  █████░░████████  ░░█████  █████ █████ █████  ░░█████  ░░███████ 
	 ░░░       ░░░░░░  ░░░░░  ░░░░░░░░    ░░░░░  ░░░░░ ░░░░░ ░░░░░    ░░░░░    ░░░░░███ 
																			   ███ ░███ 
																			  ░░██████  
																			   ░░░░░░   
						   █████████                                                    
						  ███░░░░░███                                                   
						 ███     ░░░  █████ ████ ████████  █████ ████                   
						░███         ░░███ ░███ ░░███░░███░░███ ░███                    
						░███    █████ ░███ ░███  ░███ ░░░  ░███ ░███                    
						░░███  ░░███  ░███ ░███  ░███      ░███ ░███                    
						 ░░█████████  ░░████████ █████     ░░████████                   
						  ░░░░░░░░░    ░░░░░░░░ ░░░░░       ░░░░░░░░                    
""")


parser = argparse.ArgumentParser(description='Volatility Guru - Automated volatility analysis.')
parser.add_argument('-f', help='File path to memory dump')
args = parser.parse_args()


print("---- Get Operation System ----")
osProfile = os.popen('volatility -f ' + args.f + 'imageinfo').read()
print("Operation System Profile: " + osProfile)


print("---- Process ----")
pslist = os.popen('volatility -f ' + args.f + 'pslist').read()
print("pslist: " + pslist)


	#Process


#	volatility -f [image] --profile = [OS Profile] pslist  
#volatility -f [image] --profile = [OS Profile] psscan  
#volatility -f [image] --profile = [OS Profile] pstree  
#volatility -f [image] --profile = [OS Profile] psxview  
#volatility -f [image] --profile = [OS Profile] psxview --apply-rules



#pcap = input("Path to memory: ");
#print(pcap)

#print("1. Install ")

#command = input("Select Option:");


#if command == "1":
#	os.system('sudo apt update && sudo apt install -y docker.io && sudo systemctl enable docker --now && sudo usermod -aG docker $USER')
#	os.system('docker pull phocean/volatility')
#	os.system('echo \'\nfunction volatility() {\n\tdocker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps:ro,Z -ti phocean/volatility $@\n}\' >> ~/.zshrc')
	




	
	

	
