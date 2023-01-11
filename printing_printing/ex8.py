# declare a formatter variable with 4 dynamic values
formatter = "{} {} {} {}"

# printing the formatter variable with 1 2 3 4
print(formatter.format(1,2,3,4))

# print some string
print(formatter.format("one", "two", "three", "four"))

# print boolean values
print(formatter.format(True, False, False, True))

# print the formatter value 4 times
print(formatter.format(formatter, formatter, formatter, formatter))

# print some long string
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
