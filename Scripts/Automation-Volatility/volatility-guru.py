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


def install():
	os.system('sudo apt update && sudo apt install -y docker.io && sudo systemctl enable docker --now && sudo usermod -aG docker $USER')
	os.system('sudo docker pull phocean/volatility')
	os.system('echo \'\nfunction volatility() {\n\tsudo docker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps:ro,Z -ti phocean/volatility $@\n}\' >> ~/.zshrc')
	



volScript = "python2 ~/scripts/volatility/vol.py"

parser = argparse.ArgumentParser(description='Volatility Guru - Automated volatility analysis.')
parser.add_argument('-f', '--file', help='File path to memory dump')
parser.add_argument('-i', '--install', action='store_true', help='Install Volatility 2.6.0 via docker')
args = parser.parse_args()


if args.install == True:
	install()


if args.file:
	print("---- Get Operation System ----")
	osProfile = os.popen(volScript + ' -f ' + args.f + 'imageinfo').read()
	print("Operation System Profile: " + osProfile)


	print("---- Process ----")
	pslist = os.popen(volScript + ' -f ' + args.f + 'pslist').read()
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






	
	

	
