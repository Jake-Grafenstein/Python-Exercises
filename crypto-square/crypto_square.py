import string
import math

def encode(myInput):
    counter = 0
    myString = ''
    # Remove white space
    string = myInput.replace(" ", "")

    # Remove any non alphanumeri characters
    for letter in string:
        if (not(letter.isalnum())):
            string = string.replace(letter,"")

    string = string.lower()
    nearestSquare = int(math.ceil(math.sqrt(len(string))))

    # Initialize double array for square and put items in square
    code = [[0 for x in range(nearestSquare)] for y in range(nearestSquare)]
    for index in range(nearestSquare):
        for secondIndex in range(nearestSquare):
            if (counter >= len(string)):
                break
            else:
                code[index][secondIndex] = string[counter]
                counter += 1

    # pull items off square and put in new string
    for index in range(nearestSquare):
        for secondIndex in range(nearestSquare):
            myLetter = code[secondIndex][index]
            if (myLetter):
                myString += str(myLetter)
        myString += " "

    # Remove trailing white space
    myString = myString.rstrip()
    return myString
