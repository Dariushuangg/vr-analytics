import os
# import re

# m = re.search(r"\d+-[a-zA-Z]", "2022-11-25_00-19-27_2-P_I3T").group(0)
# print(m)

# path = os.getcwd()
# print(os.path.join(path, 'data', 'raw'))
curr_path = os.getcwd()
path = os.path.join(curr_path, 'data', 'raw')
for filename in os.listdir(path):
    print(type(filename))
