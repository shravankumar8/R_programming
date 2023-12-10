numbers=[ i for i in range(0,10)]
# this array stores the even numbers
even=[i for i in numbers if i%2==0]
# this array stores odd numbers
odd=[i for i in numbers if i%2!=0]
# this array stores square of numbers
squr=[i*i for i in numbers]
print(numbers)
print(even)  
print(odd)
print(squr)