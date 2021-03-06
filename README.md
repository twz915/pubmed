`pubmed` is used to: 

1. Get literature information via PubMed ID, such as the author, title, journal_name, pub_date and so on.

2. Read csv file downloaded from pubmed search page.

![how to download pubmed search results](https://raw.githubusercontent.com/twz915/pubmed/master/docs/pubmed_results.png)


## Install
    pip install pubmed

## Usage
### Query Online
```python
from pubmed import PubMed
# http://www.ncbi.nlm.nih.gov/pubmed/26471457
pm = PubMed(26471457)

print pm.title
print pm.authors
print pm.pub_date
print pm.journal_name
print pm.journal_full_name

or

print pm.get_title()
print pm.get_authors()
print pm.get_pub_date()
print pm.get_journal_name()
print pm.get_journal_full_name()

or

print pm.getTitle()
print pm.getAuthors()
print pm.getPubDate()
print pm.getJournalName()
print pm.getJournalFullName()
```
### Read Download File
read csv files download from pubmed
```python
from pubmed import OpenCsv

f = OpenCsv('./pubmed_result.csv')

for p in f:
    print(p.title)
    print(p.authors)
    print(p.PMID)
```

demo

```
>>> pm = PubMed(26471457)
>>> pm.authors
['Tu W', 'Zhang H', 'Liu J', 'Hu QN']
>>> pm.title
'BioSynther: a customized biosynthetic potential explorer.'
>>> pm.pub_date
'2016 Feb 1'
>>> 
```
