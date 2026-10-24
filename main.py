try:
    a = int(input("enter  the frist number: "))
    b = int (input("inter second number : "))
    print("what kind of opreation do you want to perfform. press + for addition, - for substraction, * for multiplication, / for division")
    opreation = input("enter the opreatin; ")
    match opreation:
        case "+":
            print("the sum of two number is : ", a + b)
        case "-":
            print("the difference of two number is : ", a - b)
        case "*":
            print("the product of two number is : ", a * b)
        case "/":
            print("the quotient of two number is : ", a / b)
        case _:
            print("Invalid opreation")
except Exception as e:
     print("please enter valid number")
         











         
    
    
        
            
    



