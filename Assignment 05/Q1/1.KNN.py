import csv
file=open("UCS411 Artificial Intelligence/Lab/Assignment 05/Q1/1.Dataset.csv")
type(file)
csvreader=csv.reader(file)

#INPUT
###############################
data=[5, 8, 10]
#data=[8, 7, 6]
###############################


header=[]
header=next(csvreader)

rows=[]
distance=[]
for row in csvreader:
    #Convert string to int
    for i in range(0, len(row)):
        row[i]=int(row[i])

    rows.append(row)

    distance.append( pow( (pow(row[0]-data[0], 2) + pow(row[1]-data[1], 2) + pow(row[2]-data[2], 2)), 0.5 ) )

file.close()

index=distance.index(min(distance))
print(f"Predicted salary: {rows[index][3]}")