num = int(input("Enter a number: "))

result = list(map(lambda x : 2 ** x, range(num+1)))
print (result)
for i in range(num +1):
  print(f"2 to the power of {i} is {result[i]}")