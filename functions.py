"""
1.  Write a program that lists the numbers
    from 0-10 on separate lines
"""
for i in range(11):
    print(i)


"""
2.  Write a program that counts down from
   100 by 5's
"""
for i in range(100,0,-5):
    print(i)


"""
3.  Write a function called Triple(x):
This Function should take the value x and
Return 3 times that number. Call the function
and print the result to the screen for x = 20
"""
def triple(x):
    x = x * 3
    return x
print(triple(20))


"""
4.  Write a program that will ask the user
to input a number, triple it and  display
the result.  You will NEED print statements
AND you may use your function above.
"""
def triple():
    print("put a number you want tripled")
    x = int(input())
    x = x * 3
    return x
print(triple())


"""
5.  Write a program that will return the result
for the equation on the board:  Run this function
and print the results for the inputs:
(-3, -2, -1, 0, 1, 2, 3)
"""








