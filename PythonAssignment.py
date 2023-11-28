from helpers import *

if __name__  == "__main__":
    functions_dict = {
        "Type Conversions": [age_difference, float_to_integer, fahrenheit_to_celsius],
        "Operators": [addition, rectangle_area, celsius_to_fahrenheit, volume_of_sphere, odd_or_even],
        "Expressions": [find_average, find_leapyear, pythagorean, compound_interest, factorial],
        "Input-Output": [personalized_greeting, kilometers_to_miles, word_count, traingle_area],
        "Conditional Statements": [interger_type, vowel_consonant_check, find_max, determine_ticket_price, is_leap_year],
        "loops": [numbers_1_10, sum_up_to_limit, multiplication_table, sum_positive_numbers, fibonacci_series],
        "Control Flow": [grant_access, print_even_numbers, repeated_ask_for_numbers],
        "Lists and Tuples" : [create_color_list, sentence_to_words, replace_list_element, demonstrate_list_and_tuple,
                              sum_of_even_numbers, find_small_large_numbers, reverse_list, combine_lists, remove_duplicates,
                              filter_odd_numbers, sort_names, word_lengths, find_element_index, square_numbers, is_palindrome]
        }
    for category, functions in functions_dict.items():
        print(f"\n {category}: \n")
    # functions = functions_dict["Lists and Tuples"]
        for func in functions:
            if callable(func):
                func()
            else:
                print(f"Unknown function: {func}")
            print("\n")
