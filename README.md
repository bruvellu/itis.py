itis.py
=======

Python library to access the web services of [ITIS database](http://www.itis.gov/).

Dependencies
------------

* [pip](http://www.pip-installer.org/en/latest/installing.html "Pip installation guide") - If you don't have pip installed, follow the link.

Setup
-----

```bash
pip install -r requirements.txt
```


Basic usage
-----------

```bash
./bin/itis-cli.py -s Malus

(SvcScientificNameList){
   scientificNames[] = 
      (SvcScientificName){
         tsn = "504851"
         author = "L."
         combinedName = "Rubus fruticosus"
         kingdom = "Plantae"
         unitInd1 = None
         unitInd2 = None
         unitInd3 = None
         unitInd4 = None
         unitName1 = "Rubus"
         unitName2 = "fruticosus"
         unitName3 = None
         unitName4 = None
      },
 }
```
