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


def main():


   print("Starting time value: " + str(start_time))

   print("\nWriting values to array_a")
   writeRandomArrayValues(array_a, rows, columns, range_beginning, range_end) 

   print("\nWriting values to array_b")
   writeRandomArrayValues(array_b, rows, columns, range_beginning, range_end)
   
   print("\nDone writing values to array_a and array_b.)\n")

   print("\nAdding array_a to array_b...")


   addArrays(array_a, array_b)
   
  	  	    
   end_time = time.time()

   print("Ending time value: " + str(end_time))
   print("Total Time: " + str(end_time - start_time))	  


def addArrays(array1, array2):

   for i in range(rows - 1):


      for j in range(columns - 1):
         result[i][j] =  array1[i][j] + array2[i][j]
      
      if i % 100 == 0:
         print("Processed row " + str(i + 1) + "...")


def writeRandomArrayValues(array, numRows, numColumns, randIntBegin, randIntEnd):
   for k in range(numRows - 1):
                                                                                                                                                                                                                                                                                                               
      if k % 100 == 0:                                                                                                                                                   
         print("\nWriting random values to row " + str(k + 1))                                                                            
                                                                                                                                                                                                                                                                                                                                            
      for l in range(numColumns - 1):                                                                                                                             
         array[k][l] = random.randint(randIntBegin, randIntEnd)                        
                                                                                                                                                                                                                                                      
         
if __name__ == '__main__':
   main()


