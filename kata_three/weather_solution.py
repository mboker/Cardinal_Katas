import pandas as pd
from kata_three_shared import *

# From inspecting the data, I see that one MxT cell and one MnT cell have trailing asterisks.
# These will need to be stripped so that the values can be converted to doubles.
# To accomplish this, rstrip_astrsk will be passed as a converter for each of MxT and MnT in the
# call to pandas.read_table.  This will strip the asterisks from the input while loading it into a dataframe
def rstrip_astrsk(str_val):
    return str_val.rstrip('*')

if __name__ == '__main__':
    # Read weather.dat into a pandas dataframe, stripping trailing asterisks from the MxT and MnT column values, 
    # and using any contiguous block of whitespace as the delimiter between columns
    table = pd.read_table('../weather.dat', converters={'MxT': rstrip_astrsk, 'MnT': rstrip_astrsk}, delim_whitespace=True)
    print(get_answer('MxT', 'MnT', table, 'Dy'))