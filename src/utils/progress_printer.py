class ProgressPrinter:
    def __init__(self,n,digit=1,prefix=""):
        self.n=n
        self.i=0
        self.buf=prefix+"Progress: {}%"
        self.k=10**digit
        self.print()
    def print(self):
        print(self.buf.format(self.i*100*self.k//self.n/self.k),end="\r")
    def go(self):
        self.i+=1
        if self.i*100*self.k//self.n!=(self.i-1)*100*self.k//self.n:
            self.print()