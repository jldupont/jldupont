"""
    @author: Jean-Lou Dupont
"""

from google.appengine.ext import db

class DebianRepos(db.Model):
    """
    Debian Repository Information
    
    List of source Repos forming the Virtual Repository.
    """
    url=db.StringListProperty(required=True)
    component=db.StringListProperty(required=True)
    distribution=db.StringListProperty(required=True)
    


class DebianRepoVersions(db.Model):
    """
    Debian Repository Version Information
    
    Each row in this table corresponds to a version
    of the source repository.  An 'entry_count' is 
    maintained to track the number of entries written
    in the table `DebianPackageEntries'. 
    """
    repo        = db.ReferenceProperty(DebianRepo)
    version     = db.StringListProperty(required=True)
    entry_count = db.IntegerProperty(default=0)
    
    
class DebianPackageEntries(db.Model):
    """
    Debian Package Entries
    
    Each row corresponds to a package from a specific
    source repository of a specific version.
    
    The field `version` corresponds to the field
    of the same name in the table `DebianRepoVersions'.
    
    The field `data` corresponds to the textual entry
    associated with the package entry taken from the
    `Packages.gz` file from the source Repository.
    """   
    version         = db.StringListProperty(required=True)
    package_name    = db.StringListProperty(required=True)
    package_version = db.StringListProperty(required=True)
    data            = db.StringListProperty(default=None)
      

class DebianVirtualRepositoryVersion(db.Model):
    """
    Virtual Repository Information
    
    Each row in this table makes up an association 
    between a source repository package list and
    a virtual repository package version. In other words,
    each VR Version is made up of a list of specific
    packages from the source repositories.
    """
    vr_version = db.StringListProperty(required=True)
    