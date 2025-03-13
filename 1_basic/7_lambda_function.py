a = "awanish"

first_letter = lambda x: x[0]

# print(first_letter(a))

# Find Number is positive neagtive or zero

number_1 = 0
number_2 = -1
number_3 = 3

type =  lambda x: "positive" if x>0 else "Negative" if x < 0  else "Zero"

# print(type(number_1))
# print(type(number_2))
# print(type(number_3))


# Check odd or even 
check_odd_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check_odd_even(number_1))

# add Two numbers 

perform_addition = lambda x, y: ("Additon is: ", x+y, "Mutiplication is: " ,x*y)

# print(perform_addition(89,89))


# Filter Function of lambda 

n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even)) 