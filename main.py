import json
import os
import sys
import argparse
import numpy as np

from src.naive_bayes import NaiveBayesClassifier
from src.accuracy_methods import get_accuracy_method

def train_and_eval(config, train_set, test_set):
    model=NaiveBayesClassifier(lmd=config["lambda"])

    test_y_true=[]
    test_x=[]
    for test_case in test_set:
        test_y_true.append(test_case["label"])
        test_x.append(test_case["input"])
    test_y_true=np.array(test_y_true)
    if "training_rate" in config:
        train_set=train_set[:int(config["training_rate"]*len(train_set))]
    model.fit(train_set)
    y_pred=model.predict(test_x)

    result={}
    for method_name in config["accuracy_method"]:
        method=get_accuracy_method(method_name)
        result[method_name]=round(method(test_y_true,y_pred),6)
    return result

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Config file path")

    args=parser.parse_args()
    
    config=json.load(open(args.config,"r"))

    train_set=[]
    for train_file in config["train_file"]:
        temp=json.load(open(train_file,"r"))
        train_set.extend(temp)
    test_set=[]
    for test_file in config["test_file"]:
        temp=json.load(open(test_file,"r"))
        test_set.extend(temp)

    result=train_and_eval(config=config, train_set=train_set,test_set=test_set)
    print(result)