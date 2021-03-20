# This is what we learned last week.
# Oh, one more new thing.
# Any line that starts with a "#" (hash) symbol is a comment
# Python ignores comments. Comments are for humans.

# This is how to print a string (text) to the screen:
print("Hi there!")

# "hi there" is a string.
# Inside a string, you can write anything you want. You can write Korean too:
print("안녕~")

# Every string has quotes on both ends. You can use a double quote: "
# Or a single quote: '
print('Single quote sentence')
print("Double quote sentence")

# You can give a string a name:
my_name = "Jeroen"

# This is called a variable.
# The name of the variable is "my_name" and the value is "Jeroen".
# Variable names cannot have spaces. That is why I used a _ (underscore)

# You can use the variable just like the string itself:
print(my_name)

# You can use a variable inside another string like this, with an f before the quote:
print(f"Hi, my name is {my_name}")

# You can also stick strings together using + (plus):
print("Hi, my name is " + my_name)

# You can even multiply a string if you want to, using * (asterisk):
print("Mine!" * 10)

# You can do things with strings like making them all upper case letters:
print("Nice to meet you".upper())

# You can even replace parts of a string with something else
print("I like eating apples, pears, and oranges".replace("pears", "grapes"))

# You can ask a user for a string to use in your program:
print("Please tell me your name")
name = input()
print(f"Hi {name}!")