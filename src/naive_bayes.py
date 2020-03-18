from .progress_printer import ProgressPrinter
import numpy as np

class NaiveBayesClassifier:
    def __init__(self, lmd):
        self.lmd=lmd
        self.statistic={}
        self.features={}
        self.n_train_set=0
    
    def fit(self,data):
        self.n_train_set=len(data)
        pp=ProgressPrinter(self.n_train_set,prefix="Training... ",digit=1)
        for doc in data:
            label=doc["label"]
            d=doc["input"]
            if label not in self.statistic:
                self.statistic[label]={"n":0,"count":{}}
            self.statistic[label]["n"]+=1
            for key in d.keys():
                if type(d[key])==str:
                    seq=[d[key]]
                elif type(d[key])==list:
                    seq=d[key]
                else:
                    continue
                
                if key not in self.statistic[label]["count"]:
                    self.statistic[label]["count"][key]={}
                if key not in self.features:
                    self.features[key]={}
                for feature in seq:
                    if feature not in self.statistic[label]["count"][key]:
                        self.statistic[label]["count"][key][feature]=0
                    if feature not in self.features[key]:
                        self.features[key][feature]=0
                    self.statistic[label]["count"][key][feature]+=1
                    self.features[key][feature]+=1
            pp.go()
        self.label=list(self.statistic.keys())
        self.n_label=len(self.label)
    
    def get_p(self,label,key,feature):
        try:
            u=self.statistic[label]["count"][key][feature]
        except:
            u=0
        try:
            v=self.statistic[label]["n"]
        except:
            return 0
        return (u+self.lmd)/(v+self.lmd*2)
    
    def predict(self,data):
        if not self.n_train_set:
            raise RuntimeError
        ret=[]
        pp=ProgressPrinter(len(data),prefix="Testing ... ")
        for d in data:
            p=[]
            for label in self.statistic.keys():
                curr_p=np.log(self.statistic[label]["n"])-np.log(self.n_train_set)
                for key in d.keys():
                    if type(d[key])==str:
                        seq=[d[key]]
                    elif type(d[key])==list:
                        seq=d[key]
                    else:
                        continue
                    x=0
                    for feature in seq:
                        tmp=self.get_p(label,key,feature)
                        x+=np.log(tmp)
                    curr_p+=x
                p.append((curr_p,label))
            pred=max(p)[1]
            ret.append(pred)
            pp.go()
        return np.array(ret)