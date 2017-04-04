
class Node():
    def __init__(self, fstats=[], names=[]):
        self.fstats = fstats
        self.n = 0
        self.stat = dict()
        for f in names:
            self.stat[f] = None
        self.names = names

    def update(self, log):
        #v = (v_0, v_1)
        #v_0 - extract stat from log
        #v_1 - update stat from Node by v[0](log)

        for k in range(len(self.fstats)):
            name = self.names[k]
            v = self.fstats[k]
            if not self.stat[name]:
                self.stat[name] = v[0](log)
            else:
                self.stat[name] = v[1](self.stat[name], v[0](log))

        self.n += 1

    def __str__(self):
        strs = []
        for name in self.names:
            strs.append(name + ': ' + str(self.stat[name]))
        return 'Node(' + '; '.join(strs) + ')'

    def __repr__(self):
        return str(self)
