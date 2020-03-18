import json
import os
import sys
import argparse
import numpy as np

from main import train_and_eval


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Config file path")
    parser.add_argument("--print-all-results", help="Print all results when each group is test set.", action="store_true")

    args=parser.parse_args()
    print_all=args.print_all_results
    
    config=json.load(open(args.config,"r"))
    data_set,k=[],0
    while True:
        file_name=os.path.join(config["data_path"],"data_{}.json".format(k))
        if not os.path.exists(file_name):
            break
        data_set.append(json.load(open(file_name,"r")))
        k+=1

    result={}
    for i in range(k):
        train_set=[]
        for j in range(k):
            if j!=i:
                train_set.extend(data_set[j])
        test_set=data_set[i]
        curr_result=train_and_eval(config=config, train_set=train_set,test_set=test_set)
        if print_all:
            print("{} : {}".format(i,json.dumps(curr_result)))
        for key in curr_result.keys():
            if key not in result:
                result[key]=[]
            result[key].append(curr_result[key])
    result_mean={}
    result_std={}
    for key in result.keys():
        result_mean[key]=round(np.mean(result[key]),6)
        result_std[key]=round(np.std(result[key]),6)
    print("Mean : ",end="")
    print(result_mean)
    print("Std : ",end="")
    print(result_std)