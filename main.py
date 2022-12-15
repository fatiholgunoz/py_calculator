#Calculator

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("\nWhat is the first number? "))
  
  for symbol in operations:
    print(symbol)
    
  prompt = "continue"
  while prompt == "continue":
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))
    answer = operations[operation_symbol](num1, num2) 
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    num1 = answer
    prompt = input(f"Type 'continue' to continue calculating with {num1},\nor type 'reset' to start over: ")
  if prompt == "reset":
    calculator()

print("Welcome to the PyCalculator 1.0!")
calculator()
