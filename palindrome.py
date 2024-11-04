#palindrome program

user=input("Enter the Words:")
if (user==user[::-1]):
    print("It is a palindrome")
else:
    print("oops!, it is not a palindrome")    