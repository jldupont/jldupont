#!/usr/bin/env python
"""
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "$Id$"

__all__ = ['prepareFeedTemplate',]

from libs.feed.type0 import FeedRss

_feed_template = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <atom:link href="http://www.jldupont.com/services/pypirss/rss/$package" rel="self" type="application/rss+xml" />
        
        <title>Package <$package></title>
        <description>RSS feed for PYPI package <$package></description>
        <link>http://www.jldupont.com/services/pypirss/rss/$package</link>

        $items

    </channel>
</rss>
"""

_item_template = """
        <item>
            <title>Statistics for <$package></title>
            <description>Release[$release] Downloads[$downloads]</description>
            <link>http://pypi.python.org/pypi/pypp/$package</link>
            <pubDate>$itemPubDate</pubDate>
            <guid isPermaLink='false'>$itemGUID</guid>
        </item>
"""

def prepareFeedTemplate():
    return FeedRss( _feed_template, _item_template )
