x={"a","b","c","d","e"}
y={"a","j","h","g","f"}
a={"a","b"}

print("f" in x|y) #or operator
print(x | y)#this is a or operator will print element both in x and y
print(x & y)#prints the elements which are in x and y
print(x - y)#this prints difference elements in x and y
print(x >a)#subset checks if y elements are subset of x