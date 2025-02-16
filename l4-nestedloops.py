#Ask user to type a word
string = input("Please enter your own word : ")
#take input of a character
char = input("Please enter your own Character : ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(string)): #string operation

    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1

#Display the result
print("The total Number of Times ", char, " has Occurred = " , count)


#find prime numbers between the range:
#take two input from user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# activity 3
# wap to find product of middle digits

#Input a number 
num = int(input("Enter the number : "))
t = num
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  t = int(t/10)

if numLen>=4: #condition 1
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    rem = num%10
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")
  
  
  # act 4 wap to find strong number
  
  #Ask user to enter a number
Number = int(input(" Please Enter any Number: "))
Sum = 0 #initialise
Temp = Number 

while(Temp > 0): #using while loop
    Factorial = 1   # fact variable with 1  
    #intialize with 1  
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i # Find factorial of each number  
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10
    
#display output
print("\n Sum of Factorials of a Given Number %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not a Strong Number" %Number)


# act 4
#Take input of number of rows
n=int(input("enter the number of rows: "))

#iterate loop for row
for i in range(n):
  #loop for columns
    for j in range(n):
        if j == i:
          print(i, j)
          
          

#_________________________________________________________________________


#Input a number 
num = int(input("Enter the number : "))
t = num
numLen = 0
#iterate the loop
while t>0: 
  numLen = numLen+1
  # calculate the number of digits in the number by repeatedly dividing the number by 10
  t = int(t/10)
#Check if the number has 4 or more digits
if numLen>=4: #condition 1
  #Extract the middle two digits: You divide numLen by 2 to find the position of the middle digits.
  numLen = int(numLen/2)
  chk = 0
  while num>0: #iterate loop
    #you iterate through each digit of the number (by dividing it by 10 at each step).
    rem = num%10
    #reach the middle positions (numLen-1 and numLen), you store those digits in midOne and midTwo.
    if chk==numLen: #nested condition 1
      midOne = rem
    elif chk==(numLen-1): 
      midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo #product of middle digits
  #display the result
  print("\nProduct of Mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")


# in class Aarav

# check the number of char in a string

string = input("Enter a word: ")
char = input("Enter the char you want to chek in the word")

i = 0
count = 0

while (i < len(string)):
  if string[i] == char:
    count =count+1
  i =i +1 

print("the total number of ", char , "in the ", string , "are", count)





