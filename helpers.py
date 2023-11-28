import math
import random


# Type Conversions:

# 1 : Write a Python function that takes a user's input for their age as a string. Convert the string to an 
# integer and print a message indicating how many years they need to reach 100 years old.
def age_difference():
    user_age_str = input("Enter your age: ")
    try:
        
        user_age = int(user_age_str)
        years_to_100 = 100 - user_age
        if years_to_100 > 0:
            print(f"You will reach 100 years old in {years_to_100} years.")
        
        elif years_to_100 == 0:
            print("Congratulations! You are already 100 years old.")
        else:
            print("You are already older than 100 years.")

    except ValueError:
        print("Invalid Input. Please enter a valid age.")

# 2 : Create a Python function that converts a floating-point number to an integer. Round the floating-point number before converting it.
def float_to_integer():
    try:
        float_number = float(input("Enter your floating-point number: "))
        rounded_number = round(float_number)
        integer_number = int(rounded_number)
        
        print(f"The rounded is: {rounded_number}")
        print(f"The rounded and converted integer is: {integer_number}")

    except ValueError:
        print("Invalid Input. Please enter a valid floating-point number.")

# 3 : Write a Python function that converts a temperature in Fahrenheit to Celsius. Take the Fahrenheit
# value as input, convert it to a float, and then perform the conversion. 
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Enter your temperature in Fahrenheit(F): "))
        celsius = (fahrenheit-32) * 5/9
        
        print(f"The {fahrenheit}F is equals into {celsius: .2f}C")

    except ValueError:
        print("Invalid Input. Please enter a valid temperature.")

# Operators:

# 1 : Write a Python function that takes two numbers as input and calculates their sum using the
# addition operator.
def addition():
    
    addend_1 = float(input("Enter first addend value:"))
    addend_2 = float(input("Enter second addend value:"))
    try: 
        sum = addend_1 + addend_2
        print(f"The sum of {addend_1} and {addend_2} is: {sum}")
    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")

# 2 : Create a Python function that calculates the area of a rectangle. Take the length and width as
# input and use the multiplication operator to perform the calculation.
def rectangle_area():
    
    length= float(input("Enter length value:"))
    width = float(input("Enter width value:"))
    try: 
        area = length*width
        print(f"The sum of {length} and {width} is: {area}")
    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")


# 3 : Write a Python function that converts temperature from Celsius to Fahrenheit. Take the Celsius
# value as input and use the appropriate formula involving multiplication and addition operators.
def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter your temperature in celsius(C): "))
        fahrenheit = (celsius*9/5) + 32
        
        print(f"The {celsius: .2f}C is equals into {fahrenheit}F")

    except ValueError:
        print("Invalid Input. Please enter a valid temperature.")

# 4 : Create a function that calculates the volume of a sphere. Take the radius as input and use the
# power operator for exponentiation.
def volume_of_sphere():
    try:
        radius = float(input("Enter radius value: "))
        volume = (4/3*math.pi) * (radius**3)
        
        print(f"The volume of the sphere with radius {radius} is {volume: .3f}")
    except ValueError:
        print("Invalid Input. Please enter a valid temperature.")

# 5 : Write a Python function to determine whether a given number is even or odd using the modulo
# operator. 
def odd_or_even():
    try:
        number = int(input("Enter an integer: "))
        if number%2 == 0:
            print(f"Number {number} is Even")
        else:
            print(f"Number {number} is Odd")
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

# Expressions:

# 1 : Write a Python function that calculates the average of three numbers. Use expressions to perform
# the addition and division.
def find_average():
    try:
        num_1 = float(input("Enter first value: "))
        num_2 = float(input("Enter second value: "))
        num_3 = float(input("Enter third value: "))

        avg_num = (num_1+num_2+num_3) / 3

        print(f'The average of {num_1}, {num_2}, {num_3} is {avg_num}')

    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")   


# 2 : Create a function that checks if a given year is a leap year. Use expressions to set the conditions
# for leap years (divisible by 4, but not by 100 unless also divisible by 400).
def find_leapyear():
    try:
        year = int(input("Enter year:"))
        if  year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            print(f"The {year} is a Leap year")
        else:
            print(f"The {year} is not a Leap year")

    except ValueError:
        print("Invalid Input. Please enter a valid year.")   

# 3 : Write a Python function to calculate the hypotenuse of a right triangle using the Pythagorean
# theorem. Take the lengths of the two shorter sides as input.
def pythagorean():
    try:
        a = float(input("Enter first value: "))
        b = float(input("Enter second value: "))

        c = math.sqrt(a**2 + b**2)
        print(f"The hypotenuse of {a}, {b} is {c: .2f}")

    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")   


