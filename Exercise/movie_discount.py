# asking the user to enter their age
x = input("Enter your age: ")
# asking the user if they are student or not
y = input("Are you student? (yes/no): ").lower()
if x <= "12" :
        print("you are eligible for the discount on movie ticket")
elif (x >= "13" or x <= "18") and y == "yes" :
        print("you are eligible for the discount for movie ticket") 
else :
        print("you are not eligible for the movie discount ticket ")