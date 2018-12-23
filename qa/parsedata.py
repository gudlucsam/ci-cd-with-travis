import pandas as pd
from pathlib import Path

def readData(txt):
    # read txt and normalize
    data = pd.read_csv(txt, delimiter="\n", header=None)
    data[0] = data[0].apply(lambda x: str(x).lower())

    return data[0]


def generate_pairs():
    # create main dataframe
    col_names = ["Topic", "Question", "Answer"]
    df = pd.DataFrame(columns=col_names)
    # create pandas dataframes for files
    topics = readData("qa/dataset/Topics.txt")
    questions = readData("qa/dataset/Questions.txt")
    answers = readData("qa/dataset/Answers.txt")
    # create large data frame
    df["Topic"]=topics.apply(lambda x: str(x).lower())
    df["Question"]=questions.apply(lambda x: str(x).lower())
    df["Answer"]=answers.apply(lambda x: str(x).lower())

    return df

def convert_to_list(txt):
    """takes a text file and returns a list"""
    data = pd.read_csv(txt, delimiter="\n", header=None)
    return data.values.tolist()