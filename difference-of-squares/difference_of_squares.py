def difference(number):
    squareOfSum = square_of_sum(number)
    sumOfSquare = sum_of_squares(number)
    return squareOfSum - sumOfSquare

def square_of_sum(number):
    count = 0
    for index in range(number+1):
        count += index
    count = count**2
    return count

def sum_of_squares(number):
    count = 0
    for index in range(number+1):
        count += index**2
    return count
