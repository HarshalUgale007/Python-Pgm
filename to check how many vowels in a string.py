# ! # $ % _- +  "" ? *  <  >  % ^ & @  {}  ():  ()

string =  "my name is bond james  bond , a detactive"
vowel = 0
const = 0
for i in string:
  if i in "aeiouAEIOU":
    vowel += 1
  elif i ==  " ":
    continue
  else:
    const += 1
print(f"your total vowels are {vowel} and your total constants are {const}")