import os

file = open("demo.txt", "w")
file.write("                 (this is first line of the file)")
file.write(" hello")
file.close()

file = open("demo.txt", "r")  # Corrected this line
print("reading the file :")
print(file.read())
file.close()

file=open("demo.txt","a")
file.write("\n this is appended line")
file.close()

file=open("demo.txt","r+")
file.write("this is r+ mode")
file.seek(0)
file.close()

  