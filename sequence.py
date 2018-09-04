#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.

n = int(input("Enter the length of the sequence: ")) # Do not change this line  
tala1 = 1
tala2 = 2
tala3 = 3

gildi = 0 #gildið sem notast á við
if n == 0:
    print("Veldu heiltölu stærri en 0")
elif n == 1:
    print(tala1)
elif n == 2:
    print(tala2)
elif n == 3:
    print(tala3)
elif n > 3:
    print(tala1)
    print(tala2)
    print(tala3)
    for n in range(3,n):
        gildi = tala1 + tala2 + tala3
        if gildi > 0:
            print(gildi)
        tala1 = tala2
        tala2 = tala3
        tala3 = gildi 



