#!/usr/bin/env python

'''Client to access the web services of ITIS database (http://www.itis.gov/).

Usage:

    from itis import Itis
    itis = Itis()
    results = itis.search_by_scientific_name('Genus name')
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

# Cria o manipulador do arquivo.log.
#file_handler = logging.FileHandler('logs/itis.log')
#file_handler.setLevel(logging.DEBUG)
#file_handler.setFormatter(formatter)
#logger.addHandler(file_handler)


class Itis:
    '''Main ITIS interactor.'''
    def __init__(self):
        self.url = 'http://www.itis.gov/ITISWebService.xml'

        logger.info('Initiating contact with ITIS...')

        try:
            self.client = Client(self.url)
            logger.info('Connected to ITIS web services.')
        except:
            print('Could not connect to client!')

    def search_by_scientific_name(self, query, attempt=0):
        '''Search by scientific name.

        searchByScientificName:
        http://www.itis.gov/ws_searchApiDescription.html#SrchBySciName

        '''

        logger.info('Search ITIS for: %s', query)

        try:
            results = self.client.service.searchByScientificName(query)
        except:
            while attempt < 3:
                logger.warning('Could not connect... try=%d' % attempt)
                attempt += 1
                self.search_by_scientific_name(query, attempt)
            logger.critical('Closing up the connection. I failed.')
            results = None
        return results

    def get_accepted_names_from_tsn(self, tsn):
        '''Get accepted names from TSN.'''
        try:
            response = self.client.service.getAcceptedNamesFromTSN(tsn)
        except:
            logger.warning('Connection problem %d', tsn)
            response = None
        return response

    def get_full_hierarchy(self, tsn):
        '''Get full hierarchy.

        Uses: http://www.itis.gov/ws_hierApiDescription.html#getFullHierarchy

        http://www.itis.gov/ITISWebService/services/ITISService/getFullHierarchyFromTSN?tsn=1378

        '''

        logger.info('Getting hierarchy...')

        try:
            hierarchy = self.client.service.getFullHierarchyFromTSN(tsn)
        except:
            logger.warning('Error pulling hierarchy %s, connection problem', tsn)
            hierarchy = None
        return hierarchy

# Script version?
if __name__ == '__main__':
    print('Command line not yet implemented.')
