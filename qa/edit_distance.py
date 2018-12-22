import pandas as pd
from parsedata import generate_pairs
from nltk.metrics import edit_distance
import argparse



def edit_dis(question):
    """Retrieves the similar question in the test data with a users question"""

    # retrive dataframe
    df = generate_pairs()

    # convert to list for modeling
    x = df.Question.tolist()
    y = df.Answer.tolist()

    x_index = -1  # initialize index for tracking index of similar question
    _val = 1000
    for i in range(len(x)):
        # calculate edit distance
        val_dis = edit_distance(question.split(), x[i].split())
        if(val_dis < _val):
            _val = val_dis
            x_index = i
    return y[x_index]
