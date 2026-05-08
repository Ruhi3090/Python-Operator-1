English=float(input("Enter Your Marks for English: "))
Math=float(input("Enter Your Marks for Math: "))
Science=float(input("Enter Your Marks for Science: "))
Gp=float(input("Enter Your Marks for Gp: "))
Computing=float(input("Enter Your Marks for Computing: "))
German=float(input("Enter Your Marks for German: "))
#find sum
sum=English+Math+Gp+German+Computing+Science
print("Your total marks are: ",sum)
#percentage
per100=(sum/600)*100
print("The overall percentage you recieved is: ",per100)
