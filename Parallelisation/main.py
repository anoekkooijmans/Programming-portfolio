from Bio import Entrez

# the next two lines are needed to create an environment in which the 
# ssl doesn't complain about non-existing public keys...
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#enter your email here; the one you used to create an api key in step 0
Entrez.email = '' 

file = Entrez.elink(dbfrom="pubmed",
                   db="pmc",
                   LinkName="pubmed_pmc_refs",
                   id="30049270",
                   api_key='58de29bc3ae55149d8e95dbd417aa9a0d909')
results = Entrez.read(file)
print (results)

references = [f'{link["Id"]}' for link in results[0]["LinkSetDb"][0]["Link"]]
print (references)

handle = Entrez.efetch(db="pubmed",
                id='30049270',
                retmode="xml",
                api_key='58de29bc3ae55149d8e95dbd417aa9a0d909')
print(handle.read())