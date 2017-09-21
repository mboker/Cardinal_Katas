import numpy as np

# This is a bit of a reach for refactoring, but I did see that, once the tables were built, the rest of the code
# for each solution was almost identical, or at least could be.  Adding the use of absolute value
# and nanargmin to the solution for weather has no impact on its output, so there is no problem with using
# them in a shared method.
def get_answer(col_one_name, col_two_name, table, answer_col):
    # Convert the col_one_name and col_two_name pandas series from the dataframe into numpy float arrays
    col_one, col_two = np.float_(table[col_one_name]), np.float_(table[col_two_name])
    # perform vector subtraction on the float arrays to get an array of the differences.  
    # Take the absolute values of these differences
    spread = abs(col_one - col_two)
    # Get the index for the smallest value in the spread array, ignoring nan values
    answer_idx = np.nanargmin(spread)
    return table[answer_col][answer_idx]