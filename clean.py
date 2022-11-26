import pandas as pd    
import math

def extract_head_pose(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    Take a dataframe representation of file and extract the head pose
    data, since we will discretized the data.
    """
    pass

def clean(df: pd.DataFrame) -> None:
    """
    Clean one data file.
    """
    # Extract head pose data that needs to be frame-continuous
    extract_head_pose(df)
    
    # Drop the first row with empty values and the last few head pose rows
    df.drop([0], inplace=True)
    df.drop(df.columns[-6:], axis=1, inplace=True)
    
    # Aggregate all frames in one second together and convert to relative time
    df["time"] = df["time"].map(lambda x : math.floor(x))
    df["time"] = df["time"].map(lambda x : x - df["time"][1]) 
    df = df.groupby(df["time"]).aggregate({col:"last" for col in df.columns})
    return df
    
    
def clean_all(raw_data):
    """
    Take in raw data, produce cleaned data
    """
    for env in raw_data.keys():
        for question in raw_data[env].keys():
            for file in raw_data[env][question].keys():
                raw_data[env][question][file] = clean(raw_data[env][question][file])
    return raw_data[env][question][file]