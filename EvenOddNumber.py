evenFactor = 2

#PARAMETER: inputValue is float type

def evenOddNumber (inputValue) : 
    if (inputValue / evenFactor).is_integer() :
        return("Even")
    else :
        return("Odd")

#driver
print(evenOddNumber(23))
