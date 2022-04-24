rows, cols = (3,8)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)
ticket = [4,2,1,3,3,2]
count34 = count2 = count1 = 0
for i in ticket:
  if(i == 4 or i == 3): 
    for j in range(i):
      arr[count34][2+j]=1
      print(str(count34+1) + "a")
    count34 = count34 + 1
print(arr)
