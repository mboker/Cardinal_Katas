import pandas as pd
from kata_three_shared import *

if __name__ == '__main__':
    # First, read football.dat into a pandas dataframe
    # using any contiguous block of whitespace as the delimiter between columns.
    # Upon observing the data, I see that there is a column of hyphens between the 'for' and 'against'
    # columns, and this column has no header.  
    # To account for this, I set header=0 to discard the top row from the file,
    # thus allowing me to use my own set of column headers.
    # I specify the headers in the 'names' parameter.  
    table = pd.read_table('../football.dat', delim_whitespace=True, header=0, \
                names=['number', 'name', 'p', 'w', 'l', 'd', 'for', 'dash', 'against', 'pts'])
    print(get_answer('against', 'for', table, 'name'))