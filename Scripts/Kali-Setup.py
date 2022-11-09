#!/usr/bin/python3

import os

print("Kali Setup for ARM64");

print("----- Install Burpsuite");
os.system("sudo apt install burpsuite")


print("----- Install Microsoft Visual Studio Code");
os.system("wget https://az764295.vo.msecnd.net/stable/c3511e6c69bb39013c4a4b7b9566ec1ca73fc4d5/code_1.67.2-1652811872_arm64.deb -O vscode-arm64.deb && sudo apt install ./vscode-arm64.deb")


print("----- Install Gnome: (Please select later 'gdm3' in Wizzard)");
os.system("sudo apt update && sudo apt upgrade")
os.system("sudo apt install kali-desktop-gnome")
os.system("sudo tasksel")


print("----- Install zaproxy");
os.system("sudo apt install -y zaproxy")

