"""
    @author: Jean-Lou Dupont
"""
def verifyQuotes(tag_name, obj):
    if (obj is None):
        return
    
    if (type(obj) == 'list'):
        for o in obj:
            if not (o[0] == o[-1] and o[0] in ('"', "'")):
                raise template.django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, o)
            
    if (type(obj) == 'str'):
        if not (obj[0] == obj[-1] and obj[0] in ('"', "'")):
            raise template.django.template.TemplateSyntaxError, "%r tag's parameter[%s] be in quotes" % (tag_name, obj)
    
