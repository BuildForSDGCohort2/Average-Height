# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  #print(student_heights[n]) #prints each element on the student_heights list

  sum += student_heights[n] # sums the elements on the student_heights list

#print(sum) #prints the sum of all elements on the student_heights list
#print(len(student_heights)) #prints the number of elements in the student_heights list
Average_height =round(sum / len(student_heights)) # Calculates the average 
print(f" Average height of students is {Average_height}.")
#Write your code below this row 👇




