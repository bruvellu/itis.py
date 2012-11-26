itis.py
=======

Python library to access the web services of [ITIS database](http://www.itis.gov/).

Basic usage:

    from itis import Itis
    itis = Itis()
    results = itis.search_by_scientific_name('Genus name')
    print(results)
