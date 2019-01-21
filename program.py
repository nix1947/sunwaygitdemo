print("Hello world")


def sum(*a):
  sum = 0
  for num in a:
     sum += num
  
  return sum


x = sum(1,2,3)

print("Sum of 1,2,3 is", x)



    


