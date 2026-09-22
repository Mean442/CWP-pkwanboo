print("Enter the first number:")
a = int(input())
print("Enter the second number:")
b = int(input())
x = a * b

print(f"{a} x {b} = {x}")
if (x == 0) :
    print("The result is positive and negative.")
elif (x > 0) :
    print("The result is positive.")
else :
    print("The result is negative.")
