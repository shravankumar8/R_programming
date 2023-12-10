cities=["mumbai","newyork","paris"]
countries=["india","usa","france"]
zip1=zip(cities,countries)
# zip merges two arrays can create a objactof that 
for i in zip1:
    print(i)

d={cities:countries for city ,countries in zip(cities,countries)}  
print(d)  