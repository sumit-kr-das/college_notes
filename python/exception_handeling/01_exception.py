# Basic three types of errors:
# a. compile time errors (syntax error)
# b. logical error (2+3=4, code bugs)
# c. run time error (compiled by we provide wrong input, mistake is responsible)

a = input('Enter a Number: ')
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(i)} X {a} = {int(a)*i}")
except Exception as e:
    print(e)

print("Code End... :)")