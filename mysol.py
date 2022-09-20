x=int(input("enter a number between 1 to 100"))
if x%3==0:
    print("fizz")
elif x%5==0:
    print("buzz")
elif x%3==0 and x%5==0:
    print("fizzBuzz")
else:
    print(x)

