def question1(batsman,bowler):
    count = 0
    for i in range(1,len(l)):
        l1=l[i].split(',')
        if((batsman == l1[2]) and (bowler == l1[3]) and ('no wicket' in l[i])):
            count = count + int(l1[5])
    return(count)
def question2(batsman,bowler):
    count = 0
    for i in range(1,len(l)):
        l1=l[i].split(',')
        if((batsman == l1[2]) and (bowler == l1[3]) and ('no wicket' not in l[i])):
            count = count + 1
    return(count)
fp = open("final_original_data.txt","r")
l=fp.readlines()
count = 0
batsman = input("Enter batsman name")
bowler = input("Enter bowler name")
print("Enter your choice")
print("1.Batsman Vulnerability")
print("2.Bowler Vulnerability")
number = int(input())
if(number == 1):
    result = question1(batsman,bowler)
else:
    result = question2(batsman,bowler)
print(result)
