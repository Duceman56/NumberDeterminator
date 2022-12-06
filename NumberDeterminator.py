evenFactor = 2

#PARAMETER: inputValue is float type

def determineNumber(inputValue) : 
    if (inputValue / evenFactor).is_integer() :
        return("Even")
    else :
        return("Odd")
        
    if inputValue / 1 == 0 :
        return("True")
    else :
        return("False")
    


#driver
print(determineNumber(11))