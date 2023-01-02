from parse import parse
from clean import *
import pandas as pd
import math

def calculate_concentration_percent(row):
    """Calculate the percentage of time focus on content in one duration.
    Args:
        row: One row in the df output by concentration
    """
    concentrated_frame = row["Molecule Frames"] + row["UI Frames"]
    total_frame = row["Total Frame"]
    
    if concentrated_frame > total_frame:
        concentrated_frame = total_frame # fix rounding error
    if total_frame == 0:
        return 0 # display 0 rows
        
    percentage = concentrated_frame / total_frame
    return percentage
