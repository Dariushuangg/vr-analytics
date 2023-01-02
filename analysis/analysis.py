from parse import parse
from clean import *
from conc_percent import *
from conc_switch import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def corr_focus_quiz(focus_time: list, quiz_score: list):
    a = np.corrcoef(focus_time, quiz_score)[0, 1]
    pass

def concentration_percentage_analysis(cleaned_data):
    conc = pd.DataFrame()
    res = pd.DataFrame()
    for env in ["1", "2", "3"]:
        for task in ["C", "P", "F"]:
            for person in cleaned_data[env][task].keys(): # for each environment-task combination, do:
                df = cleaned_data[env][task][person]
                conc[person] = concentration(df).apply(lambda row: calculate_concentration_percent(row), axis = 1)
        res["Classroom " + env] = conc.mean(axis=1)
        conc = pd.DataFrame()
    
    res.reset_index(inplace=True) # Make Duration accessible by column name for plot() to use
    res.plot(x="Duration",
              y=['Classroom 1', 'Classroom 2', 'Classroom 3'],
              kind='line',
              xlabel='Time Period (3 seconds / Time Period)',
              ylabel="Average Concentration Percentage")	
    plt.show()

def concentration_switches_analysis(cleaned_data):
    switches = list()
    res = dict()
    for env in ["1", "2", "3"]:
        for task in ["C", "P", "F"]:
            for person in cleaned_data[env][task].keys():
                df = cleaned_data[env][task][person]
                switch = calculate_concentration_switches(
                    concentration(df).apply(lambda row: is_looking_at(row), axis = 1).tolist()
                    )
                switches.append(switch)
        res["Classroom " + env] = sum(switches) / (len(switches) * 3)
        switches = list()
    
    plt.bar(res.keys(), res.values())
    plt.ylim([0,1])
    for key in res.keys(): # add label to plot
        plt.annotate(str(round(res[key], 3)), xy=(key, round(res[key], 3)), ha='center', va='bottom')
    plt.title("Average Focus Switches / Second")
    plt.show()

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

def analyze():
    """
    Entrance function for generating analytic results.
    """
    raw_data = parse()
    cleaned_data = clean_all(raw_data)    
    # concentration analysis
    concentration_percentage_analysis(cleaned_data)
    
    # concentration switches analysis
    concentration_switches_analysis(cleaned_data)
    pass   

def completion_time(df: pd.DataFrame) -> int:
    """
    Analyze the time spent on completing the task
    Args:
        file (pd.DataFrame): cleaned dataframe representing a file from experiment
    """
    #return df.iloc[-1, 0] 
    return -1 # deprecated

analyze()
# focus_time = [0.31, 0.33, 0.21]
# quiz_score = [0.31, 0.33, 0.21]
# corr_focus_quiz(focus_time, quiz_score)