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
"""
print("No of batsman",len(batsman))
print(batsman)
print("No of bowlers",len(bowler))
print(bowler)
"""
batsman_bowler_run = dict()
for i in range(len(batsman)):
    for j in range(len(bowler)):
        count = 0
        #print(batsman[i]+bowler[j])
        for k in range(1,len(l)):
            l1 = l[k].split(',')
            if((l1[2] == batsman[i]) and (l1[3] == bowler[j]) and ('no wicket' not in l[k])):
                count = count + 1
        batsman_bowler_run[batsman[i]+bowler[j]] = count
        #print(count)
print(batsman_bowler_run)
