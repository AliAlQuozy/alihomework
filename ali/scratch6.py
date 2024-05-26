
quiz=open('./question.txt','r')
Name=input('Enter Your Full Name')
Age=input('Enter Your Age')
Number=input('Enter Your Number')
a =[]
ca = ['2','4','6','12','15','20','25','33','45','50','60','65','66','70','80','100','105','110','120','130']
result = 0
print(f'Student Info:Name:{Name},Age:{Age},Number:{Number}')
print('Start!')
for Q in range(20):
  A=input(f'{quiz.readline()}')
  a.append(A)
for i in range (20):
  if a[i] == ca[i] :
   result += 0.5
import json
Details={"Name":Name,"Age":Age,"Number":Number,"Result":result}
with open(".\Result.json","w") as  file:
             json.dump(Details,file)
