## Function and Methods Homework

## Calculate volume of sphere

def vol(rad):
  v = (4/3) * (3.14) * (rad**3)
  return v

print(vol(2))


## Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
  return num >= low and num <= high

print(ran_check(3,1,10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    cupper =0
    clower =0
    for item in s:
      if item.islower(): clower +=1
      if item.isupper(): cupper +=1
    print(f,'Original String : {s}')
    print(f,'No. of Upper case characters : {cupper}')
    print(f,'No. of Lower case Characters : {clower}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
