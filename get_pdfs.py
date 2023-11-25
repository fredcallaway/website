import requests
import os
import yaml
import PyPDF2
from glob import glob

def is_valid_pdf(filename):
    try:
        with open(filename, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if len(reader.pages) > 0:  # Check if it has at least one page
                return True
    except Exception:
        return False
    return False

def get_pdf(url, citekey):
    filename = f'content/pdfs/{citekey}.pdf'
    if os.path.isfile(filename):
        return filename

    local = glob(f'/Users/fred/zotero/storage/*/{citekey}*')
    if len(local):
        os.system(f'cp "{local[0]}" "{filename}"')
        print(f'SUCCESS {citekey}: using local copy of {filename}')
        return filename

    if not url:
        print(f"ERROR {citekey}: no local file or url")
        return
    if 'psyarxiv' in url and 'download' not in url:
        url += '/download'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        with open(filename, 'wb') as f:
            f.write(response.content)

        if is_valid_pdf(filename):
            print(f"SUCCESS {citekey}: downloaded and verified {filename}")
            return filename
        else:
            print(f"ERROR {citekey}: {url} is not a valid PDF.")
            os.remove(filename)  # Optionally remove the invalid file

    except requests.RequestException as e:
        print(f"ERROR {citekey}: downloading {url} {e}")

def main():
    with open("pubs.yml", 'r') as f:
        pubs = yaml.safe_load(f)

    for pub in pubs:
        file = get_pdf(pub['link'], pub['citekey'])
        if file:
            assert is_valid_pdf(file)
            pub['link'] = f"https://fredcallaway.com/pdfs/{os.path.basename(file)}"

    with open("pubs.yml", 'w') as f:
        f.write(yaml.dump(pubs, allow_unicode=True, sort_keys=False, width=140).replace('- title', '\n- title'))








if __name__ == "__main__":
    main()
