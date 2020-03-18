# README

git repo: [https://github.com/wangyurzee7/NaiveBayes4SpamDetection](https://github.com/wangyurzee7/NaiveBayes4SpamDetection)

## Environment and Dependence

* OS: `macOS Catalina 10.15.3`

* Python Version: `Python 3.7.6`

* Packages: `numpy`, `sklearn`

## How to Run?

`get_data.py` is used for pre-processing datas.

`main.py` can train and test on the specified dataset.

`kfold.py` is used for k-fold cross validation.

You can know how to use them by `--help`:

```
$ python3 get_data.py --help
usage: get_data.py [-h] --src SRC --dst DST [--seed SEED]
                   [--k-groups K_GROUPS]

optional arguments:
  -h, --help            show this help message and exit
  --src SRC             Source data (directory `trec06p`) path
  --dst DST             Destination path
  --seed SEED           Random seed, default=19260817
  --k-groups K_GROUPS, -k K_GROUPS
                        The number of groups you want to divide the dataset
                        into, default=5
```

Besides, here is a sample config for `main.py`:

```

```

Here is a sample config for `kfold.py`:

```

```

## How to Recurrence Experiment in the Report

If the source data is at `${src_path}/trec06p`.

```
chmod +x run.sh
./run.sh ${src_path}/trec06p
```

## Experimental Report

See `report.md` or `report.pdf`.
