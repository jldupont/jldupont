#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

from string import Template

class FeedRss(object):
    """ Base class for feeds.
        Use 'produce' method for substituting with $ escape
    """
    def __init__(self, feed_template, item_template):
        self.feed_template = feed_template
        self.item_template = item_template

    def produce(self, feed_params, item_params_list):
        """
            feed_params: dictionary of feed level parameters
            item_params_list: list of dictionaries, each entry corresponds to an item in the feed
        """        
        result = ''
        for params in item_params_list:
            result = result + self.item_template.substitute( params )
           
        feed_params['items'] = result
        feed = self.feed_template.substitute( feed_params ) 
        
        return feed