# 4 : Create a function that calculates the compound interest. Take principal amount, rate, and time as
# input. Use expressions to calculate compound interest.
def compound_interest():
    try:
        p = float(input("Enter Principal Amount: "))
        r = float(input("Enter Interest Rate: "))
        t = float(input("Enter the length if time you invest: "))

        accumulated_amount = p * (1+r) ** t
        print(f"The Compound Interest is {accumulated_amount}")
    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")       

# 5 : Write a Python function that calculates the factorial of a number. Use expressions to perform the
# multiplication.
def factorial():
    """ 
    This factorial function
    """
    try:
        num = int(input("Enter an Integer: "))
        fact = (lambda x: x * fact(x-1) if x > 0 else 1)
        fact_value = fact(5)
        print(f"The Factorial of {num}! is {fact_value}")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")

# Input-Output Operations:

# 1 : Write a Python function that takes a user's name as input and prints a personalized greeting.
def personalized_greeting():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to our function.")

# 2 : Create a function that converts kilometers to miles. Take the distance in kilometers as input and
# perform the conversion using appropriate expressions.
def kilometers_to_miles():
    try:
        distance_km = float(input("Enter distance in kilmeters: "))
        distance_miles = distance_km*0.621371
        print(f"{distance_km: .2f}km is equals to {distance_miles: .2f}mi")
    
    except ValueError:
        print("Invalid Input. Please enter a valid distance.")

# 3 : Write a Python function that reads a sentence from the user and counts the number of words.
# Assume that words are separated by spaces.
def word_count():
    sentence = input("Enter your sentence as comma separated words: ")
    count = len(sentence.split(','))
    print(f"Word count of you sentence: {count}")

# 4 : Create a function that takes a user's age as input and determines whether they are eligible to vote
# (18 years or older). Output an appropriate message.
def eligiblity_to_vote():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print(f"Hooray! You are eligible to vote.")
        else:
            print(f"Sorry! you are not eligible for vote")
    except ValueError:
        print("Invalid Input. Please enter a valid age")

# 5 : Write a Python function that calculates the area of a triangle using the base and height entered
# by the user. 
def traingle_area():
    try:
        base = float(input("Enter triangle base value:"))
        height = float(input("Enter triangle height value:"))
        area = (base*height) / 2

        print(f"Area of the triangle with base {base: .2f} and {height: .2f} is {area: .2f}")
    except ValueError:
        print("Invalid Input. Please enter a valid values")

# Conditional Statements (if, else, elif):

# 1 : Write a Python function that takes an integer as input and prints whether it is positive, negative,
# or zero.
def interger_type():
    try:
        num = int(input("Enter an integer:"))
        if  num > 0:
            print(f"The {num} is positive")
        elif num < -1:
            print(f"The {num} is negative")
        else:
            print(f"This is zero")

    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

# 2 : Create a function that checks whether a character entered by the user is a vowel or a consonant.
def vowel_consonant_check():
    # letters = list(string.ascii_lowercase)
    vowels = ['a', 'e', 'i', 'o', 'u']
    # consonant = [con for con in letters if con not in vowels]

    character = input("Enter an character to check whether it is an vowel or consontant: ")
    if character.isalpha() and len(character)==1:
        result = 'vowel' if character.lower() in vowels else 'consonant'
        print(f"The character {character} is a {result}")
    else:
        print("Invalid Input. Please enter a valid single character.")
        
# 3 : Write a Python function to find the maximum of three numbers. Take the numbers as input and
# use conditional statements to compare and determine the maximum.
def find_max():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        if num1 >= num2 and num1 >= num3:
            result = num1
        elif num2 >= num1 and num2 >= num3:
            result = num2
        else:
            result = num3
        
        print(f"The maximum of {num1}, {num2}, and {num3} is {result}")
    
    except ValueError:
        print("Invalid Input. Please enter a valid numbers.")

# 4 : Create a function that determines the ticket price based on the age of a person. If the age is
# under 12, the ticket is free. If the age is between 12 and 18, the ticket is discounted. Otherwise, the
# ticket is full price.
def determine_ticket_price():
    try:
        age = int(input("Enter your age: "))
        if age < 12:
            price = "Free"
        elif 12 <= age <=18:
            price = "Discounted"
        else:
            price = "Full Price"

        print(f"Your ticket is {price}")   
    except ValueError:
        print("Invalid Input. Please enter a valid age.")
    
# 5 : Write a Python function that takes a year as input and prints whether it's a leap year or not using
# conditional statements.
def is_leap_year():
    try:
        year = int(input("Enter year:"))
        if  year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            print(f"The {year} is a Leap year")
        else:
            print(f"The {year} is not a Leap year")

    except ValueError:
        print("Invalid Input. Please enter a valid year.")  

