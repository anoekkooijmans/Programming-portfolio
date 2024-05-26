from Bio import Entrez
import ssl
import multiprocessing as mp
import time
import logging

class PubMedArticleDownloader:
    def __init__(self, email, api_key):
        # Configure SSL settings to prevent certificate verification errors.
        ssl._create_default_https_context = ssl._create_unverified_context
        
        # Configure email and API key for Entrez.
        Entrez.email = email
        self.api_key = api_key
        
        # Set up logging configuration.
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    def download_article(self, pubmed_id, mode='parallel'):
        """Download a PubMed article."""
        try:
            handle = Entrez.efetch(db='pubmed', id=pubmed_id, retmode='xml', api_key=self.api_key)
            xml_data = handle.read()
            handle.close()

            file_name = f'{pubmed_id}.xml'
            with open(file_name, 'wb') as file:
                file.write(xml_data)

            logging.info(f'PubMed article {pubmed_id} successfully downloaded in {mode} mode.')
        except Exception as e:
            logging.error(f'Error occurred while downloading {pubmed_id}: {str(e)}')

    def get_references(self, pubmed_id, amount):
        """Retrieve references for a PubMed article."""
        try:
            file = Entrez.elink(dbfrom='pubmed', db='pmc', LinkName='pubmed_pmc_refs', id=pubmed_id, api_key=self.api_key)
            results = Entrez.read(file)
            file.close()
            references = [link['Id'] for link in results[0]['LinkSetDb'][0]['Link']]

            return references[:amount]
        except Exception as e:
            logging.error(f'Error occurred while retrieving references for {pubmed_id}: {str(e)}')
            return []

    def download_articles(self, pubmed_id, amount, mode='parallel'):
        """Download articles either in parallel or sequentially."""
        try:
            start_time = time.time()
            references = self.get_references(pubmed_id, amount)
            end_time = time.time()
            logging.info(f'Total time for getting references: {end_time - start_time}')

            start_time = time.time()
            if mode == 'parallel':
                with mp.Pool() as pool:
                    pool.map(self.download_article, references)
            else:
                for reference in references:
                    self.download_article(reference)
            end_time = time.time()
            logging.info(f'Total time for downloading articles in {mode} mode: {end_time - start_time}')
        except Exception as e:
            logging.error(f'Error occurred during {mode} downloading: {str(e)}')
