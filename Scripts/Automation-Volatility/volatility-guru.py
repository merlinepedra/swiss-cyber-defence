#!/usr/bin/env python3

import os
import argparse
import pprint
from subprocess import Popen, PIPE
import subprocess
import sys

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
	

# volScript = 'sudo docker run --rm --user=$(id -u):$(id -g) -v "$(pwd)":/dumps:ro,Z -ti phocean/volatility '
volScript = "volatility "


parser = argparse.ArgumentParser(description='Volatility Guru - Automated volatility analysis.')
parser.add_argument('-f', '--file', help='File path to memory dump')
parser.add_argument('-i', '--install', action='store_true', help='Install Volatility 2.6.0 via docker')
args = parser.parse_args()


if args.install == True:
	install()


if args.file:
	print("---- Get Operation System ----")

	# profileOS = os.popen(volScript + ' -f ' + args.file + 'imageinfo')
	# print("Profile of Operating System: " + profileOS)

	profileOS = "Win7SP1x64"

	print("---- Process ----")
	cmd = volScript + '" -f ' + args.file + " --profile " + profileOS + ' pslist"'
	print(cmd)
	pslist = os.popen(cmd).read()
	print("pslist: " + pslist)


print("---- Done ----")



#	volatility -f [image] --profile = [OS Profile] pslist  
#volatility -f [image] --profile = [OS Profile] psscan  
#volatility -f [image] --profile = [OS Profile] pstree  
#volatility -f [image] --profile = [OS Profile] psxview  
#volatility -f [image] --profile = [OS Profile] psxview --apply-rules



#pcap = input("Path to memory: ");
#print(pcap)


#command = input("Select Option:");






	
	

	
