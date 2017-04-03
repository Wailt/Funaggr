
class Node():
    def __init__(self, fstats=[], names=[]):
        self.fstats = fstats
        self.stat = dict()
        for f in range(len(fstats)):
            self.stat[f] = None
        self.names = names

    def update(self, log):
        #v = (v_0, v_1)
        #v_0 - extract stat from log
        #v_1 - update stat from Node by v[0](log)

        for k, v in enumerate(self.fstats):
            if not self.stat[k]:
                self.stat[k] = v[0](log)
            else:
                self.stat[k] = v[1](self.stat[k], v[0](log))
