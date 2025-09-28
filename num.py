# built in function
print(abs(-5))
print(pow(2,3))
print(round(2.7))
#num list
num_list = [2,3,4,5,1,7]
square_list=(map(lambda num:num**2,num_list))
print(square_list)
s=(0,1,2,3,4,5,6,7)
square=(lambda num:num**2, s in range (0,11))
for s in s:
    print(s)