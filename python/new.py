print("Hello World")
print("My name is Anna")
teachername ="Anna" 
teacherage =31
print("teacher's name is " ,teachername)
print("teacher's age is" ,teacherage)


myName ="Anna"
myOccupation = "Educationist"

print("My name is %s I am a %s" % ( myName, myOccupation))

print(type(myName))
print(type(myOccupation))



def sum ( first, second ):
    sum = first + second
    return sum

print(sum(10,5))



def calculate (action,firstNum,secondNum): 
    if action == "multiply":
      result = firstNum * secondNum
      return  result


    elif action == "division" :
      result = firstNum / secondNum
      return result
    

calcResult = calculate("division",10,5)
print( "The result is ",calcResult)






 





