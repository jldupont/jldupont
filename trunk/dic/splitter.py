import os
import sys

type_blacklist = {}

type_map = {    'Verb':         'v',
                'Noun':         'n',
                'Adverb':       'adv',
                'Interjection': 'intj',
                'Adjective':    'adj',
                'Conjunction':  'conj',
                'Article':      'a',
                'Contraction':  'contr',
                'Pronoun':      'p',
                'Inflexion':    'inf',
                'Prefix':       'p',
                'Suffix':       's',
                #'':'',
                #'':'',
            }

lang_list = { 'Mandarin': False,
                'Breton': False,
                'Scots':  False,
            }

lang_map = {    'English':      'en',
                'French':       'fr',
                'German':       'de',
                'Italian':      'it',
                'Spanish':      'es',
                'Swedish':      'sv',
                'Latin':        'la',
                'Dutch':        'nl',
                'Japanese':     'ja',
                'Indonesian':   'id',
                'Bosnian':      'bs',
                'Croatian':     'hr',
                'Irish':        'ga',
                'Romanian':     'ro',
                'Czech':        'cs',
                'Esperanto':    'eo',
                'Catalan':      'ca',
                #'':'',
                #'':'',
            }


input = "output.csv"
leftovers = "leftovers.csv"

done = False

ifile = open(input,"r")
lfile = open(leftovers,"r")

while not done:
    line = ifile.readline()
    if line is "":
        done = True
        continue
    
    #strip and split
    parts = line.rstrip("\n").split(",")
    
    #more stripping
    parts = map(lambda x:x.lstrip(), parts)
    
    
    
#END
ifile.close()
lfile.close()
