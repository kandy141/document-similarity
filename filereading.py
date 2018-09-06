import sys,os
def filesread():
    path="E:/Python32/files/"
    for filename in os.listdir(path):
        print(path+filename)
