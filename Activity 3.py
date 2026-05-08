Amount =int(input("Please Enter Amount for Withdraw :"))

#number of notes
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print( "Number of 100 rupee notes" , note_1)
print("Number of 50 rupee notes" , note_2)
print("Number of 10 rupee notes" , note_3)
