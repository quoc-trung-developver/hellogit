'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
N = input (">>")
I = 0
while I == 0:
    if N == "R":
        f = input("file: ")
        j = open (j,"r+")
        i = f.read()
        print (i)
        f.close()
    elif N == "E":
        break
    else:
        print ("os")
    N = input (">>")
        
