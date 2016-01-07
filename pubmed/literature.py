# -*- coding: utf-8 -*-
# @Date    : 2015-01-15 14:22:54
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1
'''
Get literature information via PubMed id
'''
from __future__ import unicode_literals

from urllib2 import urlopen
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as BS


class PubMed(object):
    '''
    PMID is pubmed id: such as 22012762
    '''

    def __init__(self, PMID=''):
        self.PMID = str(PMID)
        self.url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={ids}'.format(
            ids=self.PMID)
        # use bs to standardize the xml content
        self.xml = pq(str(BS(urlopen(self.url).read())))

        # add attr for instance
        # such as: pm.title, pm.authors and pm.getTitle(), pm.getAuthors()
        PubMed_funs = filter(lambda x: not x.startswith(
            '_'), PubMed.__dict__.keys())
        for fname in PubMed_funs:
            setattr(self, fname.replace('get_', '', 1), getattr(self, fname)())
            parts = fname.split('_')
            new_fname = parts[0] + ''.join([p.title() for p in parts[1:]])
            setattr(self, new_fname, getattr(self, fname))

    def __get(self, name):
        return self.xml('[name="%s"]' % name)

    def get_authors(self):
        return [author_label.text for author_label in self.__get('Author')]

    def get_title(self):
        return self.__get('Title').text()

    def get_pub_date(self):
        return self.__get('PubDate').text()

    def get_journal_name(self):
        return self.__get('Source').text()

    def get_journal_full_name(self):
        return self.__get('FullJournalName').text()


if __name__ == '__main__':
    import unittest
    print 'loading literature information...',
    pm = PubMed(22012762)
    print 'ok!\nreading...'

    class TestPubMed(unittest.TestCase):

        def test_get_title(self):
            self.assertTrue('Biosynthesis of isoprene units' in pm.get_title())

        def test_get_authors(self):
            self.assertTrue('Ahrens-Botzong A' in pm.get_authors())

        def test_get_pub_date(self):
            self.assertEqual('2011 Dec 9', pm.get_pub_date())

        def test_get_journal_name(self):
            self.assertEqual('Angew Chem Int Ed Engl', pm.get_journal_name())

        def test_get_journal_full_name(self):
            self.assertEqual('Angewandte Chemie (International ed. in English)',
                             pm.get_journal_full_name())

    unittest.main()
