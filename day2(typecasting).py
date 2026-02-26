#Explicit Typecasting (datatype converted by developer according to requirenment)
a = "15"
b = 7
c = int(a) #it will convert str into int if int is written as str 
sum = b + c
print(sum)

#Implicit Typecasting (datatypes converted by python interpreter itself)
a = 7
b = 3.0
c = a + b
print(c)