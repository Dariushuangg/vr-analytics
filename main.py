from parse import parse
from clean import *
    
def analyze():
    """Entrance function for generating analytic results.
    """
    raw_data = parse()
    clean_all(raw_data)

analyze()