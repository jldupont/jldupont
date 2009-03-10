#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['feed',]

from libs.feed.type2 import FeedRss

_feed_template = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <atom:link href="^^feedLink" rel="self" type="application/rss+xml" />
        
        <title>^^feedTitle</title>
        <description>^^feedDescription</description>
        <link>^^feedLink</link>

        $items

    </channel>
</rss>
"""

_item_template = """
        <item>
            <title>^^itemTitle</title>
            <description>$itemDescription</description>
            <link>^^itemLink</link>
            <pubDate>$itemPubDate</pubDate>
            <guid isPermaLink='false'>$itemGUID</guid>
        </item>
"""

feed=FeedRss( feed_template, item_template )

base_feed = {'feedLink':"Feed Link", 
             'feedTitle':"Feed Title", 
             'feedDescription':'Feed Description' }

base_item = {'itemTitle':'Item Title', 
             'itemLink':'Item Link'}

feed.prepare( base_feed, base_item )
