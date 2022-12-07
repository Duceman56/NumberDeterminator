# Make a function to determine if a number is prime or not
def primeNumber_Check(inputValue) :
    """
    primeNumber_Check determines if the input value is prime or not

    _extended_summary_

    :param inputValue: the value to be determined
    :type inputValue: float
    """
    # a prime number is a number that is only divisible by itself and 1.
    # if the input value is divisible by 2, it is not prime
    if type(inputValue) == float :
        # if the input value is a float, it is not prime
        return False

    if inputValue == 1 :
        # if the input value is 1, it is not prime
        return False

    # check if the input value is divisible by any number other than itself and 1. One nice trick to know is that you only need to check up to the square root of the number. If the number is not divisible by any number up to the square root, then it is not divisible by any number.

    for i in range(2, int(inputValue ** 0.5) + 1) :
        if inputValue % i == 0 : # if the input value is divisible by any number other than itself and 1, it is not prime
            return False # if the input value is divisible by any number other than itself and 1, it is not prime

    return True # if the input value is not divisible by any number other than itself and 1, it is prime

# test the function with a few numbers
print(primeNumber_Check(1)) # 1 is not prime
print(primeNumber_Check(2)) # 2 is prime
print(primeNumber_Check(3)) # 3 is prime
print(primeNumber_Check(41)) # 41 is prime