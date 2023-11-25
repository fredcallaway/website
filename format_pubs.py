#!/usr/bin/env python3

import os
import sys
import yaml
from toolz import groupby

here = os.path.dirname(os.path.abspath(__file__))

type_map = {
    "prep": "In preparation",
    "journal": "Journal articles",
    "proceedings": "Refereed conference papers",
    "presentation": "Conference presentations",
}

def format_pub(pub):
    pub['authors'] = pub['authors'].replace('*', "^&ast;^")
    txt = "- {authors} ({year}). {title}. ".format_map(pub)
    if pub["venue"]:
        # if pub['type'] == 'proceedings':
        #     txt += "In "
        # elif pub['type'] == 'presentation':
        #     txt += "At "
        txt += '_{venue}_. '.format_map(pub)
    if pub['link']:
        txt += "[\\faFilePdfO]({link})".format_map(pub)
    return txt + '\n'

with open(f"{here}/pubs.yml", 'r') as f:
    pubs = yaml.safe_load(f)
grouped = groupby('type', pubs)

for line in sys.stdin.readlines():
    if line == '<<PUBS>>\n':
        for typ, name in type_map.items():
            print("\n###", name, '\n')
            for pub in grouped[typ]:
                print(format_pub(pub))
    else:
        print(line, end='')




