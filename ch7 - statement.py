### Statement Assessment Test
## 1
st = 'Print only the words that start with s in this sentence'
s = st.split(" ")
for x in s:
  if x[0] == 's': print(x)

## 2

numlist = range(0,11)
for x in numlist:
  if (x % 2) == 0: print(x)


## 3
numlist = range(1,51)
for x in numlist:
  if (x % 3) == 0: print(x)

## 4
st = 'Print every word in this sentence that has an even number of letters'
s = st.split(" ")
  for x in s:
    if (len(x)%2) == 0:
      print("Even!")
    else:
      print(x)

## 5
numlist = range(1,101)
for x in numlist:
  if (x % 3) == 0 and (x % 5) == 0: print('FizzBuzz')
  elif (x % 3) == 0 : print('Fizz')
  elif (x % 5) == 0: print('Buzz')
  else : print(x)
