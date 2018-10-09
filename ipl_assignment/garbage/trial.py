fp = open("cricket.txt","r")
l=fp.readlines()
count = 0
for i in range(len(l)):
	l1=l[i].split(',')
	#print(l1)
	if(l1[5]=='SK Raina' and l1[7] == 'PP Chawla' and l1[10] == ""):
		count = count + int(l1[8])
print(count)
#ball,innings,ball_no,team,on_strike,off_strike,bowler,runs,extras,dismissal_mode,batsman_out

#['245', 'ball', '2', '19.5', 'Gujarat Lions', 'DJ Bravo', 'KD Karthik', 'SR Watson', '4', '0', '', '\n']
