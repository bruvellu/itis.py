#!/usr/bin/env python

'''Client to access the web services of ITIS database (http://www.itis.gov/).

Usage:

    from itis import Itis
    itis = Itis()
    results = itis.search_by_scientific_name('Priapulus caudatus')
    print(results)

'''

from suds.client import Client
import logging

# Create logger.
logger = logging.getLogger('itis')
logger.setLevel(logging.DEBUG)
logger.propagate = False
formatter = logging.Formatter('[%(levelname)s] %(asctime)s @ %(module)s %(funcName)s (l%(lineno)d): %(message)s')

# Console handler for logger.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class Itis:
    '''Main ITIS interactor.'''
    def __init__(self):
        host = 'http://www.itis.gov/'
        wsdl_path = host + 'ITISWebService/services/ITISService?wsdl'

        logger.info('Initiating contact with ITIS...')

        try:
            self.client = Client(wsdl_path)
            logger.info('Connected to ITIS web services.')
        except:
            print('Could not connect to client!')

    def wire(self, service, query, attempt=0):
        '''Manage reconnections between client and ITIS.'''
        try:
            results = service(query)
        except:
            while attempt < 3:
                logger.warning('Could not connect... try=%d' % attempt)
                attempt += 1
                self.wire(service, query, attempt)
            logger.critical('Closing up the connection. I failed.')
            results = None
        return results

    def search_by_scientific_name(self, query, attempt=0):
        '''Search by scientific name.

        searchByScientificName:
        http://www.itis.gov/ws_searchApiDescription.html#SrchBySciName

        Output:

            results                     [main]
                .scientificNames        [list]
                    name                [object with scientific name]
                        .combinedName   [string with genus+sp]
                        .tsn            [entry tsn]

        '''
        logger.info('Searching for the scientific name "%s"', query)

        results = self.wire(
            self.client.service.searchByScientificName,
            query
            )
        return results

    def get_accepted_names_from_tsn(self, tsn):
        '''Get accepted names from TSN.

        getAcceptedNamesFromTSN:
        http://www.itis.gov/ws_tsnApiDescription.html#getAcceptedNames

        Output:

            results             [main]
                .acceptedNames  [list]
                .tsn            [entry tsn]

        '''
        logger.info('Retrieving accepted names from TSN=%s', tsn)

        results = self.wire(
            self.client.service.getAcceptedNamesFromTSN,
            tsn
            )
        return results

    def get_full_hierarchy_from_tsn(self, tsn):
        '''Get full hierarchy from TSN.

        getFullHierarchyFromTSN:
        http://www.itis.gov/ws_hierApiDescription.html#getFullHierarchy

        Output:

            results                 [main]
                .tsn                [entry tsn]
                .hierarchyList      [list]
                    node            [node object]
                        .parentName [name of parent node]
                        .parentTsn  [tsn of parent node]
                        .rankName   [node rank]
                        .taxonName  [node name]
                        .tsn        [node tsn]
        '''
        logger.info('Retrieving full hierarchy from TSN=%s', tsn)

        results = self.wire(
            self.client.service.getFullHierarchyFromTSN,
            tsn
            )
        return results


# Script version?
if __name__ == '__main__':
    print('Command line not yet implemented.')
