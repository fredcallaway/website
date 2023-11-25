import json
import re
from toolz import partition

def reformat_authors(author_string):
    # Split the string into individual author entries
    s = author_string.strip().replace('^&ast;^', '*').replace(',*', '*,')
    parts = s.replace(", &", " &").replace(' &', ',').split(", ")

    authors = []
    for (last_name, initials) in partition(2, parts):
        auth = initials.replace('.', '').replace(' ', '') + ' ' + last_name
        if '*' in auth:
            auth = auth.replace('*', '') + '*'
        authors.append(auth)

    return ", ".join(authors)


# Example usage
author_string = "Correa, C. G., Ho, M. K., Callaway, F., Daw, N. D., & Griffiths, T. L."
reformat_authors(author_string)

def citekey(authors, year, title):
    year = str(year)
    if year == 'in press':
        year = '2023'
    elif ' ' in year:
        return None
    return (authors.split(',', 1)[0] + year + title.split(' ', 1)[0]).lower().strip()

type_map = {
    "Conference presentations": "presentation",
    "Refereed conference papers": "proceedings",
    "In preparation": "prep",
    "Journal articles": "journal"
}

def parse_references(text):
    # Split the text into sections
    sections = re.split(r'\n### ', text)
    publications = []

    for section in sections[1:]:
        lines = section.split('\n')
        section_title = lines[0].strip()

        for line in lines[1:]:
            if line.startswith('- '):
                # Extract authors, year, and title
                author_year_title = re.match(r'^(.+?)\((.*)\)\. (.+)$', line[2:])
                if not author_year_title:
                    print(line)
                if author_year_title:
                    authors, year, title = author_year_title.groups()

                    # Extract venue if present
                    venue = re.search(r'_([^_]+)_', title)
                    venue = venue.group(1) if venue else ""

                    # Extract link if present
                    link = re.search(r'\(https?://[^)]+\)', title)
                    link = link.group(0)[1:-1] if link else ""

                    # Clean title by removing link and venue parts
                    title = re.sub(r'\[link\]|\(https?://[^)]+\)|_[^_]+_', '', title).strip()

                    if venue == '':
                        venue = None
                    if len(year) == 4:
                        year = int(year)
                    publications.append({
                        "title": title.replace('.', '').strip(),
                        "authors": reformat_authors(authors),
                        "year": year,
                        "venue": venue,
                        "link": link,
                        "type": type_map[section_title],
                        "citekey": citekey(authors, year, title),
                    })

    return publications


# Replace the text variable below with your actual list of references
with open('input.md') as f:
    text = f.read()


import yaml
# Parse and convert to JSON
parsed_data = parse_references(text)
print(len(parsed_data), 'references found')

with open("pubs.yml", 'w') as f:
    f.write(yaml.dump(parsed_data, allow_unicode=True, sort_keys=False, width=140).replace('- title', '\n- title'))

# Output the JSON data
# print(json_data)

with open("pubs.yml", 'r') as f:
    pubs = yaml.safe_load(f)
pubs[0]
assert pubs == parsed_data
