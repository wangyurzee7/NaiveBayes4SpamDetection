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

    args=parser.parse_args()
    seed=args.seed
    src_path=args.src
    dst_path=args.dst
    k=args.k_groups
    utf8_only=args.utf8_only
    random.seed(seed)

    print("Pre-processing Data")

    print("Getting data from '{}' {}...".format(src_path,"(UTF-8 datas only)" if utf8_only else ""))
    data=data_loader(args.src,utf8_only=utf8_only)
    n_data=len(data)

    print("Randomly dividing {} pieces of data into {} groups, using random seed {}.".format(
        n_data,k,seed
    ))
    print("Saving at '{}'.".format(dst_path))
    if os.path.exists(dst_path):
        print("Warning !!!! Destination path already exists. Files of the same name may be covered.")
    else:
        os.makedirs(dst_path, exist_ok=True)
    
    for _ in range(10):
        random.shuffle(data)
    for i in range(k):
        curr_data=data[n_data*i//k : n_data*(i+1)//k]
        file_name=os.path.join(dst_path,"data_{}.json".format(i))
        print(" - '{}' contains {} pieces of data".format(file_name,len(curr_data)))
        json.dump(
            curr_data,
            open(file_name,"w"),
            indent=2,
        )

    print("Saved.")
    print("Pre-processing finished.")
    print("")


    
