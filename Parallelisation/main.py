from PubMedArticleDownloader import PubMedArticleDownloader
import logging

if __name__ == '__main__':
    # Initialize the PubMedArticleDownloader instance
    # Je moet niet je credentials in je repo zetten. Maak gebruik van 
    # args of van omgevingsvariabelen.
    downloader = PubMedArticleDownloader(email='a.kooijmans@st.hanze.nl', api_key='58de29bc3ae55149d8e95dbd417aa9a0d909')
    
    logging.info("Starting the PubMed article downloader...")
    pubmed_id = '30049270'
    amount = 10
    downloader.download_articles(pubmed_id, amount, mode='parallel')
    downloader.download_articles(pubmed_id, amount, mode='sequential')
    # Zou fijn zijn wanneer je hier nog de processortijd bij had gezet, maar soit.
    logging.info("Script execution completed.")