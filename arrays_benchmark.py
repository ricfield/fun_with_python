import time, random

range_beginning = 1
range_end = 1000000000
rows = 5000
columns = 5000
array_a = [[0] * columns] * rows
array_b = [[0] * columns] * rows
result = [[0] * columns] * rows
start_time = 0
end_time = 0
start_time = time.time()
debug = False

print("Starting time value: " + str(start_time))

for k in range(rows - 1):

   if k % 100 == 0:
      print("\nWriting random values to row " + str(k + 1) + " in array_a and array_b...")
      
   
   for l in range(columns - 1):
      array_a[k][l] = random.randint(range_beginning, range_end)
      array_b[k][l] = random.randint(range_beginning, range_end)

      if debug == True and l % 1000 == 0 and k % 100 == 0:
         print(str(array_a[k][l]) + "," + str(array_b[k][l]))

print("Done writing values to array_a and array_b.)\n")


print("Adding array_a to array_b...")

for i in range(rows - 1):


   for j in range(columns - 1):
      result[i][j] =  array_a[i][j] + array_b[i][j]
      
   if i % 100 == 0:
      print("Processed row " + str(i + 1) + "...")

      if debug == True:
         print("array_a[" + str(i) + "][" + str(j) + "] = " + str(array_a[i][j]))
         print("array_b[" + str(i) + "][" + str(j) + "] = " + str(array_b[i][j]))
         print("result[" + str(i) + "][" + str(j) + "] = " + str(result[i][j]) + "\n") 

          	  	    
end_time = time.time()

print("Ending time value: " + str(end_time))
print("Total Time: " + str(end_time - start_time))	  
