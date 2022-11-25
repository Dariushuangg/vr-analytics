import os
import re
import pandas as pd
from collections import defaultdict

def d_dict():
    return defaultdict(d_dict)

def parse():
    """
    Parse all data files in directory and return a dictionary of 
    dictionary of array of data frames.
    """
    raw_data = d_dict()
    curr_path = os.getcwd()
    path = os.path.join(curr_path, 'data', 'raw')
    for filename in os.listdir(path):
        identifier = re.search(r"\d+-[a-zA-Z]", filename).group(0).split("-")
        env = identifier[0]
        question = identifier[1]
        raw_data[env][question][filename] = pd.read_csv(os.path.join(path, filename),
                                                        quotechar='"',
                                                        sep=',',
                                                        dtype=float)
    return raw_data

# raw_data = parse()
# df = raw_data["3"]["C"]['2022-11-25_00-22-23_3-C_I3T.txt']
# print(df.head(5))
