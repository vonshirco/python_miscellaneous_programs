
hexNumbers = {
    '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15
}

#fuction to convert a string hexadecimal number into an interger decimal
def hexToDec(hexNum):
    #Iterate in the dictionery make sure the inputs/characters are in the dictionery
    for char in hexNum:
        if char not in hexNumbers:
            return None

    #initial variables       
    exponent = 0
    decimalValue = 0
    #Iterating through the characters backward by using string slice with -1
    for char in hexNum[::-1]:
        decimalValue = decimalValue + hexNumbers.get(char, 0) * (16**exponent)
        exponent = exponent + 1

    return decimalValue

while True: #Continue to prompt a user for inputs until they type exit
    #Prompt a user to enter an hexadecimal number
    userInput = input("Enter a Hexadecimal number (or type 'exit to quit'): ")

    #Check if the user input after converting to lower case (by lower() function) is exit, inorder to break the loop
    if userInput.lower() == 'exit':
        break

    #Calling the function
    ans = hexToDec(userInput)

    #Displaying the answer/output
    if ans is not None:
        print(f"The decimal number of {userInput} is: {ans}")
    else:
        print("Invalid input. Please enter a valid hexadecimal number.")

