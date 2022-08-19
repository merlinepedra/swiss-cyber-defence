#!/usr/bin/env python3

import os
import argparse
import subprocess
import command


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
parser.add_argument('-i', '--install', action='store_true', help='Install Volatility 2.6.1 via docker')
parser.add_argument('-f', '--file', help='File name of memory dump in (/home/kali/dumps)')
args = parser.parse_args()


if args.install == True:
	install()


if args.file:
	print("---- Get Operation System ----")

	response = command.run([volScript])
	print(response.output)
	print(response.exit)


	# Define command and options wanted
	command = volScript
	options = "-h"
	# Ask user for file name(s) - now it's safe from shell injection
	#filename = input("Please introduce name(s) of file(s) of interest:\n")
	# Create list with arguments for subprocess.check_output
	args=[]
	args.append(command)
	args.append(options)
	#for i in filename.split():
	#	args.append(i)
	# Run subprocess.check_output and save command output


	# Run subprocess.run and save output object
	output = subprocess.run(args,capture_output=True, shell=True)
	print(output)




	# profileOS = os.popen(volScript + ' -f ' + args.file + 'imageinfo')
	# print("Profile of Operating System: " + profileOS)

	profileOS = "Win7SP1x64"

	print("---- Process ----")
	cmd = volScript + ' -f ~/dumps/' + args.file + " --profile " + profileOS + ' pslist'
	print(cmd)


	#p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	#for line in p.stdout.readlines():
	#	print(line),
	#retval = p.wait()

	os.system(cmd)


	# pslist = os.popen(volScript).read()
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






	
	

	
