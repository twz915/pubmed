import unittest
from pubmed import PubMed


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


if __name__ == '__main__':
    print 'loading literature information...',
    pm = PubMed(22012762)
    print 'ok!'

    unittest.main()

