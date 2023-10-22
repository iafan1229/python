from defs.indeed import getIndeedData
import csv

indeed = [['타이틀','링크','회사이름','회사위치']]
temp = []

for number in range(5):
  temp.append(getIndeedData('python',number*10))

for item in temp:
    for data in item:
       if data is not None:
         indeed.append(data)

# print(indeed)
# CSV 파일로 데이터 쓰기
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for row in indeed:
        writer.writerow(row)
