import os
a=open("pyth.txt")
b=os.stat("apple.txt")
print("the size of the file in bytes is given below\n",b.st_size)
