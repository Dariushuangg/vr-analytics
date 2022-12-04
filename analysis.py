from parse import parse
from clean import *
import math

def analyze():
    """Entrance function for generating analytic results.
    """
    raw_data = parse()
    cleaned_data = clean_all(raw_data)
    df = cleaned_data["3"]["C"]['2022-11-25_00-22-23_3-C_I3T.txt']
    conc = concentration(df)
    # print(conc.iloc[:10, :5])
    comp_t = completion_time(df)
    # print(comp_t)
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