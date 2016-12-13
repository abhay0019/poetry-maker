import random
import sys

def poem():
  i=0
  f=open("combined.txt","r")
  vect=(f.read()).split('\n')
  str=''
  while i<5:
    str+=random.choice(vect)+' '+random.choice(vect)+' , '+random.choice(vect)+' '+random.choice(vect)+'\n'
    i=i+1
  return str
  
def copy(filename):
  f=open(filename,'r')
  str=f.read()+'\n'
  f1=open('combined.txt','a')
  f1.write(str)
  f1.close()

args=sys.argv[1:]
f=open("combined.txt","w")
f.write("")
f.close()
f=open("poem.txt","w")
f.write("")
f.close()
for file in args:  
  copy(file)
str=poem()
print str
