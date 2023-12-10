# this is a simplch can write text to a text file
file= open("random.txt", "r")
fileout=open("randomlens.txt", "w")
for line in file:
    a=line.split(" ")
    fileout.write(str(len(a))+" is length of :"+line )
file.close()
