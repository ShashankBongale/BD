def question1():
    d = dict()
    for i in range(1,len(l)):
    	l1=l[i].split(',')
    	key_name = l1[2]+l1[3]
    	if('no wicket' in l[i]):
    		if(key_name in d.keys()):
    			d[l1[2]+l1[3]] = d[l1[2]+l1[3]] + int(l1[5])
    		else:
    			d[l1[2]+l1[3]] = int(l1[5])
    vul_dict = dict()
    key_list = list(d.keys())
    temp_list= []
    for i in range(len(batsman)):
        max_score = 0
        for j in range(len(key_list)):
            if(batsman[i] in key_list[j]):
                if(d[key_list[j]]>=max_score):
                    pair = key_list[j]
                    max_score = d[key_list[j]]
        vul_dict[batsman[i]] = max_score
def question2():
    d = dict()
    for i in range(1,len(l)):
    	l1=l[i].split(',')
    	key_name = l1[2]+l1[3]
    	if('no wicket' not in l[i]):
    		if(key_name in d.keys()):
    			d[l1[2]+l1[3]] = d[l1[2]+l1[3]] + 1
    		else:
    			d[l1[2]+l1[3]] = 1
    print("Bowler Vulnerability")
    print(d)
fp = open("final_original_data.txt","r")
l=fp.readlines()
batsman = []
bowler = []
for i in range(1,len(l)):
    l1=l[i].split(',')
    batsman.append(l1[2])
    bowler.append(l1[3])
batsman = list(set(batsman))
bowler = list(set(bowler))
print(len(batsman))
question1()
#question2()
