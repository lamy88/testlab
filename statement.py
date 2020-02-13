st = 'Print every word in this sentence that has an even number of letters'
s = st.split(" ")
  for x in s:
    if (len(x)%2) == 0:
      print("Even!")
    else:
      print(x)
