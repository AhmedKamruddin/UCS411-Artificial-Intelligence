import csv
file=open("UCS411 Artificial Intelligence/Lab/Assignment 05/2.Dataset.csv")
type(file)
csvreader=csv.reader(file)

#BINS
###############################
#GradPercent
gradPercent=[0, 0, 0, 0]
#  Index
# 0 - outstanding
# 1 - good
# 2 - average
# 3 - bad

#Experience
exp=[0, 0, 0]
#   Index
# 0 - advanced
# 1 - intermediate
# 2 - novice

#WrittenScore
written=[0, 0, 0, 0]
#  Index
# 0 - outstanding
# 1 - good
# 2 - average
# 3 - bad

#InterviewScore
interview=[0, 0, 0, 0]
#  Index
# 0 - outstanding
# 1 - good
# 2 - average
# 3 - bad 

#Selection
selected=[0, 0]
#  Index
# 0 - yes
# 1 - no

prob_gradPercent=[[0, 0], [0, 0], [0, 0], [0, 0]]
prob_exp=[[0, 0], [0, 0], [0, 0]]
prob_written=[[0, 0], [0, 0], [0, 0], [0, 0]]
prob_interview=[[0, 0], [0, 0], [0, 0], [0, 0]]
prob_selected=[0, 0]
###############################

header=[]
header=next(csvreader)

rows=[]
for row in csvreader:
    #Convert string to int
    for i in range(0, len(row)):
        row[i]=int(row[i])
    
    rows.append(row)

    #GradPercent
    if(75<=row[0]):
        gradPercent[0]+=1
        if(row[4]==1):
            prob_gradPercent[0][0]+=1
        elif(row[4]==0):
            prob_gradPercent[0][1]+=1
        
    elif(50<=row[0] and row[0]<75):
        gradPercent[1]+=1
        if(row[4]==1):
            prob_gradPercent[1][0]+=1
        elif(row[4]==0):
            prob_gradPercent[1][1]+=1

    elif(25<=row[0] and row[0]<50):
        gradPercent[2]+=1
        if(row[4]==1):
            prob_gradPercent[2][0]+=1
        elif(row[4]==0):
            prob_gradPercent[2][1]+=1

    elif(row[0]<25):
        gradPercent[3]+=1
        if(row[4]==1):
            prob_gradPercent[3][0]+=1
        elif(row[4]==0):
            prob_gradPercent[3][1]+=1

    #Experience
    if(10<=row[1]):
        exp[0]+=1
        if(row[4]==1):
            prob_exp[0][0]+=1
        elif(row[4]==0):
            prob_exp[0][1]+=1

    elif(5<=row[1] and row[1]<10):
        exp[1]+=1
        if(row[4]==1):
            prob_exp[1][0]+=1
        elif(row[4]==0):
            prob_exp[1][1]+=1

    elif(row[1]<5):
        exp[2]+=1
        if(row[4]==1):
            prob_exp[2][0]+=1
        elif(row[4]==0):
            prob_exp[2][1]+=1

    #WrittenScore
    if(8<=row[2]):
        written[0]+=1
        if(row[4]==1):
            prob_written[0][0]+=1
        elif(row[4]==0):
            prob_written[0][1]+=1

    elif(5<=row[2] and row[2]<8):
        written[1]+=1
        if(row[4]==1):
            prob_written[1][0]+=1
        elif(row[4]==0):
            prob_written[1][1]+=1

    elif(3<=row[2] and row[2]<5):
        written[2]+=1
        if(row[4]==1):
            prob_written[2][0]+=1
        elif(row[4]==0):
            prob_written[2][1]+=1

    elif(row[2]<3):
        written[3]+=1
        if(row[4]==1):
            prob_written[3][0]+=1
        elif(row[4]==0):
            prob_written[3][1]+=1

    #InterviewScore
    if(8<=row[3]):
        interview[0]+=1
        if(row[4]==1):
            prob_interview[0][0]+=1
        elif(row[4]==0):
            prob_interview[0][1]+=1

    elif(5<=row[3] and row[3]<8):
        interview[1]+=1
        if(row[4]==1):
            prob_interview[1][0]+=1
        elif(row[4]==0):
            prob_interview[1][1]+=1

    elif(3<=row[3] and row[3]<5):
        interview[2]+=1
        if(row[4]==1):
            prob_interview[2][0]+=1
        elif(row[4]==0):
            prob_interview[2][1]+=1

    elif(row[3]<3):
        interview[3]+=1
        if(row[4]==1):
            prob_interview[3][0]+=1
        elif(row[4]==0):
            prob_interview[3][1]+=1    

    #Selection
    if(row[4]==1):
        selected[0]+=1
    elif(row[4]==0):
        selected[1]+=1
        
file.close()

#PROBABILITES
###############################
#prob_GradPercent
for i in range(0, len(gradPercent)):
    for j in range(0, 2):
        prob_gradPercent[i][j]/=selected[j]

#prob_Experience
for i in range(0, len(exp)):
    for j in range(0, 2):
        prob_exp[i][j]/=selected[j]

#prob_WrittenScore
for i in range(0, len(written)):
    for j in range(0, 2):
        prob_written[i][j]/=selected[j]

#prob_InterviewScore
for i in range(0, len(interview)):
    for j in range(0, 2):
        prob_interview[i][j]/=selected[j]

#prob_Selection
rowCount=sum(1 for row in rows)
for i in range(0, len(selected)):
    prob_selected[i]=selected[i]/rowCount
###############################


#INPUT
###############################
data=[90, 5, 8, 10]
#data=[75, 8, 7, 6]
###############################


#CLASSIFY DATA
###############################
#GradPercent
if(75<=data[0]):
    indexGradPercent=0
elif(50<=data[0] and data[0]<75):
    indexGradPercent=1
elif(25<=data[0] and data[0]<50):
    indexGradPercent=2
elif(data[0]<25):
    indexGradPercent=3

#Experience
if(10<=data[1]):
    indexExp=0
elif(5<=data[1] and data[1]<10):
    indexExp=1
elif(data[1]<5):
    indexExp=2

#WrittenScore
if(8<=data[2]):
    indexWritten=0
elif(5<=data[2] and data[2]<8):
    indexWritten=1
elif(3<=data[2] and data[2]<5):
    indexWritten=2
elif(data[2]<3):
    indexWritten=3

#InterviewScore
if(8<=data[3]):
    indexInterview=0
elif(5<=data[3] and data[3]<8):
    indexInterview=1
elif(3<=data[3] and data[3]<5):
    indexInterview=2
elif(data[3]<3):
    indexInterview=3
###############################

prob_x=(gradPercent[indexGradPercent]/rowCount) * (exp[indexExp]/rowCount) * (written[indexWritten]/rowCount) * (interview[indexInterview]/rowCount)

prob_x_yes=prob_gradPercent[indexGradPercent][0] * prob_exp[indexExp][0] * prob_written[indexWritten][0] * prob_interview[indexInterview][0]
prob_yes=prob_selected[0]

prob_x_no=prob_gradPercent[indexGradPercent][1] * prob_exp[indexExp][1] * prob_written[indexWritten][1] * prob_interview[indexInterview][1]
prob_no=prob_selected[1]

prob_yes_x=(prob_x_yes*prob_yes)/prob_x
prob_no_x=(prob_x_no*prob_no)/prob_x

print(f"P(Yes|X)={prob_yes_x}")
print(f"P(No|X)={prob_no_x}")