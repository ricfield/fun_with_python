import json, time, random


range_beginning = 1
range_end = 1000000000
rows = 50
columns = 5000
array_a = [[0] * columns] * rows
array_b = [[0] * columns] * rows
result = [[0] * columns] * rows
start_time = 0
end_time = 0
start_time = time.time()
debug = False


def makeRandArray(event, context):
   for k in range(rows - 1):
      for l in range(columns - 1):
         array_a[k][l] = random.randint(range_beginning, range_end)
         array_b[k][l] = random.randint(range_beginning, range_end)

   for i in range(rows - 1):
      for j in range(columns - 1):
         result[i][j] =  array_a[i][j] + array_b[i][j]

        	  	    
   end_time = time.time()
   return end_time - start_time
   
