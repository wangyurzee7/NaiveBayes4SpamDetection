from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def accuracy(y_true,y_pred):
    return accuracy_score(y_true=y_true,y_pred=y_pred)

def macro_precision(y_true,y_pred):
    return precision_score(y_true=y_true,y_pred=y_pred,average="macro")

def macro_recall(y_true,y_pred):
    return recall_score(y_true=y_true,y_pred=y_pred,average="macro")

def macro_f1(y_true,y_pred):
    return f1_score(y_true=y_true,y_pred=y_pred,average="macro")

def micro_f1(y_true,y_pred):
    return f1_score(y_true=y_true,y_pred=y_pred,average="micro")

method_list={
    "accuracy": accuracy,
    "macro-precision": macro_precision,
    "macro-recall": macro_recall,
    "macro-f1": macro_f1,
    "micro_f1": micro_f1,
}

def get_accuracy_method(method_name):
    if method_name in method_list.keys():
        return method_list[method_name]
    raise NotImplementedError