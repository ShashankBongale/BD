import time
import operator
def question1():
    d = dict()
    for i in range(1,len(l)):
        l1 = l[i].split(',')
        key_name = l1[2]+"-"+l1[3]
        if(not('no wicket' in l[i] and int(l1[5])==0)):
            if(key_name in d.keys()):
                d[key_name] = d[key_name] + int(l1[5])
            else:
                d[key_name] = int(l1[5])
    b = dict()
    pair_list =[]
    for i in bowler:
        max_score = 0
        for j in d.keys():
            l1 = j.split('-')
            if(i == l1[1] and d[j]>=max_score):
                max_score = d[j]
                pair = j
        if(pair in b.keys()):
            pair = pair + "1"
        b[pair] = max_score
    print("Bowler Vulnerability")
    #print(len(b))
    sort=sorted(b.items(),key=lambda kv:kv[1])
    print(sort)
def question2():
    d = dict()
    for i in range(1,len(l)):
    	l1=l[i].split(',')
    	key_name = l1[2]+'-'+l1[3]
    	if('no wicket' not in l[i]):
    		if(key_name in d.keys()):
    			d[key_name] = d[key_name] + 1
    		else:
    			d[key_name] = 1
    b = dict()
    pair = ""
    for i in batsman:
        max_out = 0
        for j in d.keys():
            l1 = j.split('-')
            if(i == l1[0] and d[j]>=max_out):
                max_out = d[j]
                pair = j
        if(pair in b.keys()):
        	pair = pair + "1"
        b[pair] = max_out
    print("Batsman Vulnerability")
    #print(len(b))
    sort=sorted(b.items(),key=lambda kv:kv[1])

    print(sort)
fp = open("data.txt","r")
l=fp.readlines()
batsman = []
bowler = []
for i in range(1,len(l)):
    l1 = l[i].split(',')
    batsman.append(l1[2])
    bowler.append(l1[3])
batsman=list(set(batsman))
bowler=list(set(bowler))
start_question1 = time.time()
question1()
end_question1 = time.time()
print("Time taken for Bowler Vulnerability",end_question1-start_question1)
start_question2 = time.time()
question2()
end_question2 = time.time()
print("Time taken for Batsman Vulnerability",end_question2-start_question1)
#['inings', 'ball_number', 'batsman', 'bowler', 'non-striker', 'runs', 'extras', 'batsman_out\n']
