__author__ = 'LiGuangyu'

import asyncio,re

patten = re.compile(r'(\w+)\((\d+)(,\d+)?\)')
sList = []

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
    length = m.group(2)
    if m.group(3):
        type = 'Double'
    elif m.group(1).upper() == 'NUMBER':
        # if length ==16:
        #     type='BigDecimal'
        type = 'Long'
    return type, m.group(2)

def buildDeclare(name, type,comm):
    rev = "\tprivate %s %s;"%(type,name)
    if comm:
        rev += "\t//" + comm
    rev += '\n'
    return rev

def buildGetter(name, gName,dbName, type, length):
    nn = dbName.upper()
    sList.append(nn)
    map={"name":name,"gName":gName,"dbName":nn,"type":type,"length":length}
    pp = "\n\t@Column(name=\"%(dbName)s\",length=%(length)d )\n\tpublic %(type)s %(gName)s(){\n\t\treturn this.%(name)s;\n\t}\n" % map
    return pp

def buildSetter(name,sName,type):
    map = {"name":name,"type":type,"sName":sName}
    pp = "\n\tpublic void %(sName)s ( %(type)s %(name)s) {\n\t\tthis.%(name)s=%(name)s;\n\t}\n" % map
    return pp


def parseLine(line):
    v = line.split('\t')
    a,b =v[0:2]
    comm = v[4].strip() if (len(v) > 3) else None
    type, length = getTypeLength(b)
    return a, type, int(length), comm


def main():
    declares = []
    getSeters = []
    with open('D:/nbweb/topTransDtl - 副本.txt') as f:
        for l in f.readlines():
            if(len(l) > 0):
                dbName,type,length,comm = parseLine(l)
                vname, gName, sName = getVName(dbName)
                declares.append(buildDeclare(vname,type,comm))
                getSeters.append(buildGetter(vname,gName,dbName,type,length))
                getSeters.append(buildSetter(vname,sName,type))
            pass
    with open('D:/nbweb/test2.txt','w') as of:
        for x in declares:
            of.write(x)
        for x in getSeters:
            of.write(x)

if __name__ =='__main__':
    main()
    print(','.join(sList))
