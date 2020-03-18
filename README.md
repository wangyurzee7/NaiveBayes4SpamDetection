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
                   [--k-groups K_GROUPS] [--utf8-only] [--do-not-shuffle]

optional arguments:
  -h, --help            show this help message and exit
  --src SRC             Source data (directory `trec06p`) path
  --dst DST             Destination path
  --seed SEED           Random seed, default=19260817
  --k-groups K_GROUPS, -k K_GROUPS
                        The number of groups you want to divide the dataset
                        into, default=5
  --utf8-only           Only collect datas encoded by UTF-8
  --do-not-shuffle      Do not do random shuffle

$ python3 main.py --help
usage: main.py [-h] --config CONFIG

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  Config file path

$ python3 kford.py --help
usage: kford.py [-h] --config CONFIG [--print-all-results]

optional arguments:
  -h, --help           show this help message and exit
  --config CONFIG      Config file path
  --print-all-results  Print all results when each group is test set.
```

Besides, here is a sample config for `main.py`:

```
{
    "train_file": ["data/test/data_0.json","data/test/data_1.json","data/test/data_2.json","data/test/data_3.json"], // Train file list
    "test_file": ["data/test/data_4.json"], // Test file list

    "lambda": 1.0, // Parameter lambda for Laplace Smoothing

    "accuracy_method": [ // Accuracy functions. In addition to the following, 'micro-f1' is also supported(for multi-label classification task)
        "accuracy",
        "macro-precision",
        "macro-recall",
        "macro-f1"
    ]
}
```

Here is a sample config for `kfold.py`:

```
{
    "data_path": "data/test/", // Data path. Data files in this path should be named as `data_{i}.json`

    // fields below are same as the config for `main.py`
    "lambda": 1.0,

    "accuracy_method": [
        "accuracy",
        "macro-precision",
        "macro-recall",
        "macro-f1"
    ]
}
```

These two configs above can be found at `config/samples`

## How to Reproduce Experiment in the Report

If the source data is at `${src_path}/trec06p`.

```
chmod +x run.sh
./run.sh ${src_path}/trec06p
```

## Experimental Report

See `report.md` or `report.pdf`.
