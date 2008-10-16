
class X(object):
    def __get__(self, object, var):
        print "class [%s].__get__ var[%s]" % (self.__class__, var)
       
    def __getattr__(self, var): 
        print "class [%s].__getattr__ var[%s]" % (self.__class__, var)
        if (var == 'info'):
            raise AttributeError()
            
class Y(object):
    def __getattr__(self, var): 
        print "class [%s].__getattr__ var[%s]" % (self.__class__, var)
    
    def __getattribute__(self, var): 
        #print "class [%s].__getattribute__ var[%s]" % (self.__class__, var)
        return object.__getattribute__(self, var)
         
class Z(object):
    def __init__(self, var):
        self.var = var
    
    def __get__(self, instance, owner):
        print "class [%s].__get__ instance[%s] owner[%s]" % (self.__class__, instance, owner)
        return 'intercepted!'
    
class Game(object):
    z1 = Z(1)
    z2 = Z(2)
            
if __name__ == "__main__":
    x = X()
    x.x
        
    y = Y()
    y.y
        
    print Game.z1
    print Game.z2
    