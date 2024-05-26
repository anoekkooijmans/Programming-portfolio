from PubMedArticleDownloader import PubMedArticleDownloader
import logging

if __name__ == '__main__':
    # Initialize the PubMedArticleDownloader instance
    downloader = PubMedArticleDownloader(email='a.kooijmans@st.hanze.nl', api_key='58de29bc3ae55149d8e95dbd417aa9a0d909')
    
    logging.info("Starting the PubMed article downloader...")
    pubmed_id = '30049270'
    amount = 10
    downloader.download_articles(pubmed_id, amount, mode='parallel')
    downloader.download_articles(pubmed_id, amount, mode='sequential')
    logging.info("Script execution completed.")