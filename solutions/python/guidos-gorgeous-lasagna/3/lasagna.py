"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - minutes_in_oven
    



def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
    :param number_of_layers: nt  - number of layers in the lasagna
    :return: int - 'number_of_layers' multiplied by 2 is the total preparation time.    
    """
    return number_of_layers * 2
    


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):  
    """Calculate elapsed time in minutes.
    :param number_of_layers: nt  - number of layers in the lasagna
    :param elapsed_bake_time: int - number of minutes in the oven
    :return: int - elapsed time in minutes.    
    """    
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time


