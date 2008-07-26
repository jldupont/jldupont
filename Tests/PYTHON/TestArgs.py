class A:
    def m(self, *args, **keys):
        
        print "args length= %i" % len(args)
        print "keys length= %i" % len(keys)
        
        for a in args:
            print "a=%s" % a
        for i in keys:
            print "i=%s" % i

if (__name__ == "__main__" ):
    a=A()
    a.m(1,2,3,k1="v1",k2="v2")
    
"""
args length= 3
keys length= 2
a=1
a=2
a=3
i=k2
i=k1
"""