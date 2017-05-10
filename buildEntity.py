__author__ = 'LiGuangyu'

import asyncio,re

patten = re.compile(r'(\w+)\((\d+)\)')


def getVName(dbName):
    dbName =dbName.lower();
    vname = ''

    for x in dbName.split('_'):
        vname += x.capitalize()
    gName = 'get' + vname
    sName = 'set' + vname
    vname = vname[0].lower() + vname[1:]
    return vname,gName,sName

def getTypeLength(s):
    m = patten.match(s)
    type = 'String'
    if m.group(1).upper() == 'NUMBER':
        type = 'Long'
    return type, m.group(2)

def buildDeclare(name, type):
    return "\tprivate %s %s;\n"%(type,name)

def buildGetter(name, gName,dbName, type, length):
    map={"name":name,"gName":gName,"dbName":dbName,"type":type,"length":length}
    pp = "\n\t@Column(name=\"%(dbName)s\",length=%(length)d )\n\tpublic %(type)s %(gName)s():{\n\t\treturn this.%(name)s;\n\t}\n" % map
    return pp

def buildSetter(name,sName,type):
    map = {"name":name,"type":type,"sName":sName}
    pp = "\n\tpublic %(sName)s ( %(type)s %(name)s) {\n\t\tthis.%(name)s=%(name)s;\n\t}\n" % map
    return pp


def parseLine(line):
    v = line.split('\t')
    a,b =v[0:2]
    type, length = getTypeLength(b)
    return a, type, int(length)


def main():
    declares = []
    getSeters = []
    with open('C:/Users/Guangyu/Desktop/新建文本文档 (4).txt') as f:
        for l in f.readlines():
            dbName,type,length = parseLine(l)
            vname, gName, sName = getVName(dbName)
            declares.append(buildDeclare(vname,type))
            getSeters.append(buildGetter(vname,gName,dbName,type,length))
            getSeters.append(buildSetter(vname,sName,type))
            pass
    for x in declares:
        print(x)
    for x in getSeters:
        print(x)

if __name__ =='__main__':
    main()
