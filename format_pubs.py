#!/usr/bin/env python3

import os
import sys
import yaml
from toolz import groupby

type_map = {
    "prep": "In preparation",
    "journal": "Journal articles",
    "proceedings": "Refereed conference papers",
    "presentation": "Conference presentations",
}

paper_icon = {
    'tex': '\\faFilePdfO',
    'html': '<span class="fa fa-file"></span>',
}

star = {
    'tex': "^&ast;^",
    'html': "<sup>&ast;</sup>",
}

selected = [
    'callaway2022planning',
    'callaway2021fixation',
    'callaway2023metamemory',
    'callaway2023nudging',
    'callaway2022leveraging',
]

here = os.path.dirname(os.path.abspath(__file__))
with open(f"{here}/pubs.yml", 'r') as f:
    pubs = yaml.safe_load(f)
grouped_pubs = groupby('type', pubs)

def format_pub(pub, fmt):
    pub['authors'] = pub['authors'].replace('*', star[fmt])
    txt = ""
    if fmt == 'tex':
        txt += "- "
    txt += "{authors} ({year}). {title}. ".format_map(pub)

    if pub["venue"]:
        # if pub['type'] == 'proceedings':
        #     txt += "In "
        # elif pub['type'] == 'presentation':
        #     txt += "At "
        txt += '_{venue}_. '.format_map(pub)

    if pub['link']:
        pub['icon'] = paper_icon[fmt]
        txt += "[{icon}]({link})".format_map(pub)

    return txt + '\n'

def write_pubs(file, fmt='tex', skip_types=[]):
    for typ, name in type_map.items():
        if typ in skip_types:
            continue
        print("\n###", name, '\n', file=file)
        for pub in grouped_pubs[typ]:
            print(format_pub(pub, fmt), file=file)


def write_selected(file, fmt='html'):
    selected_pubs = [p for p in pubs if p['citekey'] in selected]
    selected_pubs.sort(key=lambda pub: selected.index(pub['citekey']))
    for pub in selected_pubs:
        print(format_pub(pub, fmt), file=file)


def update_file(fn, selected=False):
    with open(fn) as f:
        lines = f.readlines()

    with open(fn, 'w') as f:
        for line in lines:
            if '<<PUBS>>' in line:
                f.write(line + '\n')
                if selected:
                    write_selected(f)
                else:
                    write_pubs(f, 'html', ['presentation'])
                break
            else:
                f.write(line)


def filter_stdin():
    for line in sys.stdin.readlines():
        if line == '<<PUBS>>\n':
            write_pubs(sys.stdout)
        else:
            print(line, end='')

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'cv':
        filter_stdin()
    elif mode == 'web':
        update_file('content/pages/publications.md')
        update_file('content/pages/about.md', selected=True)

