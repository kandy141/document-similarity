import re
f=open("C:/Python32/files/k1.txt","r")
g=open("C:/Python32/files/k11.txt","r")
h=open("C:/Python32/files/temp.txt","w")
first=re.split('\. ',f.read())
second=re.split('\. ',g.read())
f.close()
g.close()
count1=0
count2=0
tempcount1=0
tempcount2=0
for char in first:
    sp=re.split(' ',char)
    for i in range(0,len(sp)-4):
        count1=count1+1
        poi=''
        for x in range(0,5):
            poi=poi+str(sp[i+x])+' '
        #print(poi)
        for y in second:
            if poi[:-1] in y:
                #print(poi)
                h.write(poi+'.')
h.close()
for char in second:
    sp=re.split(' ',char)
    for i in range(0,len(sp)-4):
        count2=count2+1
h=open("C:/Python32/files/temp.txt","r")
temp=re.split(' \.',h.read())
print(temp)
for a in temp:
    for char in first:
        if a in char and a!='':
            tempcount1=tempcount1+1
            #print(a)
    for char in second:
        if a in char and a!='':
            tempcount2=tempcount2+1
print(tempcount1)
print(count1)
print(count2)
print(tempcount2)
print(tempcount1/count1*100)
print(tempcount2/count2*100)
