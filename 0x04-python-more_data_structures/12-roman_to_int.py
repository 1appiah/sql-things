#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
             "D": 500, "M": 1000, "IX": 9, "IV": 4, "XL": 40,
             "XC": 90, "CD": 400, "CM": 900}
    if roman_string in list(roman):
        return roman[roman_string]
    count = 0
    for i in range(0, len(roman_string)):
        if roman[roman_string[i]]:
            count = count + roman[roman_string[i]]
    return count
