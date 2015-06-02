#-------------------------------------------------------------------------------
# Sherif Sarhan
# This is a simple program to output the word count of a file.
#-------------------------------------------------------------------------------
def parse_document(filename):
	#Opens file with read param
	file = open(filename+".txt", "r")
	fileString = file.read()
	
	#print("\nfileString before: ",fileString)
	
	#bad symbols
	badsymbol = """`~!@#$%^&*()-_=+\|]}[{;:'",<.>/?"""
	
	#lowercases everything
	fileString = fileString.lower()
	
	#loop to get double nest
	for eachchar in fileString:
		for eachbad in badsymbol:
			if eachchar == eachbad:
				#print(eachchar)
				fileString = fileString.replace(eachchar,'')
	
	#print("\nfileString after: ",fileString)
	
	words = fileString.split()
	
	#print("\nwords split: ",words)
	
	unique_words = list(set(words))							
	
	#print("\nunique words: ",unique_words,"\n")
	
	#loop to get wordcount into dictionary
	wordcount = {}
	for eachword in unique_words:
		wordcount[eachword] = 0
	
	#loop to get length of words
	for i in range(len(words)):
		for key in wordcount.keys():
			current_score = words[i]
			if current_score == key:
				wordcount[key] = wordcount[key] + 1
	
	file.close()
	return (wordcount)
	
def build_report(freq):
	lengthlist = []
	#Gets the length of each key
	for eachkey in sorted(freq.keys()):
		lengthlist.append(len(eachkey))
		#print("key: ", eachkey, "\nlength: ",len(eachkey),"\n")
	#print("lengthlist: ",lengthlist)
	
	####SHORTS####
	lowest = lengthlist[0]
	for eachval in lengthlist:
		if lowest <= eachval:
			lowest = lowest
		else:
			lowest = eachval	
	#print(lowest)
	
	####LONGS####
	highest = lengthlist[0]
	for eachval in lengthlist:
		if highest >= eachval:
			highest = highest
		else:
			highest = eachval
	#print(highest)
	
	lowestlist = []
	highestlist = []
	for eachkey in sorted(freq.keys()):
		if len(eachkey) == lowest:
			lowestlist.append(eachkey)
		if len(eachkey) == highest:
			highestlist.append(eachkey)
	
	report = {"shorts":lowestlist,"longs":highestlist}
	
	####MODE####
	
	occur_list = []
	for eachkey in freq.keys():
		occur_list.append(freq[eachkey])
	#print("occur list: ",occur_list)
	
	#finds the highest occuring
	highest = occur_list[0]
	for eachval in occur_list:
		if highest >= eachval:
			highest = highest
		else:
			highest = eachval
	#print(highest)
	
	modelist = []
	for eachkey in sorted(freq.keys()):
		if freq[eachkey] == highest:
			modelist.append(eachkey)
	
	report["mosts"] = modelist
	
	####COUNT####
	count = 0
	for each_num in occur_list:
		count += each_num
	#print("count: ",count)
	
	report["count"] = count
	
	####AVLEN####
	totcount = 0
	#gets the total count of all lengths, divides by # of words
	for eachkey in freq.keys():
		totcount += len(eachkey) * freq[eachkey]
	totcount = totcount/count	
	avglen = totcount
	
	#print(avglen)
	
	#appending dictionaries
	report["avglen"] = avglen
	
	#### freqs ####
	report["freqs"] = freq
	
	return(report)

