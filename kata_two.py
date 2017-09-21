import pandas as pd
import numpy as np

if __name__ == '__main__':
    # First, read football.dat into a pandas dataframe
    # using any contiguous block of whitespace as the delimiter between columns.
    # Upon observing the data, I see that there is a column of hyphens between the 'for' and 'against'
    # columns, and this column has no header.  
    # To account for this, I set header=0 to discard the top row from the file,
    # thus allowing me to use my own set of column headers.
    # I specify the headers in the 'names' parameter.  
    table = pd.read_table('football.dat', delim_whitespace=True, header=0, \
                names=['number', 'name', 'p', 'w', 'l', 'd', 'for', 'dash', 'against', 'pts'])
    # convert the 'for' and 'against' series into numpy float arrays
    pts_agnst, pts_for = np.float_(table['against']), np.float_(table['for'])
    # create a numpy float array that contains the absolute values of the differences between 'against' and 'for'
    spread = abs(pts_agnst-pts_for)
    # Now, get the array index of the smallest spread value that is not == nan
    # Ignoring nan is necessary to account for the row of hyphens.  Another option would have been to 
    # skip this row in pd.read_table, but the approach I have used is more general.
    # numpy.nanargmin does exactly this, finding the index of a float array for the minimum value in
    # that array which is not nan
    answer_idx = np.nanargmin(spread)
    # Print the value in the name column for the row with the smallest spread
    print(table['name'][answer_idx])