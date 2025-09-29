#! /usr/bin/env python3

import pandas as pd

def read_file(inFile: str) -> pd.DataFrame:
    """
    Function to read the input txt file containing the data
    and put it in a pandas dataframe
    The txt file contains columns separated by 2 spaces
    """

    # read file and put content in dataframe
    df = pd.read_csv(inFile, 
                     sep=r"\s{2,}",
                     skip_blank_lines=True,
                     engine='python',
                     names=["h", "k", "l", 
                            "Energy", "idk5", "Intensity",
                            "idk7","idk8","idk9",
                            "idk10","idk11","idk12",
                            "idk13",])
    
    # force the data to be numbers
    # because they are in scientific notation with E
    # and they get interpreted as strings
    df = df.apply(pd.to_numeric, errors='coerce')

    # reduce dataframe to the columns of interest
    df = df[["h", "k", "l", "Energy", "Intensity"]]

    # remove NaN values from dataframe
    # drop rows which contain missing values
    df = df.dropna(axis=0) 
    
    # check for NaN values
    if(df.isna().any().any()): # returns True if there is at least 
                                # one NaN value anywhere in the df, 
                                # and False if there are no NaN 
                                # values in the entire DataFrame.
        raise ValueError("The dataframe contains NaN values. " \
                         "Please check the data.")
    
    print(df.columns)
    print(df.shape)

    return df
