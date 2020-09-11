import json
import csv
import re 
import random

leetData = open('leetData.csv', 'r+')
Qcollection = open('Qcollection.csv', 'r+')
qbank = open("questionbank.json", 'r')
writer = csv.writer(leetData)
Qwriter = csv.writer(Qcollection)
data = json.load(qbank)
dic = data.items()

Qcol = []

count = 0
count5 = 0
count4 = 0
count3 = 0
count35 = 0
count1 = 0
count0 = 0
#remove the examples from the dataset
for name, r in dic:
    r[0] = re.sub("Example\s\d+(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Note:(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Note that(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("For example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Follow up:(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Suppose(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("You may assume(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Formally, (.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Answer this question(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("push(x) --(.|\s)*$", '', str(r[0]))
    r[0] = r[0].strip()
    r[0] = r[0].replace('\n', '')
    Qcol.append(r[0])

Qwriter.writerow(Qcol)
row = []
for name, r in dic:
    if r[1]:
        for qName in r[1]:
            if qName in data:
                row = []
                
                row.append(r[0])
                row.append(data[qName][0])
                row.append(5.0)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1 
                count5+=1
for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if sname != name and all(item in sr[2] for item in r[2]):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(4.0)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1 
                count4 += 1

for name,  r in dic:
    if len(r[2]) == 2:
        for sname, sr in dic:
            if sname != name and all(item in sr[2] for item in r[2]):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(3.0)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1 
                count3 +=1

for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if sname != name and len(set(r[2]) &set(sr[2])) >= 3:
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(3.5)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1 
                count35 += 1

for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if len(sr[2]) >= 3 and sname != name and not(any(item in sr[2] for item in r[2])):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(0.0)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1   
                count0 +=1

for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if len(sr[2]) >= 3 and sname != name and len(set(sr[2]).intersection(set(r[2]))) == 1:
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(1.0)
                ran = random.random()
                if ran<= 0.05:
                    row.append('test')
                elif ran <= 0.25:
                    row.append('dev')
                writer.writerow(row)
                count +=1   
                count1 +=1

#make a 20 percent dev set       

leetData.close()
Qcollection.close()
qbank.close()

print("total: " + str(count))
print("score 5: "+ str(count5))
print("score 4: "+ str(count4))
print("score 3: "+ str(count3))
print("score 3.5: "+ str(count35))
print("score 1: "+ str(count1))
print("score 0: "+ str(count0))