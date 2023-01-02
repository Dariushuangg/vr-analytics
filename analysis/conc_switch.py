from parse import parse
from clean import *
import pandas as pd
import math

def calculate_concentration_switches(ilt: list):
    """Count the percentage of time period in which a switch of focus occurs

    Args:
        df: A list representing where the user is looking at during each time period
    """
    count = 0
    for i in range(1, len(ilt)):
        count = count + 1 if ilt[i] - ilt[i - 1] != 0 else count
    return count / len(ilt)

def is_looking_at(row):
    """Determine where the user is focusing on during a period of time

    Args:
        row (_type_):One row in the df output by concentration
    """
    r = [row["Molecule Frames"], row["UI Frames"], row["Environment Frames"]] # ugly, but works
    return r.index(max(r))
