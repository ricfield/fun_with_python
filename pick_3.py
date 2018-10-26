import random

RAND_MIN = 0                                                                                                                                                             
RAND_MAX = 9                                                                                                                                                             
MAX_COMPARISONS = 1000 

i = 0
j = 0
k = 0 

pick_3_numbers = [0, 0, 0]
user_input = [0, 0, 0]

random.seed()


user_input[0] = input("Enter first number: ")
user_input[1] = input("Enter second number: ")
user_input[2] = input("Enter third number: ")

print("\nRunning comparisons...\n")

for i in range(1, MAX_COMPARISONS):
   
   pick_3_numbers = [random.randint(RAND_MIN, RAND_MAX), random.randint(RAND_MIN, RAND_MAX), random.randint(RAND_MIN, RAND_MAX)]   

   
   if int(user_input[0]) == pick_3_numbers[0] and int(user_input[1]) == pick_3_numbers[1] and int(user_input[2]) == pick_3_numbers[2]:
      print("STRAIGHT MATCH FOUND AT DRAW " + str(i))

   if int(user_input[1]) == pick_3_numbers[1] and int(user_input[2]) == pick_3_numbers[2]:
      print("BACK MATCH FOUND AT DRAW " + str(i))

   if int(user_input[0]) == pick_3_numbers[0] and int(user_input[1]) == pick_3_numbers[1]:
      print("FRONT MATCH FOUND AT DRAW " + str(i))
                                                                                                
     
print("\nComparisons completed.")

   

   
