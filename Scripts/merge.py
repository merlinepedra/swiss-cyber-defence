#!/usr/bin/python3
from encodings import utf_8
import os
import json
import datetime as datetime
import subprocess
import sys

############## Config ##############

pathAccessLog = "./access.log"  
pathForensicsJson = "./forensics.json"
pathOutputJson = "./output.json"
isDebug = False

####################################

def start():
	accessLog = importFile(pathAccessLog)
	forensicsLines = importFile(pathForensicsJson)
	writeJSON(accessLog, forensicsLines, pathOutputJson)

def importFile(path):
	f = open(path, "r")
	lines =f.readlines()
	return lines

def array_on_duplicate_keys(ordered_pairs):
	"""Convert duplicate keys to arrays."""
	d = {}
	for k, v in ordered_pairs:
		if k in d:
			if type(d[k]) is list:
				d[k].append(v)
			else:
				d[k] = [d[k],v]
		else:
		   d[k] = [v]
	return d

def handleSpecialCases(line):
	line = line.replace('"1..2""', "\'1..2\'\"")
	line = line.replace('"",', '",')
	
	return line

def writeJSON(accessLogLines, forensicsLines, pathOutputJson):	
	# clear existing file
	jsonFile = open(pathOutputJson, "w")
	jsonFile.write("")
	jsonFile.close()
	
	index = 0
	for line in accessLogLines:
		if index < 200 or isDebug == False:
			index += 1
			
			splits = line.split( )
	
			responseCode = splits[9]
			if responseCode == "-": responseCode = "0"
	
			forensicsJson = list(filter(lambda x: str(splits[0]) in x, forensicsLines))
			if len(forensicsJson) > 0:
				forensicsJson = forensicsJson[0]
			else:
				sys.stderr.write("\n\n" + str(splits[0]) + " not found in " + pathForensicsJson)
				forensicsJson = ""
				
			requestHeadersJson = ""
			
			if len(forensicsJson) > 0:
				requestHeadersJson = json.loads(forensicsJson)
				headerLines = requestHeadersJson["headers"].split('\n')
				headerString = ""
				for aLine in headerLines:
					if len(aLine) > 0:
						key = aLine.split(':')[0]
						val = aLine.split(':')[1]
						keyVal = '"' + key + '": "' +  val + '",'
						headerString = headerString + keyVal
	
				headerString = "{" + headerString[:-1] + "}"
	
				try:
					cleanHeaderString = handleSpecialCases(headerString)
					requestHeadersJson = json.loads(cleanHeaderString, object_pairs_hook=array_on_duplicate_keys)
				except Exception:
					sys.stderr.write("\n\Format Issue for:\n"  + headerString)
					requestHeadersJson = ""
					continue
	
			jsonObject = {
				'requestId':splits[0],
				'remoteAddress':splits[1],
				'timestamp': datetime.datetime.strptime(splits[4][1:] + " " + splits[5][:-1], "%d/%m/%Y:%H:%M:%S %z").isoformat(),
				'method':splits[6][1:], 
				'url':splits[7], 
				'version':splits[8][:-1], 
				'responseCode':responseCode,
				'responseSize': splits[10],
				'requestHeaders': requestHeadersJson
			}
			
			jsonFile = open(pathOutputJson, "a")
			jsonFile.write(json.dumps(jsonObject))
			jsonFile.write("\n")
			jsonFile.close()
	
	if  isDebug == True:
		os.system("cat " + pathOutputJson)
	
	print("\n\n ✅  Merging done -> check output.json")


start()