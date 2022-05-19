#!/usr/bin/python3
from encodings import utf_8
import os
import json
import datetime as datetime
import subprocess

pathAccessLog = "./access.log"
pathForensicsJson = "./forensics.json"

def start():
	accessLog = importFile(pathAccessLog)
	forensicsJson = importFile(pathForensicsJson)
	writeJSON(accessLog, forensicsJson)


def importFile(path):
	f = open(path, "r")
	lines =f.readlines()
	return lines

def writeJSON(accessLogLines, forensicsJsonLines):
	jsonArray = []

	for line in accessLogLines:
		splits = line.split( )
		responseCode = splits[9]
		if responseCode == "-": responseCode = "0"

		command = 'grep -i "' + str(splits[0]) + '" ' + pathForensicsJson
		forensicsJson = (subprocess.check_output(command, shell=True)).decode('utf-8');
		requestHeadersJson = json.loads(forensicsJson)
		requestHeadersJson = requestHeadersJson["headers"].split('\n')
		


		jsonObject = {'requestId':splits[0],
		'remoteAddress':splits[1],
		'timestamp': datetime.datetime.strptime(splits[4][1:] + " " + splits[5][:-1], "%d/%m/%Y:%H:%M:%S %z").isoformat(),
		'method':splits[6][1:], 
		'url':splits[7], 
		'version':splits[8][:-1], 
		'responseCode':responseCode,
		'responseSize': splits[10],
		'requestHeaders': requestHeadersJson}
		jsonArray.append(jsonObject)
   
	jsonString = json.dumps(jsonArray)

	jsonFile = open("./output.json", "w")
	jsonFile.write(json.dumps(json.loads(jsonString), indent=4))
	jsonFile.close()

	jsonFile = open("./output.json", "r")
	print(jsonFile.read())

start()