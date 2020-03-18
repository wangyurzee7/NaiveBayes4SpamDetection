#!/bin/bash

seed_list=(123456789 998244353 100000007)
src_path=$1

if (($#==0)); then
	echo Too Few Arguments.
	exit
fi

python3 get_data.py --src ${src_path} --dst data/ --do-not-shuffle -k 1
for seed in ${seed_list[@]}; do
	python3 get_data.py --src data/data.json --dst data/${seed}_5 --seed ${seed} -k 5
done

for ((i=2;i<=4;++i)); do
	python3 get_data.py --src data/data.json --dst data/${seed}_${i} -k ${i}
done

for seed in ${seed_list[@]}; do
	echo $seed
done
