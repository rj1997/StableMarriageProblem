from collections import defaultdict

def printdict(dict):
	for k,v in dict.items():
		print(k,v)

temp_engagement = {}
male_pref = defaultdict(list)
female_pref = defaultdict(list)

# File reading starts here

f = open('mp.txt')
for item in (f.read().strip().split()):
	if ':' in item:
		maleanimal = item.split(':')[0]
	else:
		male_pref[maleanimal].append(item.replace("'","").replace(",","").replace("[","").replace("]",""))

f2 = open('fp.txt')
for item in (f2.read().strip().split()):
	if ':' in item:
		femaleanimal = item.split(':')[0]
	else:
		female_pref[femaleanimal].append(item.replace("'","").replace(",","").replace("[","").replace("]",""))

# File reading ends here

males = len(male_pref)
females = males

print('Preference list of males here : ')
printdict(male_pref)
print('Preference list of females here : ')
printdict(female_pref)

day = 0

counter = dict.fromkeys([key for key,value in female_pref.items()],0 )

while len(temp_engagement) is not males:

	femalecontenderslist = defaultdict(list)

	for key,value in female_pref.items():
		if key not in temp_engagement.values():
			chosenmale = female_pref[key][counter[key]]
			#sendProposal(chosenmale,key)
			femalecontenderslist[chosenmale].append(key)
			counter[key] = counter[key] + 1

	for key,value in male_pref.items():
		if key in temp_engagement.keys():
			femalecontenderslist[key].append(temp_engagement[key])
		for item in femalecontenderslist[key]:
			if femalecontenderslist[key].index(item) == 0:
				femalenametillnow = item
				temp_engagement[key] = item
			if male_pref[key].index(item) <= male_pref[key].index(femalenametillnow):
				femalenametillnow = item
				temp_engagement[key] = item

	print('At the end of day',day+1,":")
	printdict(temp_engagement)

	day = day + 1


	# for key,value in female_pref:
	# 	chosenmale = female_pref[key][day]
	# 	if chosenmale not in temp_engagement:
	# 		temp_engagement[chosenmale] = key
	# 	else:
	# 		if male_pref[chosenmale].index(key) < male_pref[chosenmale].index(temp_engagement[chosenmale]):
	# 			temp_engagement[chosenmale] = key
	# day = day + 1
