def calculator(operator,num1,num2):
  if not isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
    return "Invaild Numbers"
  elif operator == "+":
    return num1+num2
  elif operator == "-":
    return num1-num2
  elif operator in ["x", "X", "×", "*"]:
    return num1*num2
  elif operator == "/":
    return num1/num2
  elif operator == "**":
    return num1**num2
  else:
    return "Invalid Operator!"

operator = input("Enter Operation\n")
num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter Second Number\n"))
print(str(num1) +" "+ operator +" "+ str(num2) +" "+ "= ")
print(calculator(operator,num1,num2))