# Loops:

# 1 : Write a Python function that uses a for loop to print the numbers from 1 to 10.
def numbers_1_10():
    for idx in range(1, 11):
        print(idx)

# 2 : Create a function that uses a while loop to calculate the sum of numbers from 1 to a userspecified limit.
def sum_up_to_limit():
    try:
        limit = int(input("Enter a limit: "))
        sum = 0
        curr_number = 1
        while curr_number <= limit:
            sum +=curr_number
            curr_number +=1
        print(f"The sum of numbers from 1 to {limit} is: {sum}")
    
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

# 3 : Write a Python function that prints the multiplication table of a number entered by the user,
# using a for loop.
def multiplication_table():
    try:
        number = int(input("Enter a Integer: "))
        print(f"Multiplication table for {number}")
        for idx in range(1,11):
            value = number * idx
            print(f"{number} x {idx} = {value}")

    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

# 4 : Create a function that uses a while loop to keep asking the user for a number until they enter a
# negative number. Calculate and print the sum of all positive numbers entered.
def sum_positive_numbers():
    sum = 0
    while True:
        number = float(input("Enter a number (negative to stop): "))
        
        if number < 0:
            break  
        else:
            sum += number

    print(f"The sum of positive numbers entered is: {sum}")

# 5 : Write a Python function that uses a for loop to print the Fibonacci series up to the nth term,
# where n is taken as input from the user.
def fibonacci_series():
    try: 
        number = int(input("Enter a number: "))
        sequence = []
        if number <=0:
            print("Please enter a positive number")
        elif number == 1:
            sequence = [0]
        elif number == 2:
            sequence = [0, 1]
        else:
            sequence = [0, 1]
            for idx in range(2, number):
                next = sequence[idx - 1] + sequence[idx - 2]
                sequence.append(next)
        print(f"Fibonacci series up to the {number}th term:")
        for idx in sequence:
            print(idx)

    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

# Control Flow Keywords (break, continue, pass):

# 1 : Create a Python function that takes user input for a password. If the password matches
# "secret123", print "Access granted." If the password is incorrect, print "Access denied."
def grant_access():
    curr_pwd = input("Please enter password: \n")
    pwd = "secret123"
    while(pwd != curr_pwd):

        print("access denied")
        pass
        curr_pwd = input("Please enter password: \n")
        
    print ("access granted")

# 2 : Write a function that prints all even numbers from 1 to 20 using a for loop and the continue
# keyword.
def print_even_numbers():
    print(f"Printing even number from 1 to 20:")
    for idx in range(1,21):
        if idx%2 == 0:
            print(idx)
        else:
            continue
# 3 : Create a function using a while loop to repeatedly ask the user for a number. If the user enters -1,
# exit the loop using the break keyword. 
def repeated_ask_for_numbers():
    while True:
        try:
            number = int(input("Please enter a number (-1 to exit): \n"))
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")
        if number == -1:
            break
        print(f"You entered: {number}")

# Lists and Tuples:

# 1 : Write a Python function that creates a list of your favorite colors. Print each color using a loop.
def create_color_list():
    favorite_colors = list(('purple', 'green', 'teal', 'yellow'))
    print(f"Printing my favorite colors:")
    for item in favorite_colors:
        print(item)

# 2 : Create a function that takes a sentence as input and stores each word in a list. Print the list of
# words.
def sentence_to_words():
    sentence = input("Enter a sentence with space: ")
    words = sentence.split(' ')
    print("Printing words from given sentence: ")
    for word in words:
        print(word)

# 3 : Write a Python function that uses indexing to replace the second element of a list with a new
# value.
def replace_list_element():
    elements = [1, 6, 7, 9, 3, 2]
    value = input("Enter new integer value: ")
    try:
        elements[1] = int(value)
        print(f"Updated list: {elements}")
    except ValueError:
        print("List is not updated due to invalid input. Please enter a valid integer.")
    

# 4 : Create a function that demonstrates the difference between a list and a tuple. Define a list and a
# tuple with some elements, then try modifying elements and observe the results.
def demonstrate_list_and_tuple():
    my_list = [1, 6, 7, 9, 3, 2]
    my_tuple = (1, 6, 7, 9, 3, 2)

    print("Modifying list elements: ")
    my_list[3] = "22"
    print(f"Modified list: {my_list}")

    try:
        print("Modifying tuple elements: ")
        my_tuple[3] = "22"
        print(f"Modified tuple: {my_tuple}")
    except TypeError as e:
        print(f"Error: {e}")
        print(f"Tuple remains unchanged: {my_tuple}")

