#PARAMETER: inputValue is float type
modulusFactor = 2

def primeNumber (inputValue) : 
    if (inputValue % modulusFactor) == 1 :
        return("prime number found")
    else :
        return("not a prime number")
    

#driver
print(primeNumber(11))

