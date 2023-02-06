class listreverse():

    def __init__(self,nlist):
        self.nlist = nlist

    def listrmethod(self,nlist):
         self.nlist.append(nlist)

lr = listreverse([1,2,3,4,5])
print(lr.nlist)
lr.listrmethod(6)
print(lr.nlist)
