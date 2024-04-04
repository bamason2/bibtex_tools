# tools to clean bibtex files i.e. replace all citation keys with unique six digit number 
# and add a citation key to entries who are missing one.

import re
from random import randint


# n digit random integer generator
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# clean up .bib file
def unique_citation_key(file, export_filename):
    with open(file, encoding='utf-8') as f:
        file_contents = f.read()
        
    # replace the citation key with random 6 digit number
    strings = re.findall(r'[@\w+]+{\w+', file_contents)
    for string in strings:
        pattern = string.split('{',1)[1]
        file_contents = re.sub(pattern, str(random_with_N_digits(6)), file_contents, 1)

    with open(export_filename, 'w') as f:
        f.write(file_contents)

def fill_citation_key(file, export_filename):
    with open(file, encoding='utf-8') as f:
        file_contents = f.read()

    # find missing citation keys and replace with random 6 digit number
    strings = re.findall(r'{,', file_contents)
    for string in strings:
        pattern = '{,'
        file_contents = re.sub(pattern, '{'+str(random_with_N_digits(6))+',', file_contents, 1)

    with open(export_filename, 'w') as f:
        f.write(file_contents)

unique_citation_key(file='files/export.bib', export_filename='files/export_modified.bib')
fill_citation_key(file='files/export_modified.bib', export_filename='files/export_modified.bib')


