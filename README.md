Get literature information via PubMed ID, such as the author, title, journal_name, pub_date and so on.

## Install
    pip install pubchem

## Usage
    from pubmed import PubMed
    # http://www.ncbi.nlm.nih.gov/pubmed/24622768
    pm = PubMed(24622768)

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