def combine_reports(r1,r2):
	#print("\nR1",r1,"\n")
	#print("\nR2",r2,"\n")
	
	r3 = {}
	
	#### SHORTS #####
	shortlist = []
	
	shortlist1 = list(r1["shorts"])
	shortlist2 = list(r2["shorts"])
	
	#Checking the shortest lists
	if len(shortlist1[0]) < len(shortlist2[0]):
		r3["shorts"] = list(set(shortlist1))
	elif len(shortlist1[0]) == len(shortlist2[0]):
		shortlist3 = list(set(shortlist1 + shortlist2))
		r3["shorts"] = list(set(shortlist3))
	elif len(shortlist1[0]) > len(shortlist2[0]):
		r3["shorts"] = list(set(shortlist2))
	#### SHORTS #####			
	
	
	
	
	
	#### LONGS ####
	longlist = []
	
	longlist1 = list(r1["longs"])
	longlist2 = list(r2["longs"])
	
	#checking the longest lists
	if len(longlist1[0]) < len(longlist2[0]):
		r3["longs"] = list(set(longlist2))
	elif len(longlist1[0]) == len(longlist2[0]):
		longlist3 = list(set(longlist1 + longlist2))
		r3["longs"] = list(set(longlist3))
	elif len(longlist1[0]) > len(longlist2[0]):
		r3["longs"] = list(set(longlist1))
	#### LONGS ####
	
	
	
	
	
	#### MOSTS ####
	r1mosts = []
	for eachVal in r1["mosts"]:
		r1mosts.append(eachVal)
	
	r1Val = r1["freqs"][r1mosts[0]]
	
	#print("r1Val",r1Val)
	
	#print("r1mosts: ",r1mosts)
	
	r2mosts = []
	for eachVal in r2["mosts"]:
		r2mosts.append(eachVal)
	
	r2Val = r2["freqs"][r2mosts[0]]
	
	r3mosts = r1mosts + r2mosts
	
	#checking the modes
	if r1Val > r2Val:
		r3["mosts"] = r1mosts
	elif r1Val == r2Val:
		r3["mosts"] = r3mosts
	elif r2Val > r1Val:
		r3["mosts"] = r2mosts		
	#### MOSTS ####
	
	
	
	#### COUNT ####
	countVal1 = r1["count"]
	
	countVal2 = r2["count"]
	
	countVal3 = countVal1 + countVal2
	
	r3["count"] = countVal3
	#### COUNT ####
	
	
	
	#### AVGLEN ####
	avglen1 = r1["avglen"]
		
	avglen2 = r2["avglen"]
	
	totavg = ((avglen1 * countVal1) + (avglen2 * countVal2))/countVal3
	
	r3["avglen"] = totavg
	#### AVGLEN ####
	
	
	
	
	#### FREQS ####
	freq1 = r1["freqs"]
	freq2 = r2["freqs"]
	
	newfreq = {}
	
	bothfreq = {}
	
	#getting the frequencies from freq1 and freq2
	for eachkey1 in freq1.keys():
		for eachkey2 in freq2.keys():
			if eachkey1 == eachkey2:
				bothfreq[eachkey1] = (freq1[eachkey1] + freq2[eachkey2])

				#print(eachkey1,freq1[eachkey1] + freq2[eachkey2])
			elif eachkey1 != eachkey2:
				newfreq[eachkey1] = freq1[eachkey1]
				newfreq[eachkey2] = freq2[eachkey2]
				
				#print("OK",eachkey1)
	
	for eachkey in bothfreq:
		newfreq[eachkey] = bothfreq[eachkey]
		
	r3["freqs"] = newfreq
	#### FREQS ####
	
	return (r3)
	
