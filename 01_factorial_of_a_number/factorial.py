def factorial(num):
    if type(num) is not int:
        return None #If the inputed number is not an integer
    if num < 0:
        return None #If a negative number is inputed
    if num == 0:
        return 1
    
    results = num * factorial(num - 1)

    return results

# #Printing to the terminal
# print(factorial(10))

#Prompt a user to enter a number
user_input = input("Please enter a number: ")

#Storing user input an calling the function
num = int(user_input)
ans  = factorial(num)

#Printing to the terminal
print(f"The factorial of {num} is: {ans} ") #F-strings - the string containing placeholders for variables/expressions in {}