#!/usr/bin/python

import sys
import re
import os




if (len(sys.argv) > 1):
	print(sys.argv[1])
	
file0 = open(sys.argv[1], 'r')
Lines0 = file0.readlines()

finalData = []

if (sys.argv[1].startswith("codes/")):
	filePostfix = sys.argv[1][6:]


count = 0;

for line0 in Lines0:

	
	# hlavní sázky
	print("https://www.livesport.cz/zapas/" + line0.strip() + "/#prehled-zapasu/prehled-zapasu")
	try:
		os.system("google-chrome --headless --dump-dom https://www.livesport.cz/zapas/" + line0.strip() + "/#/prehled-zapasu/prehled-zapasu > .tmp/file.html")
	except:
		print("########## error")

	file1 = open('.tmp/file.html', 'r')
	Lines = file1.readlines()
	 
	b = []
	 
	for line in Lines:
	    b.append(re.findall('(?<=oddsValueInner">).*?(?=<)',line))
	    b.append(re.findall('(?<="fixedScore"><span>).*?(?=<)',line))
	    c = re.findall('(?<="fixedScore__divider">-</span><span>).*?(?=<)',line);
	    if (len(c) > 0):
	    	b.append([c[0]])
	    b.append(re.findall('(?<="duelParticipant__startTime"><div class="">).*?(?=<)',line))
	    b.append(re.findall('(?<=" class="participant__participantName participant__overflow">).*?(?=</a>)',line))
	    

	prefinalData = []
	for i in range (0, len(b)):
		if (len(b[i]) != 0):
			print(b[i])
			prefinalData = prefinalData + b[i]
			prefinalData = prefinalData + ([line0.strip()])
	
	

	
	# sázky asijský hendikep
	print("google-chrome --headless --dump-dom https://www.livesport.cz/zapas/" + line0.strip() + "/#/srovnani-kurzu/asijsky-handicap/zakladni-doba")
	try:
		os.system("google-chrome --headless --dump-dom https://www.livesport.cz/zapas/" + line0.strip() + "/#/srovnani-kurzu/asijsky-handicap/zakladni-doba > .tmp/file.html")
	except:
		print("########## error")

	file1 = open('.tmp/file.html', 'r')
	Lines = file1.readlines()
	 
	b = []
	
	for line in Lines:
	    #b.append(re.findall('(?<=<span class="oddsCell__noOddsCell">).*?(?=<)',line))
	    subresult = re.findall('(?<=<span class="oddsCell__noOddsCell">).*?(?=<)',line)
	    if (len(subresult) > 2):
	    	b.append([subresult[0], subresult[-1]])
	 
	for line in Lines:
	    myLine = line.replace("oddsCell__lineThrough", "")
	    #line.replace("oddsCell__lineThrough", "")
	    b.append(re.findall('(?<=<span class="">).*?(?=<)',myLine))
	    #b.append(re.findall('(?<=<span class="oddsCell__noOddsCell">).*?(?=<)',myLine))
	    
	
	    

	for i in range (0, len(b)):
		if (len(b[i]) != 0):
			print(b[i])
			prefinalData = prefinalData + b[i]
	finalData.append(prefinalData)
	
	"""
		# hendikepy
	print("https://www.livesport.cz/zapas/" + line0.strip() + "/#/srovnani-kurzu/asijsky-handicap/zakladni-doba")
	os.system("google-chrome --headless --dump-dom https://www.livesport.cz/zapas/" + line0.strip() + "/#/srovnani-kurzu/asijsky-handicap/zakladni-doba > .tmp/file.html")

	file1 = open('.tmp/file.html', 'r')
	Lines = file1.readlines()
	 
	b = []
	 
	for line in Lines:
	    b.append(re.findall('(?<=<span class="">).*?(?=<)',line))
	    


	for i in range (0, len(b)):
		if (len(b[i]) != 0):
			print(b[i])
			prefinalData = prefinalData + b[i]
			
	print("count" + str(count))
	count += 1
	"""
			
f = open("results/resultSazky_" + filePostfix, "w+")
for i in range (0, len(finalData)):
	print(finalData[i])
	if (len(finalData[i]) > 15):
		f.write(finalData[i][6] + ";")
		f.write(finalData[i][13] + ";")
		f.write(finalData[i][14] + ";")
		f.write(finalData[i][11] + ";")
		f.write(finalData[i][7] + ";")
		f.write(finalData[i][9] + ";")
		f.write(finalData[i][0] + ";")
		f.write(finalData[i][1] + ";")
		f.write(finalData[i][2] + ";")
		f.write(finalData[i][3] + ";")
		f.write(finalData[i][4] + ";")
		f.write(finalData[i][5] + ";")
		for j in range (15, len(finalData[i])):
		    f.write(finalData[i][j] + ";")
		f.write("\n")
	
f.close()
