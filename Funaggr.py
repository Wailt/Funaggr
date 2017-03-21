from copy import deepcopy
from pprint import pprint


class Funaggr():
    def __init__(self, features=[], names=[]):
        if not features:
            raise Exception("Empty function list")
        self.features = features
        self.names = names
        self.data = dict()
        self.n = len(features)
        self.rename = False

    def update(self, logs):
        if not type(logs) is list:
            logs = [logs, ]
        map(self.__update_by_one, logs)

    def __update_by_one(self, log):
        feature = [f(log) for f in self.features]
        x = self.data

        for i in range(self.n):
            feat = feature[i]

            key = (self.names[i] + ": " + str(feat)) if len(self.names) == self.n and self.rename else str(feat)

            if i < self.n - 1:
                x.setdefault(key, dict())
                x = x[key]
            else:
                x.setdefault(key, [])
                x[key].append(log)

    def fapp(self, f):
        if not type(f) is list:
            f = [f, ]
        y = deepcopy(self.data)
        for fun in f:
            self.__app(fun, deep=0, y=y)
        return y

    def __app(self, f, deep=0, y=None):
        for key in y:
            if deep < self.n - 1:
                self.__app(f, deep=deep + 1, y=y[key])
            else:
                y[key] = f(y[key])

    def __str__(self):
        pprint(self.data)
        return str(self.data)

    def to_list(self, data=None, deep=0):
        if not data:
            data = self.data
        result = []
        if deep < self.n:
            for key in data:
                result += self.to_list(data=data[key], deep=deep + 1)
        else:
            return data
        return result

    def merge(self, aggs):
        map(self.update, aggs.to_list())

    def reaggr(self, features, names=[]):
        data = self.to_list()
        self.data = dict()
        self.features = features
        self.n = len(features)
        self.names = names
        map(self.update, data)
