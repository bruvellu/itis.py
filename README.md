itis.py
=======

Python library to access the web services of [ITIS database](http://www.itis.gov/).

Basic usage
-----------

    >>> from itis import Itis
    >>> itis = Itis()
    >>> results = itis.search_by_scientific_name('Priapulus caudatus')
    >>> print(results)
    (SvcScientificNameList){
       scientificNames[] = 
          (SvcScientificName){
             tsn = "155156"
             combinedName = "Priapulus caudatus"
             unitInd1 = None
             unitInd2 = None
             unitInd3 = None
             unitInd4 = None
             unitName1 = "Priapulus                          "
             unitName2 = "caudatus"
             unitName3 = None
             unitName4 = None
          },
     }
