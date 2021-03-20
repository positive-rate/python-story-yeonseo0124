# Check the file "class_1.py" to read about what we learned last week.

# Today we will first learn about input.
# Input means asking the user of your program to write something.
# Your program can then use what they write.
# You have to save the input in a variable.

# If you run this program, it will stop here, until the user writes something:
user_name = input()

# That is not very helpful. The user doesn't know what to write.
# Delete the code above, and let's tell the user what we want first:

print("What is your name?")

# Now we can ask for input:
user_name = input()

# We can then use the input, to write something new:
print(f"Hi {user_name}, nice to meet you!")

