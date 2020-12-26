import mistletoe
from pprint import pprint
from bs4 import BeautifulSoup

def dictify(ul):
    result = {}
    for li in ul.find_all("li", recursive=False):
        key = next(li.stripped_strings)
        ol = li.find("ol")
        if ol:
            result[key] = dictify(ol)
        else:
            result[key] = None
    return result

def printter(dicc,lvl=0,prefix=''):
    count = 1
    for dic in dicc:
        print(('\t')*lvl,prefix+str(count),dic)
        if(dicc[dic] is not None):
            printter(dicc[dic],lvl=lvl+1,prefix=(prefix+str(count)+'.'))
        count+=1
    

with open('../Hardware/Reference/Specifications.md', 'r', encoding="utf8") as fin:
    rendered = mistletoe.markdown(fin)
    soup = BeautifulSoup(rendered)
    printter(dictify(soup.body.ol))