# 5 : Write a Python function that takes a list of numbers as input and calculates the sum of all even
# numbers using a loop and the sum() function.
def sum_of_even_numbers():
    numbers = input("Enter your list of numbers as comma separated integers: ")
    elements = numbers.split(',')
    try:
        numbers = [int(element) for element in elements]
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(f"The sum of even numbers in the list is: {sum(even_numbers)}")

# 6 : Write a Python function that creates a list of integers and prints the smallest and largest values in
# the list.
def find_small_large_numbers():
    numbers = input("Enter your list of numbers as comma separated integers: ")
    elements = numbers.split(',')
    try:
        numbers = [int(element.strip()) for element in elements]
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

    print(f"The smallest number of the list is {numbers[0]} \nThe largest number of the list is {numbers[-1]}")

""" noted for my refernce
def find_small_large_numbers():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"The smallest number of the list is {min(numbers)}\nThe largest number of the list is {max(numbers)}")"""

# 7 : Create a function that takes a list of strings as input and prints each string in reverse order.
def reverse_list():
    words_with_comma = input("Enter your strings as comma separated words: ")
    words = words_with_comma.split(',')
    words = [word.strip() for word in words]
    # reverse_words = words[::-1]
    words.reverse()
    print('Printing entered strings in reverse order:')
    for word in words:
        print(word)

# 8 : Write a Python function that combines two lists into a single list, where the elements alternate
# from the two input lists.
def combine_lists():
    list_1 = input("Enter your list of numbers as comma separated integers (list 1): ")
    list_2 = input("Enter your list of numbers as comma separated integers (list 2): ")
    list_1 = list_1.split(',')
    list_2 = list_2.split(',')
    list_1 = [item.strip() for item in list_1]
    list_2 = [item.strip() for item in list_2]

    combined_list = list()
    min_length = min(len(list_1), len(list_2))

    for idx in range(min_length):
        combined_list.append(list_1[idx])
        combined_list.append(list_2[idx])
    
    combined_list.extend(list_1[min_length:])
    combined_list.extend(list_2[min_length:])

    print(f"Combined list with alternating elements: {combined_list}")

# 9 : Create a function that removes all duplicates from a list while preserving the order of the
# remaining elements.
def remove_duplicates():
    my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    unique_elements = list()
    for item in my_list:
        if item not in unique_elements:
            unique_elements.append(item)
    print(f"List with duplicates removed: {unique_elements}")
    print(f"List with duplicates removed (with set): {list(set(my_list))}")

# 10 : Write a Python function that takes a list of numbers as input and prints a new list containing only
# the odd numbers.
def filter_odd_numbers():
    numbers = input("Enter your list of numbers as comma separated integers: ")
    elements = numbers.split(',')
    try:
        numbers = [int(element.strip()) for element in elements]
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    odd_numbers = [num for num in numbers if num % 2 != 0]

    print(f"Odd numbers in the list: {odd_numbers}")

# 11 : Create a function that takes a list of names and sorts them in alphabetical order. Print the sorted
# list.
def sort_names():
    name_list = ["John", "Alice", "Bob", "Eve", "Charlie"]
    print("Original List of Names:", name_list)
    print(f"Sorted List {sorted(name_list)}")

# 12 : Write a Python function that takes a list of words as input and creates a new list containing the
# lengths of the words.
def word_lengths():
    word_list = ["apple", "banana", "cherry", "date", "fig"]
    lengths = [len(word) for word in word_list]

    print("Original List of Words:", word_list)
    print("List of Word Lengths:", lengths)

# 13 : Create a function that finds the index of the first occurrence of a given element in a list. If the
# element is not found, print a message indicating so.
def find_element_index():
    my_list = [1, 2, 3, 4, 5, 6]
    try:
        element = int(input("Enter a number: "))
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    try:
        index = my_list.index(element)
        print(f"The index of {element} is {index}")
    except ValueError:
        print(f"The element '{element}' was not found in the list.")

# 14 : Write a Python function that takes a list of integers and returns a new list with the squares of the
# original numbers.
def square_numbers():
    numbers = input("Enter your list of numbers as comma separated integers: ")
    elements = numbers.split(',')
    try:
        numbers = [int(element.strip()) for element in elements]
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    squared_list = [num ** 2 for num in numbers]
    print("List of Squared Numbers:", squared_list)

# 15 : Create a function that accepts a list of numbers and checks if it's a palindrome (reads the same
# backward as forward).
def is_palindrome():
    # number_list = [1, 2, 3, 4, 3, 2, 1]
    numbers = input("Enter your list of numbers as comma separated integers: ")
    elements = numbers.split(',')
    try:
        numbers = [int(element.strip()) for element in elements]
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
    num_str = ''.join(map(str, numbers))
    if num_str == num_str[::-1]:
        print("The list a palindrome")
    else:
        print("The list is not a palindrome")
