

import random

counter = 0
sixcounter = 0
fourcounter = 0
excatlynum = 0
maxnum = 3
numDlocD = 0
numDlocY = 0


tenlist = []
sixchoicerlist=[]
fourchoicerlist=[]


while counter < 10:
    
    tennum= int(random.random()*100)
    
    tenlist.append(tennum)
    counter += 1
    

while sixcounter < 6:
    
    sixchoircer=random.choice(tenlist)
    
    sixchoicerlist.append(sixchoircer)
    sixcounter= sixcounter +1
    
while fourcounter < 4:
    
    fourchoircer=random.choice(sixchoicerlist)
    
    if fourchoicerlist.count(fourchoircer) == 0:
        
        fourchoicerlist.append(fourchoircer)
        fourcounter= fourcounter +1
    
print(tenlist)
print(sixchoicerlist)
print(fourchoicerlist)

while excatlynum < maxnum :
    
    number = int(input("Guess the number :"))
    location = int(input("Guess the number location :"))
    
    print("{} your remaining chance".format(maxnum - excatlynum))
    excatlynum += 1
    
    numcount = fourchoicerlist.count(number)
    
    try:
        
        locationcount = fourchoicerlist.index(number)
    except:
        
        print("You lost :( ")
    
    if numcount > 0 and locationcount == location:
        numDlocD += 1
        
    elif numcount > 0 and locationcount != location:
        numDlocY += 1
    
    print("D:",numDlocD)
    print("Y:",numDlocY)
    
    
    
    