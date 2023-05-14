from bs4 import BeautifulSoup
import requests



def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')
    return len(citations_needed)

def get_citations_needed_report():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = soup.find_all(class_='noprint Inline-Template Template-Fact')

    citation_report = "The following citations are needed: \n\n"

    for citation in citations_needed:
        parent = citation.find_parent()
        citation_report += f"{parent.text.strip()}\n\n"

    return citation_report


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Bird"
    count = get_citations_needed_count(url)
    report = get_citations_needed_report()
    print('Number of citations needed:', count)
    print(report)


