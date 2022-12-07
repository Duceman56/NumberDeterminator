evenFactor = 2

#PARAMETER: inputValue is float type

def determineNumber(inputValue) :
    """
    determineNumber determines if the input value is even or odd

    _extended_summary_

    :param inputValue: the value to be determined
    :type inputValue: float
    """
    if (inputValue / evenFactor).is_integer() : # if the input value is even
        return("Even")
    else :
        return("Odd")

    if inputValue / 1 == 0 : # if the input value is a whole number
        return("True")
    else :
        return("False")



#driver
print(determineNumber(11))