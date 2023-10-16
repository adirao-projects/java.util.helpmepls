number_1 = int(input("Input your first number: "))
number_2 = int(input("Input your second number: "))
operation = int(input("What type of operation do you want to do - Add(1), Subtract(2), Multiply(3), or Divide(4)?: "))

if operation == 1:
    answer = number_1 + number_2

elif operation == 2:
    answer = number_1 - number_2

elif operation == 3:
    answer = number_1 * number_2

elif operation == 4:
    answer = number_1 / number_2

else:
    print("Invalid operation")

print("The answer is: " + str(answer))