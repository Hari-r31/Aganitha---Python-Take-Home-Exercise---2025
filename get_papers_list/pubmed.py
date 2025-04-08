# get_papers_list/pubmed.py

import requests
from typing import List, Dict
from bs4 import BeautifulSoup
from get_papers_list.filters import is_non_academic

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    # Step 1: Search PubMed IDs
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10}
    r = requests.get(search_url, params=search_params)
    ids = r.json()["esearchresult"]["idlist"]

    if debug:
        print(f"Found IDs: {ids}")

    # Step 2: Fetch details
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    r = requests.get(fetch_url, params=fetch_params)
    soup = BeautifulSoup(r.text, "xml")
    papers = []

    for article in soup.find_all("PubmedArticle"):
        pmid = article.PMID.text
        title = article.ArticleTitle.text
        pub_date = article.PubDate.Year.text if article.PubDate else "Unknown"
        authors = article.find_all("Author")
        
        non_academic_authors = []
        company_affiliations = []
        email = None

        for author in authors:
            affiliation = author.find("Affiliation")
            if affiliation and is_non_academic(affiliation.text):
                last = author.LastName.text if author.LastName else ""
                first = author.ForeName.text if author.ForeName else ""
                non_academic_authors.append(f"{first} {last}")
                company_affiliations.append(affiliation.text)
                if "@" in affiliation.text and not email:
                    email = affiliation.text.split()[-1]

        if non_academic_authors:
            papers.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": email or "N/A"
            })

    return papers
