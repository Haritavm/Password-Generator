# Password-Generator
The file, random_pass.py, is part of a project named Password Generator. This file includes functionality for generating random passwords.

Key Components:
1-Imports:
    > random: Used for generating random choices.
    > string: Provides access to string constants like ascii_letters, digits, and punctuation.
2-Functions:
      > generate_password(length: int=10): Generates a random password of a specified length.
    Parameters:
      > length (int): The length of the password to be generated. Default is 10.
    Returns:
      > A string representing the generated password.
    Process:
      > Initializes an empty list password.
      > Loops through the specified length, appending a random character (from letters, digits, and punctuation) to the list.
      > Joins the list into a string and returns it.
3-Example Usage:
      Generates a password of length 5 and prints it.
