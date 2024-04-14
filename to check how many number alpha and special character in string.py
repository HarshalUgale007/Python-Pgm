
str =  "h23y?<6>lk%kug43nk54^j87ug&@iul"
alp = 0
dig = 0
spl = 0

for i in str:
  if i.isalpha():
    alp += 1
  elif i.isdigit():
    dig += 1
  else:
    spl += 1

print("Alphabets:",alp)
print("Digits:",dig)
print("Special Characters:",spl)