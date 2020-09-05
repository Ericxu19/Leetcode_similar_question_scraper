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
#remove the examples from the dataset
for name, r in dic:
    r[0] = re.sub("Example\s\d+(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Note:(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("For example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Follow up:(.|\s)*$", '', str(r[0]))
    r[0] = r[0].rstrip('\n')
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
                if random.random() <= 0.2:
                    row.append('dev')
                writer.writerow(row)
for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if sname != name and all(item in sr[2] for item in r[2]):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(4.0)
                if random.random() <= 0.2:
                    row.append('dev')
                writer.writerow(row)

for name,  r in dic:
    if len(r[2]) == 2:
        for sname, sr in dic:
            if sname != name and all(item in sr[2] for item in r[2]):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(3.0)
                if random.random() <= 0.2:
                    row.append('dev')
                writer.writerow(row)

for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if sname != name and len(set(r[2]) &set(sr[2])) >= 3:
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(3.5)
                if random.random() <= 0.2:
                    row.append('dev')
                writer.writerow(row)

for name,  r in dic:
    if len(r[2]) >= 3:
        for sname, sr in dic:
            if len(sr[2]) >= 3 and sname != name and not(any(item in sr[2] for item in r[2])):
                row = []
                row.append(r[0])
                row.append(sr[0])
                row.append(0.0)
                if random.random() <= 0.2:
                    row.append('dev')
                writer.writerow(row)  

#make a 20 percent dev set       

leetData.close()
Qcollection.close()
qbank.close()