def write_report(r,filename):
	open_report = open(filename+".txt","w")
	
	#### WRITE SHORTS ####
	open_report.write("shorts: ")
	
	x = 1
	#writes the shorts
	for eachval in r["shorts"]:
		open_report.write(eachval)

		#condition to stop so no extra commas
		if x < len(r["shorts"]):
			open_report.write(", ")
			x += 1
	
	open_report.write("\n")
	#### WRITE SHORTS ####		
	
	#### WRITE LONGS ####
	open_report.writelines("longs: ")
	
	x = 1
	#checks for longs and puts in ideal spacing and commas
	for eachval in r["longs"]:
		open_report.write(eachval)

		if x < len(r["longs"]):
			open_report.write(", ")
			x += 1
	
	open_report.write("\n")
	#### WRITE LONGS ####	
					
	
	#### WRITE MOSTS ####
	open_report.writelines("mosts: ")
	
	x = 1
	for eachval in r["mosts"]:
		open_report.write(eachval)

		if x < len(r["mosts"]):
			open_report.write(", ")
			x += 1
	
	open_report.write("\n")
	#### WRITE MOSTS ####		
			
	#### WRITE COUNT ####
	open_report.writelines("count: ")
	
	open_report.write(str(r["count"]))
	
	open_report.write("\n")
	#### WRITE COUNT ####		
	
	#### WRITE AVGLEN ####
	open_report.writelines("avglen: ")
	
	open_report.write(str(r["avglen"]))
	
	open_report.write("\n\n")
	#### WRITE AVGLEN ####	
	
	
	#### WRITE FREQS ####
	#open_report.writelines("freqs: ")
	
	for eachkey in sorted(r["freqs"]):
		open_report.write(eachkey+" "+str(r["freqs"][eachkey]))
		open_report.write("\n")
	
	#open_report.write("\n")
	#### WRITE FREQS ####	
	
	open_report.close()
	return None
		

def read_report(filename):
	#opening file with read param
	openfile = open(filename+".txt", "r")
	
	filelist = openfile.readlines()
	
	#print(filelist,"\n")
	
	freq = filelist[:]
	
	newdict = {}
	
	del freq[5]
	#print(freq)
	
	#loop to only get the frequencies
	for x in range(5,len(list(freq))):
		listfreq = list(freq[x].split())
		firstkey = listfreq[0]
		firstkey = firstkey.replace(":", "")

		#print(firstkey)
		del listfreq[0]
		
		#gets the frequency values and adds to dictionary
		valueslist = []
		for values in listfreq:
			#valueslist.append(int(values))
			newdict[firstkey] = int(values)
	
	#print("\nnewdict: ",newdict)
	
	#sends frequencies off to be rebuilt into dictionary
	finaldict = build_report(newdict)
	
	#print("\nfinaldict: ",finaldict)
	
	#print(newdict)
	
	
	#print(newreport)
	
	
	return finaldict


def run_menu():
	#loop to keep telling menu to run unless told not to do so
	runMenu = True
	#checks whether to run or not
	while runMenu == True:
		#gets input from user
		print(" 1. read file, build report, save the report\n",\
			  "2. combine two reports\n",\
			  "3. quit\n")
		option_input = int(input("Choose an option:"))
		
		#checks if input is 1 parse, build, write
		if option_input == 1:
			read = input("what file name do you want me to read?\n")
			write = input("what filename do you want to write to?\n")
			
			parseme = parse_document(read)
			print("\nOK. Done reading...\n")
			buildme = build_report(parseme)
			print("OK. Done building...\n")
			writeme = write_report(buildme,write)
		
		#if input is 2 read, combine, write
		elif option_input == 2:
			name1 = input("enter the name of the first file\n")
			name2 = input("enter the name of the second file\n")
			name3 = input("enter the name of the output file\n")
			
			readrep1 = read_report(name1)
			readrep2 = read_report(name2)
			
			combined = combine_reports(readrep1,readrep2)
			
			written = write_report(combined,name3)
		
		#quite if option is 3, tell loop to stop
		elif option_input == 3:
			print("Thanks!")
			runMenu = False
	


def main():
	print(parse_document("doc1"))
	#freq = {"hot":5,"dog":3,"cat":1,"buns":2,"jumbo":7,"laptop":1}
	#print(freq)
	#print(build_report(freq))
	#r1 = build_report(parse_document("test"))
	#r2 = build_report(parse_document("doc1"))
	#r3 = (combine_reports(r1,r2))
	#print(write_report(r3,"ultimate"))
	#print(read_report("random"))
	#run_menu()
	
main()
'''# please put this at the end of your file before submission:
def main():
	import tester
	tester.runtests(__file__)
if __name__=="__main__":
	main()'''