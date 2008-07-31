class Test(object):
    
    def method1(self, p1):
        print "method1"
        
if (__name__ == "__main__" ):
    t= Test()
    
    print t.method1.im_class.__name__
    #print t.method1.__class__