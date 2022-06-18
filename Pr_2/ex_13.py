import os
def printDir(path, rootDir):#path − This is the directory, which needs to be explored.
    list = os.listdir(path)#returns a list containing the names of the entries in the directory given by path.
    for i in list:
        if os.path.isdir(os.path.join(path, i)):#concatenates various path components
            print(rootDir + "->" + i)
            printDir(path + "\\"+ i, i)#used to Split the path name into a pair head and tail

def ex13(path):
    print('digraph G {')
    p = path.split('\\')
    printDir(path, p[len(p) - 1])
    print('}')

ex13(input())
#C:\\Program Files\\ARIS Express