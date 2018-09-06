import re
from time import clock

def func():
    q1=''
    q2=''
    print('ENTER THE 1st TEXT DOC NAME : ')
    q1=input(q1)
    print('ENTER THE 2nd TEXT DOC NAME : ')
    q2=input(q2)
    print('     ******    DOCS COMPARISION IS STARTING...    ******')
    print('------------------------------------------------------------------')

    m=clock()
    f=open("C:/Python32/files/txt's/"+q1+".txt","r")
    g=open("C:/Python32/files/txt's/"+q2+".txt","r")
    h=open("C:/Python32/files/temp.txt","w")
    first=re.split('\.\\n|\. |\. \\n',f.read())
    second=re.split('\.\\n|\. |\. \\n',g.read())
    f.close()
    g.close()
    list1=[]
    list2=[]
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
            list1.append(poi[:-1])
        #print(count1)
        #print(poi)
        #print(count1)
    for char in second:
        sp=re.split(' ',char)
        for i in range(0,len(sp)-4):
            count2=count2+1
            poi=''
            for x in range(0,5):
                poi=poi+str(sp[i+x])+' '
            list2.append(poi[:-1])
    for x in list1:
        for y in list2:
            if x==y:
                #print(x)
                h.write(x+' .')
    h.close()
    h=open("C:/Python32/files/temp.txt","r")
    temp=set(re.split(' \.',h.read()))
    #print(list1)
    #print(list2)
    #print(temp)
    for a in temp:
        for x in list1:
            if str(a)==str(x) and a!='':
                #print(a)
                tempcount1=tempcount1+1
                #print(tempcount1)
                #print(a)
        for y in list2:
            if a==y and a!='':
                tempcount2=tempcount2+1
    print('LENGTH OF 1st-LIST IS  -> ',len(list1))
    print('LENGTH OF 2nd-LIST IS  -> ',len(list2))
    #print(tempcount1)
    #print(count1)
    #print(count2)
    #print(tempcount2)
   
    if count1!=0 and count2!=0:
        print('\nPERCENTAGE OF TEMP IN 1st TEXT DOCUMENT IS -> ',tempcount1/count1*100,'%')
        print('PERCENTAGE OF TEMP IN 2nd TEXT DOCUMENT IS -> ',tempcount2/count2*100,'%')    
        n=clock()
        print('\nTIME TAKEN FOR COMPARISION -> ',n-m,' SECONDS.')
        print('------------------------------------------------------------------')
        print('DO U WANT TO CONTINUE [ y/n ]: ')
        ans=''
        ans=input(ans)
        if ans=='y':
            print('\n\n')
            func()
        else:
            print('\n\tE X I T I N G')
    else:
        print('\nEXCEPTION HANDLED , TRY ANOTHER FILE')
        print('\n\nDO U WANT TO CONTINUE [ y/n ]: ')
        ans=''
        ans=input(ans)
        if ans=='y':
            print('\n\n')
            func()
        else:
            print('\n\tE X I T I N G')
func()      
