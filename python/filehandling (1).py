import os

file = open("demo.txt", "w")
file.write("hii")
file.write(" hello")
file.close()

file = open("demo.txt", "r")  
print("reading the file :")
print(file.read())
file.close()
