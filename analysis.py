from parse import parse
from clean import *
import pandas as pd
import matplotlib.pyplot as plt
import math

def concentration_percent(row):
    """Calculate the percentage of time focus on content in one duration.
    Args:
        row: One row in the df output by concentration
    """
    concentrated_frame = row["Molecule Frames"] + row["UI Frames"]
    total_frame = row["Total Frame"]
    if concentrated_frame > total_frame:
        concentrated_frame = total_frame
    percentage = concentrated_frame / total_frame
    return percentage

def concentration_analysis(cleaned_data):
    conc = pd.DataFrame()
    res = pd.DataFrame()
    for env in ["1", "2", "3"]:
        for person in cleaned_data[env]["C"].keys():
            df = cleaned_data[env]["C"][person]
            conc[person] = concentration(df).apply(lambda row: concentration_percent(row), axis = 1)
        res["Average Concentration Percentage " + env] = conc.mean(axis=1)
        conc = pd.DataFrame()
    
    res.reset_index(inplace=True) # Make Duration accessible by column name for plot() to use
    res.plot(x="Duration",
              y=['Average Concentration Percentage 1', 'Average Concentration Percentage 2', 'Average Concentration Percentage 3'],
              kind='line',
              xlabel='Duration (3 seconds / duration)',
              ylabel="Average Concentration Percentage")	
    plt.show()

def analyze():
    """Entrance function for generating analytic results.
    """
    raw_data = parse()
    cleaned_data = clean_all(raw_data)    
    # Concentration Analysis
    concentration_analysis(cleaned_data)
    
    pass    

def concentration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze the test subject's level of concentration throughout time. Calculated
    as focused and unfocused frame divided by total frame passed during a time frame.
    Args:
        df (pd.DataFrame): cleaned dataframe representing a file from experiment
    """
    temp = df
    temp["Duration"] = df["time"].map(lambda x : math.floor(x / 3))
    temp = temp.groupby(df["Duration"]).aggregate({col:"last" for col in temp.columns}).diff()
    temp = temp.dropna(axis=0)
    temp = temp.drop(columns="time")
    
    # Note: Duration is the key of the constructed conc_df
    conc_df = pd.DataFrame({
        "Molecule Frames": temp["confusor_view"] + temp["isomer_view"],
        "UI Frames": temp["UI_view"],
        "Environment Frames": temp["total_frame"] - temp["confusor_view"] - temp["isomer_view"] - temp["UI_view"],
        "Total Frame": temp["total_frame"]})
    
    # This map is necessary because when we are simultaneously looking at two objects
    # in one frame, it's possible to have negative Environment Frames; In this situation,
    # we should consider Environment Frames = 0, namely the subject is fully concentrated.
    conc_df = conc_df.applymap(lambda x: max(0, x)) 
    
    return conc_df


def completion_time(df: pd.DataFrame) -> int:
    """
    Analyze the time spent on completing the task
    Args:
        file (pd.DataFrame): cleaned dataframe representing a file from experiment
    """
    return df.iloc[-1, 0]

analyze()