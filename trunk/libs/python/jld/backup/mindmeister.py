""" Backup for MindMeister mindmaps
""" 
import jld.api.mindmeister as mm

from optparse import OptionParser


def main():
    usage = "%prog [options] secret_key  api_key"

    parser = OptionParser( usage=usage )
    
    if sys.platform[:3] == 'win':
        pass
    else:
        pass


if __name__== "__main__":
    main()
