# 1. vectors when you want to create a vector with one onr more elements you should use c() function which means combine the elements into a vector
# creating a vector
fruits=c("apple","orange")
print(class(fruits))
print(fruits)

# 2.Lists 
# a list is an Robject which can contain many different types of elements inside it like a vector functions even another list inside it 
cars=list(c("maruti","skoda"))
print(class(cars)) #list
print(cars)

# 3.matrics
# a matrix is a two dimensional rectangular data set it can be created using a vector input to the matrix function
m=matrix(c("a","b","c","d","e","d"),nrow=2,ncol=3,byrow=TRUE)
print(class(m)) 
print(m)


# 4.Arrays 
# arrays can be any number of dimensions the array function takes a dim arrtibute which creates the required number of dimensions 
array=array(c("green","red"),dim=c(3,3,2))
print(array)

# 5.factors 
# factors are R objects which are created using a vector it stores the vectors along with the distinct values of the elements of the vector as lables the lables are always
# characters irrespective of whether it is numeric or character 

factor_apple=factor(fruits)
print(factor_apple)#Levels: apple orange
print(nlevels(factor_apple))# 2