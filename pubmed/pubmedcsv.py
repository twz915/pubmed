# -*- coding: utf-8 -*-
# @Date    : 2016-01-07 15:19:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1

'''
read csv files download from pubmed


from pubmed import OpenCsv

f = OpenCsv('./pubmed_result.csv')

for p in f:
    print(p.title)
    print(p.authors)
    print(p.PMID)

'''

from csv import DictReader


class OpenCsv(object):
    def __init__(self, path):
        '''
        f = OpenCsv('./pubmed_result.csv')
        for p in f:
            print(p.title)
            print(p.authors)
            print(p.PMID)
        '''
        self.path = path

    def read(self):
        f = open(self.path)
        self.csv = DictReader(f)

    def __iter__(self):
        self.read()
        for entry in self.csv:
            yield _Paper(entry)


class _Paper(object):

    def __init__(self, entry):
        self.title = entry['Title']
        self.authors = entry['Description']
        self.PMID = entry['Identifiers'][len('PMID:'):]


def main():
    f = OpenCsv('./pubmed_result.csv')
    for p in f:
        print(p.title)
        print(p.authors)
        print(p.PMID)


if __name__ == '__main__':
    main()
