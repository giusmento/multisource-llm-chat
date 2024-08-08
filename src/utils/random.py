import random
import string


def random_string(length):
    """
       Generates a random alphanumeric string of specified length.

       Args:
           length (int): The desired length of the generated string.

       Returns:
           str: A random alphanumeric string of the specified length.
       """
    all_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(all_characters) for _ in range(length))