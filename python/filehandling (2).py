import os

file = open("demo.txt", "w")
file.write("                 (this is first line)")
file.write(" hello")
file.close()

file = open("demo.txt", "r")  
print("reading the file :")
print(file.read())
file.close()

file=open("demo.txt","a")
file.write("\n hello")
file.close()

file=open("demo.txt","r+")
file.write("this is r+ mode")
file.seek(0)
file.close()

#if os.path.exists("demo.txt"):
 #   os.remove("demo.txt")
  #  print("\n file deleted")
#else:
  #    print("file not found")