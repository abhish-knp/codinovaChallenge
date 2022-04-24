rows, cols = (3,8)
arr = [[0 for i in range(cols)] for j in range(rows)]
print("Intial Empty Array: \n", arr)
ticket = [4,2,1,3,3,2]
count34 = count2 = count1 = 0
seating = []
for i in ticket:
  if(i == 4 or i == 3): 
    for j in range(i):
      arr[count34][2+j]=1
      
      seating.append(str(count34+1) + "a")
    count34 = count34 + 1
  elif(i == 2):
    for k in range(i):
      arr[count2][6+k] = 1
      
      seating.append(str(count2+1) + "a")
    count2 = count2 + 1

print("Seats after getting filled: \n",arr)
print("Sitting order arrangement: \n",seating)
