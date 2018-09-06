import re
import sys,os
import cx_Oracle
con=cx_Oracle.connect('scott/tiger@127.0.0.1/XE')
cus=con.cursor()
#par=input("ENTER THE PARAGRAPH  : \n")
path='C:/Python27/files/'
for filename in os.listdir(path):
    fil=open(path+filename,"r")
    par_list=list(re.compile('[.?]').split(fil.read()))
    print(par_list)
    for x in par_list:
        temp=list(re.compile('[ ]').split(x))
        temp_size=len(temp)
        if len(temp[temp_size-1])==1:
        
    #print(par_list)
    for sen in par_list:
            cus.execute('insert into testing(NAME) values(\''+sen+'\')')
            cus.execute('commit')
