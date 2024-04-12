mat1 = [[4,5,2,],
        [5,7,3]]

result = [[0,0],
          [0,0],
          [0,0]]

for i in range(len(mat1)):
  for j in range(len(mat1[0])):
    result[j][i] = mat1[i][j]
for r in result:
  print(r)