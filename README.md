# README

git repo: [https://github.com/wangyurzee7/NaiveBayes4SpamDetection](https://github.com/wangyurzee7/NaiveBayes4SpamDetection)

## Environment and Dependence

* OS: `macOS Catalina 10.15.3`

* Python Version: `Python 3.7.6`

* Packages: `numpy`

## How to Run?

`get_data.py` is used for pre-processing datas.

`main.py` can train and test on the specified dataset.

`kfold.py` is used for k-fold cross validation.

You can know how to run by `--help`:

```

```

Here is a sample config for `main.py`:

```

```

Here is a sample config for `kfold.py`:

```

```

## How to Recurrence Experiment in the Report

If the source data is at `${src_path}/trec06p`

```
chmod +x run.sh
./run.sh ${src_path}/trec06p
```

