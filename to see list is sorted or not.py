list = [1,2,3,4,5,6,7,8,9]

for i in range(len(list)-1):
    if list[i] <= list[i+1]:
        continue

    else:
        print("The list is not sorted.")
        break
else:
    print("The list is sorted.")
