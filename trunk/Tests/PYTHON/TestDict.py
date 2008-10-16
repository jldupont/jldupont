class X(object):
    
    def __getattr__(self, attr):
        return object.__getattribute__(self, attr)

    def getFromDict(self, attr):
        return self.__dict__[attr]
    
    
if __name__ == "__main__":
    x = X()
    
    x.var1 = 'var1'
    
    print x.var1
    print "============"
    print x.getFromDict( 'var1' )
    print "============"
    print x.getFromDict( 'var2' )
    