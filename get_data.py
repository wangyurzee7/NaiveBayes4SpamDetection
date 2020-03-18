import os
import sys
import json
import random

import argparse

from src.data_loader import data_loader

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="Source data (directory `trec06p`) path")
    parser.add_argument("--dst", required=True, help="Destination path")
    parser.add_argument("--seed", type=int, default=19260817, help="Random seed, default=19260817")
    parser.add_argument("--k-groups", "-k", type=int, default=5, help="The number of groups you want to divide the dataset into, default=5")
    parser.add_argument("--utf8-only", help="Only collect datas encoded by UTF-8", action="store_true")
    parser.add_argument("--do-not-shuffle", help="Do not do random shuffle", action="store_true")

    args=parser.parse_args()
    seed=args.seed
    src_path=args.src
    dst_path=args.dst
    k=args.k_groups
    utf8_only=args.utf8_only
    do_not_shuffle=args.do_not_shuffle
    random.seed(seed)

    print("Pre-processing Data")

    
    if src_path.endswith(".json"):
        print("Loading data from JSON file '{}' ...".format(src_path))
        data=json.load(open(src_path,"r"))
    else:
        print("Getting data from '{}' {}...".format(src_path,"(UTF-8 datas only)" if utf8_only else ""))
        data=data_loader(src_path,utf8_only=utf8_only)
    n_data=len(data)

    if do_not_shuffle:
        print("Dividing {} pieces of data into {} groups without shuffling.".format(n_data,k))
    else:
        print("Randomly dividing {} pieces of data into {} groups, using random seed {}.".format(n_data,k,seed))
    print("Saving at '{}'.".format(dst_path))
    if os.path.exists(dst_path):
        print("Warning !!!! Destination path already exists. Files of the same name may be covered.")
    else:
        os.makedirs(dst_path, exist_ok=True)
    
    if not do_not_shuffle:
        for _ in range(10):
            random.shuffle(data)
    for i in range(k):
        curr_data=data[n_data*i//k : n_data*(i+1)//k]
        if k>1:
            file_name=os.path.join(dst_path,"data_{}.json".format(i))
        else:
            file_name=os.path.join(dst_path,"data.json")
        print(" - '{}' contains {} pieces of data".format(file_name,len(curr_data)))
        json.dump(
            curr_data,
            open(file_name,"w"),
            indent=2,
        )

    print("Saved.")
    print("Pre-processing finished.")
    print("")


    
