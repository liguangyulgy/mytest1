import os,glob

outFileName = 'C:/Users/Guangyu/Downloads/铁汉娇娃/铁汉娇娃.txt'
dirPath = 'C:/Users/Guangyu/Downloads/铁汉娇娃/铁汉娇娃/*'

def write(fn,of):
    with open(fn,'rb') as inf:
        of.write(inf.read())
    pass

def main():
    with open(outFileName,'ab+') as of:
        print(glob.glob(dirPath))
        for fileName in glob.glob(dirPath):
            write(fileName,of)

if __name__ == '__main__':
    main()