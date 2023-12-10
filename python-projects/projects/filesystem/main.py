data=input("enter the data :")
filename=input("enter the filename :")
decision=input("do you want to data the data with the file "+filename+".txt(y/n)")
if decision=="y":
    with open(filename+".txt","w+") as f:

        f.write(data)
        f.close
else:
    print("hell you for not saving the data with the file "+filename+".txt(y/n)")    


