#!/bin/bash

seed_list=(123456789 998244353 100000007)
src_path="../trec06p"
k=5

for seed in ${seed_list[@]}; do
	python3 get_data.py --src ${src_path} --dst data/${seed} --seed ${seed} -k ${k}
done

for seed in ${seed_list[@]}; do
	echo $seed
	# TODO
done
