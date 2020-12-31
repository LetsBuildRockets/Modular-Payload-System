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
            result[li.text.rstrip()] = None

    return result

def printter(outp,dicc,lvl=0,prefix=''):
    count = 1
    for dic in dicc:
        print(prefix+str(count)+" "+dic)
        if(dicc[dic] is not None):
            outp.write("\""+prefix+str(count)+"\",\""+dic.replace("\"","")+"\",\"HEADING\",\"N/A\",\"\"\n")
            printter(outp,dicc[dic],lvl=lvl+1,prefix=(prefix+str(count)+'.'))
        else:
            if dic.lower().startswith('reference:'):
                outp.write("\""+prefix+str(count)+"\",\""+dic.replace("\"","")+"\",\"REFERENCE\",\"N/A\",\"\"\n")
            else:
                outp.write("\""+prefix+str(count)+"\",\""+dic.replace("\"","")+"\",\"\",\"\",\"\"\n")
        count+=1
    

with open('../Hardware/Reference/Specifications.md', 'r', encoding="utf8") as fin:
    rendered = mistletoe.markdown(fin)
    soup = BeautifulSoup(rendered,features="lxml")
    with open('../XXX-NNM Compliance Matrix.csv', 'w+', encoding="utf8") as outp:
        outp.seek(0)
        outp.write("\"Number\",\"Requirement\",\"Compliant\",\"Method\",\"Comment\"\n")
        printter(outp,dictify(soup.body.ol))
        printter(outp,dictify(soup.findAll('h2')[3].next_element.next_element.next_element),prefix='HR.')
        outp.truncate()
        print('Created Compliance Matrix template: "XXX-NNM Compliance Matrix.csv"')
        outp.close()
