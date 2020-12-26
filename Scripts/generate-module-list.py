from os import listdir
from os.path import isfile, join
from urllib.request import urlopen
import json

hardwareIgnoreList = ['Reference', 'lib']
moduleNames = listdir('./Hardware')
repoowner = 'LetsBuildRockets'
reponame = 'Modular-Payload-System'
modules = []

class Module:
    def __init__(self, number):
        self.number = number
        self.revision = '-'
        self.datasheet = '-'
        self.release = '-'

moduleNames = [x.upper() for x in moduleNames]
for ig in hardwareIgnoreList:
    while ig.upper() in moduleNames: moduleNames.remove(ig.upper())

githubtags = json.load(urlopen('https://api.github.com/repos/'+repoowner+'/'+reponame+'/tags'))

for modulename in moduleNames:
    module = Module(modulename)
    PrjPcbPath = './Hardware/'+modulename+'/'+modulename+'.PrjPcb'
    if isfile(PrjPcbPath):
        PrjPcb = []
        for line in open(PrjPcbPath, "r"):
            PrjPcb.append(line.rstrip())
        if 'name=projectrevision' in [x.lower() for x in PrjPcb]:
            module.revision = (PrjPcb[[x.lower() for x in PrjPcb].index('name=projectrevision')+1][6:])
            for tag in githubtags:
                if tag['name'] == module.number+'-'+module.revision:
                    module.release = 'https://github.com/'+repoowner+'/'+reponame+'/releases/tag/'+tag['name']
                        
    datasheetpath = PrjPcbPath = './Hardware/'+modulename+'/docs/datasheet.md'
    if isfile(datasheetpath):
        module.datasheet='https://github.com/'+repoowner+'/'+reponame+'/blob/master/Hardware/'+modulename+'/docs/datasheet.md'
        
    modules.append(module)


def make_markdown_table(array):

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"

moduleList = [['Number', 'Revision', 'Datasheet']]
for module in modules:
    if module.release != '-':
        module.revision = '['+module.revision+']('+module.release+')'
    else:
        if module.revision != '-':
            module.revision = module.revision+' (draft)'
        
    if module.datasheet != '-':
        module.datasheet = '[datasheet]('+module.datasheet+')'

    moduleList.append([module.number,module.revision,module.datasheet])

with open('./ModuleList.md', "r+") as f:
    data = f.read()
    f.seek(0)
    f.write('# Module List')
    f.write(make_markdown_table(moduleList))
    f.truncate()
    
        
