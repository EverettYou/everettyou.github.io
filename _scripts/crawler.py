from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import json
import re
import yaml
from pathlib import Path
from pypinyin import lazy_pinyin

class ScholarCrawler:
    ''' Crawler for Google Scholar
        Args:
            scholar_id: str, scholar id
            hl (optional): str, language
            sortby (optional): str, sort by: "pubdate", "citations"
    '''
    def __init__(self, scholar_id, hl="en", sortby="pubdate"):
        self.scholar_id = scholar_id
        self.hl = hl
        self.sortby = sortby
        self.driver = None
        self.data = {}

    @property
    def url(self):
        return f"https://scholar.google.com/citations?user={self.scholar_id}&hl={self.hl}&sortby={self.sortby}"
        
    def setup_driver(self):
        '''Initialize the Chrome WebDriver with appropriate options'''
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox') # Required for running in some environments
        options.add_argument('--disable-dev-shm-usage') # Overcome limited resource problems
        options.add_argument("--disable-blink-features=AutomationControlled") # Prevent detection as a bot
        # Add custom headers through user agent, to mimic a real browser
        # (Visit https://www.google.com/search?q=my+browser+user+agent to inspect your browser's user agent)
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36')
        self.driver = webdriver.Chrome(options=options)
        return self.driver
            
    def _load_all_publications(self):
        '''Click "Show More" until all publications are loaded'''
        try:
            show_more = self.driver.find_element(By.ID, "gsc_bpf_more")
            print("Loading all publications...")
            print(f"  Displayed publications: {self._count_publications()}")
            while show_more.is_enabled():
                show_more.click()
                time.sleep(0.5)
                print(f"  Displayed publications: {self._count_publications()}")
        except NoSuchElementException:
            pass
        
    def _count_publications(self):
        '''Count the number of publications'''
        return len(self.driver.find_elements(By.CLASS_NAME, "gsc_a_tr"))
    
    def _view_all(self):
        '''Click "View all" button'''
        try:
            view_all = self.driver.find_element(By.ID, "gsc_hist_opn")
            view_all.click()
            time.sleep(0.5)
        except NoSuchElementException:
            pass
    
    def get_scholar_data(self):
        '''Get scholar data'''
        self.driver.get(self.url)
        self._load_all_publications()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "gsc_prf_in")))
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        print("Extracting scholar profile...")
        # Find the name
        name_div = soup.find('div', id='gsc_prf_in')
        self.data['name'] = name_div.text.strip() if name_div else None
        # Find the affiliation
        affiliation_div = soup.find('div', class_='gsc_prf_il')
        self.data['affiliation'] = affiliation_div.text.strip() if affiliation_div else None
        # Find research interests
        interests_div = soup.find('div', id='gsc_prf_int')
        self.data['research_interests'] = [interest.text.strip() for interest in interests_div.find_all('a')] if interests_div else []
        print("Extracting citation metrics...")
        # Find the table with metrics
        metrics_table = soup.find('table', id='gsc_rsb_st')
        self.data['citation_metrics'] = {}
        if metrics_table:
            # Get all rows in the table
            rows = metrics_table.find_all('tr')
            # Process each row
            for row in rows:
                # Get the metric name (first cell)
                metric_name = row.find('td', class_='gsc_rsb_sc1')
                if metric_name:
                    metric_name = metric_name.text.strip()
                    
                    # Get the values (second and third cells)
                    values = row.find_all('td', class_='gsc_rsb_std')
                    if len(values) >= 2:
                        all_time = values[0].text.strip()
                        since_2020 = values[1].text.strip()
                        self.data['citation_metrics'][metric_name] = {
                            'all_time': all_time,
                            'since_2020': since_2020
                        }
        # Extract citation histogram
        hist = soup.find('div', class_='gsc_md_hist_b')
        year_spans =hist.find_all('span', class_='gsc_g_t')
        citation_bars = hist.find_all('a', class_='gsc_g_a')
        self.data['citation_histogram'] = {}
        for year_span, citation_bar in zip(year_spans, citation_bars):
            year = year_span.text.strip()
            citation = citation_bar.text.strip()
            self.data['citation_histogram'][year] = citation
        # Extract publication data
        self.data['publications'] = []
        print("Extracting publication data...")
        pubs = soup.find_all('tr', class_='gsc_a_tr')
        for id, pub in enumerate(pubs):
            title = pub.find('a', class_='gsc_a_at')
            for svg in title.find_all('svg', class_='gs_fsvg'):
                label = svg.get('aria-label', '')
                svg.replace_with(label)
            authors_div = pub.find('div', class_='gs_gray')
            journal_div = pub.find_all('div', class_='gs_gray')[1]
            citations = pub.find('a', class_='gsc_a_ac')
            year = pub.find('span', class_='gsc_a_h')
            url = "https://scholar.google.com" + title['href'] if title else None
            # construct publication data
            data = {
                'title': title.text if title else None,
                'authors': [author.strip() for author in authors_div.text.split(",")] if authors_div else [] ,
                'journal': journal_div.text if journal_div else None,
                'citations': citations.text if citations else None,
                'year': year.text if year else None,
                'url': url
            }
            # if url is provided, visit the page to get more data
            if url:
                pub_data = self.get_publication_data(url)
                data.update(pub_data)
            print(f"  [{id+1}] {data['publication_date'] if 'publication_date' in data else data['year']}: {data['title']}")
            self.data['publications'].append(data)
            if (id + 1) % 10 == 0:
                time.sleep(2)
                self.save_data("_scripts/data/publications.json")
        self.save_data("_scripts/data/publications.json")
        print(f"{len(self.data['publications'])} publications extracted.")

    def _extract_pdf_link(self, soup):
        container = soup.find(id="gsc_oci_title_gg")
        if not container:
            return None
        links = container.find_all("a")
        for link in links:
            # Priority 1: [PDF] label
            if link.find("span", class_="gsc_vcd_title_ggt") and "[PDF]" in link.text:
                return link['href']
            # Priority 2: ends with pdf
            if link['href'].lower().endswith('pdf'):
                return link['href']
            # Priority 3: "Get it at UC"
            if "Get it at UC" in link.text:
                uc_url = link['href']
                self.driver.get(uc_url)
                try:
                    pdf_link = self.driver.find_element(By.CLASS_NAME, "browzine-direct-to-pdf-link")
                    return pdf_link.get_attribute("href")
                except:
                    return None
        return None
    
    def get_publication_data(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "gsc_oci_table")))
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        table = soup.find("div", id="gsc_oci_table")
        data = {}
        for item in table.find_all("div", class_="gs_scl"):
            field = item.find("div", class_="gsc_oci_field")
            value = item.find("div", class_="gsc_oci_value")
            if not field or not value:
                continue
            key = field.get_text(strip=True)
            if key == "Scholar articles":
                articles = []
                for snippet in value.find_all("div", class_="gsc_oci_merged_snippet"):
                    parts = snippet.find_all("div")
                    if not parts:
                        continue
                    title_link = parts[0].find("a")
                    title = title_link.get_text(strip=True) if title_link else ""
                    title_url = title_link['href'] if title_link else ""
                    authors_journal = parts[1].get_text(strip=True) if len(parts) > 1 else ""
                    if "-" in authors_journal:
                        authors = authors_journal.split("-")[0].strip()
                        journal = authors_journal.split("-")[1].strip()
                    else:
                        authors = authors_journal.strip()
                        journal = ""
                    more_info = {a.get_text(strip=True): a['href'] for a in parts[2].find_all("a")} if len(parts) > 2 else {}
                    articles.append({
                        "title": title,
                        "url": "https://scholar.google.com" + title_url,
                        "authors": [author.strip() for author in authors.split(",")],
                        "journal": journal,
                        "more_info": more_info
                    })
                data['articles'] = articles
            elif key == "Total citations":
                citation_text = value.find("a").get_text(strip=True) if value.find("a") else value.get_text(strip=True)
                data['citations'] = citation_text.split()[-1]
            elif key == "Description":
                data['description'] = value.get_text(separator=" ", strip=True)
            elif key == "Authors":
                data['authors'] = [author.strip() for author in re.split(r'[,;，]+', value.get_text(strip=True))]
            else:
                data[key.lower().replace(" ", "_")] = value.get_text(strip=True)
        return data
    
    def crawl(self):
        '''Main method to crawl the scholar profile'''
        try:
            self.setup_driver()
            self.get_scholar_data()
        finally:
            if self.driver:
                self.driver.quit()

    def save_data(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def load_data(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
        return self.data
    
class PublicationFormatter:
    def __init__(self, data):
        self.data = data
    
    def _is_chinese(self, text):
        """Check if text contains Chinese characters"""
        return any('\u4e00' <= char <= '\u9fff' for char in text)
    
    def _chinese_to_pinyin(self, text):
        """Convert Chinese text to pinyin"""
        if self._is_chinese(text):
            return ''.join(lazy_pinyin(text))
        return text

    def _cite_key(self, publication):
        first_author = publication['authors'][0]
        last_name = first_author.split(' ')[-1].strip().lower()
        last_name = self._chinese_to_pinyin(last_name)
        year = publication['year']
        title_words = publication['title'].split()
        title_code = ''.join([word[0] for word in title_words[:5]]).lower()
        title_code = self._chinese_to_pinyin(title_code)
        return f'{last_name}{year}{title_code}'
    
    def _extract_doi_from_text(self, text):
        """Extract DOI from text if present"""
        if not text:
            return None
        # Match DOI pattern: 10.xxxx/xxxxx (stop at common delimiters)
        doi_match = re.search(r'10\.\d+/[^\s,\];\)]+', text)
        if doi_match:
            return doi_match.group(0).rstrip('];)')
        return None

    def _extract_arxiv_id(self, text):
        """Extract arXiv ID from text"""
        if not text:
            return None
        arxiv_match = re.search(r'arXiv:(\d+\.\d+)', text, re.IGNORECASE)
        if arxiv_match:
            return f"https://arxiv.org/abs/{arxiv_match.group(1)}"
        return None

    def _determine_type(self, journal_text):
        """Determine publication type from journal name"""
        if not journal_text:
            return 'preprint'
        
        journal_lower = journal_text.lower()
        
        if 'arxiv' in journal_lower or 'preprint' in journal_lower:
            return 'preprint'
        elif 'conference' in journal_lower or 'proceedings' in journal_lower:
            return 'conference-paper'
        else:
            return 'journal-article'

    def _parse_authors_for_yaml(self, authors_list):
        """Convert author list to YAML format"""
        result = []
        for author in authors_list:
            result.append({
                'name': author
            })
        return result

    def _format(self, publication, style='biobib'):
        # Initialize format-specific dictionaries
        if style == 'bibtex':
            bib_info = dict()
        elif style == 'yaml':
            yaml_pub = dict()
            # Generate ID from cite_key (which already includes year)
            cite_key = self._cite_key(publication)
            yaml_pub['id'] = cite_key
            # Clean title - replace newlines with spaces and strip
            title = publication.get('title', '')
            if isinstance(title, str):
                title = title.replace('\n', ' ').replace('\r', ' ').strip()
            yaml_pub['title'] = title
        
        # Format authors: "Last, F.-M." for each author
        formatted_authors = []
        if style == 'yaml':
            yaml_pub['authors'] = self._parse_authors_for_yaml(publication.get('authors', []))
        elif style == 'biobib':
            for author in publication['authors']:
                parts = author.split(' ')
                last = parts[-1]
                initials = []
                for p in parts[:-1]:
                    # Handle hyphenated first names, e.g., "Guang-Yu" -> "G.-Y."
                    if '-' in p:
                        sub_initials = [sub[0] + '.' for sub in p.split('-')]
                        initials.append('-'.join(sub_initials))
                    else:
                        initials.append(p[0] + '.')
                if initials:
                    initials_str = ''.join(initials)
                    formatted_authors.append(f"{last}, {initials_str}")
                else:
                    formatted_authors.append(f"{last}")
            if len(publication['authors']) > 1:
                formatted_authors[-1] = 'and ' + formatted_authors[-1]
            authors_str = ', '.join(formatted_authors)
        elif style == 'cv':
            authors_str = ', '.join(publication['authors'])
        elif style == 'bibtex':
            for author in publication['authors']:
                parts = author.split(' ')
                last = parts[-1]
                most = ' '.join(parts[0:-1]).strip()
                if most:
                    formatted_authors.append(f'{{{last}}}, {most}')
                else:
                    formatted_authors.append(f'{{{last}}}')
            bib_info['author'] = ' and '.join(formatted_authors)
        elif style == 'medline':
            for author in publication['authors']:
                # Format as "Last,First" (no space after comma)
                parts = author.split(' ')
                if len(parts) >= 2:
                    last = parts[-1]
                    first = ' '.join(parts[:-1])
                    formatted_authors.append(f"{last},{first}")
                else:
                    formatted_authors.append(author)
        # Compose the citation string (no journal abbreviation)
        title = publication['title']
        title = re.sub(r"<\?.*?\?>", "", title)
        if style == 'bibtex':
            bib_info['title'] = '{' + title + '}'
        if 'source' in publication:
            source = publication['source']
        else:
            source = publication['journal']
        source = title_case(source)
        
        # Extract info for YAML
        if style == 'yaml':
            journal = publication.get('journal', '')
            if journal:
                pub_type = self._determine_type(journal)
                yaml_pub['type'] = pub_type
            else:
                yaml_pub['type'] = 'preprint'
            
            # Extract DOI from journal or description
            doi = self._extract_doi_from_text(journal)
            if not doi and publication.get('description'):
                doi = self._extract_doi_from_text(publication['description'])
            if doi:
                yaml_pub['doi'] = doi
            
            # Extract URL (arXiv or other)
            url = self._extract_arxiv_id(journal)
            if not url and publication.get('url'):
                url = publication['url']
            if url:
                yaml_pub['url'] = url
            
            # Add abstract/description
            if publication.get('description'):
                yaml_pub['abstract'] = publication['description']
        
        if style == 'bibtex':
            bib_info['journal'] = source
        other = ''
        if 'volume' in publication:
            if style == 'biobib':
                other += f' {publication['volume']}'
            elif style == 'cv':
                other += f' **{publication['volume']}**'
            elif style == 'bibtex':
                bib_info['volume'] = publication['volume']
        if 'issue' in publication:
            other += f' ({publication['issue']})'
            if style == 'bibtex':
                bib_info['number'] = publication['issue']
        if 'pages' in publication:
            other += f', {publication['pages']}'
            if style == 'bibtex':
                bib_info['pages'] = publication['pages']
        if 'year' in publication:
            other += f' ({publication['year']})'
            if style == 'bibtex':
                bib_info['year'] = publication['year']
            elif style == 'yaml':
                yaml_pub['year'] = int(publication['year']) if publication['year'] else 0
        if other:
            if '—' in source:
                source = source.split('—')[0].strip()
            if 'Conference' in source or 'Symposium' in source or 'Workshop' in source:
                source = source.split(',')[0].strip()
            source += other
        
        # Record source for YAML (after all processing)
        if style == 'yaml':
            yaml_pub['journal'] = source
        
        # Return formatted output based on style
        if style == 'yaml':
            # Remove None values and return dict
            yaml_pub = {k: v for k, v in yaml_pub.items() if v is not None and v != ''}
            return yaml_pub
        elif style == 'biobib':
            formatted = f'{authors_str}, "{title}", {source}.'
        elif style == 'cv':
            formatted = f'{authors_str}. *{title}*. {source}.'
        elif style == 'bibtex':
            formatted = '@article{' + f'{self._cite_key(publication)},\n'
            for key, val in bib_info.items():
                if val:
                    formatted += f'\t{key} = {{{val}}},\n'
            formatted = formatted[:-2] + '}'
        elif style == 'medline':
            # MEDLINE format
            formatted = f"TI  - {title}\n"
            formatted += f"DP  - {publication['year']}\n"
            
            # Add authors
            for author in formatted_authors:
                formatted += f"AU  - {author},\n"
            
            # Add other fields if available
            if 'pages' in publication:
                formatted += f"PG  - {publication['pages']}\n"
            
            formatted += f"TA  - {source}\n"
            
            if 'volume' in publication:
                formatted += f"VI  - {publication['volume']}\n"
            
            if 'issue' in publication:
                formatted += f"IP  - {publication['issue']}\n"
            
            if 'doi' in publication:
                formatted += f"DO  - {publication['doi']}\n"
        
        return formatted
    
    def _classify(self, publication):
        if 'source' in publication:
            source = publication['source']
        else:
            source = publication['journal']
        source_lower = source.lower()
        # Define classification rules
        preprint_keywords = ['arxiv']
        review_keywords = ['symmetry']
        book_chap_keywords = ['iron-based', 'festschrift']
        if any(keyword in source_lower for keyword in preprint_keywords):
            return 'preprint'
        elif any(keyword in source_lower for keyword in review_keywords):
            return 'review'
        elif any(keyword in source_lower for keyword in book_chap_keywords):
            return 'book_chap'
        else:
            return 'article'
        
    def export_publications(self, filename, style='biobib'):
        """Export publications to a file in the specified format"""
        # Determine file extension based on style
        style_extensions = {
            'biobib': '.md',
            'cv': '.md',
            'bibtex': '.bib',
            'medline': '.medline',
            'yaml': '.yml'
        }
        
        ext = style_extensions.get(style, '.txt')
        
        # Ensure filename has correct extension
        filepath = Path(filename)
        if filepath.suffix != ext:
            filepath = filepath.with_suffix(ext)
        
        # Create parent directory if needed
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            if style == 'yaml':
                # Export as YAML using _format method
                publications = []
                for pub in self.data['publications']:
                    try:
                        yaml_pub = self._format(pub, style='yaml')
                        publications.append(yaml_pub)
                    except Exception as e:
                        print(f"Error converting publication '{pub.get('title', 'Unknown')}': {e}")
                        continue
                
                # Sort by year (newest first)
                publications.sort(key=lambda x: x.get('year', 0), reverse=True)
                
                # Write YAML header
                header = """# Publications data file
# Structure based on PRISM PublicationsList component
# Each publication should have:
# - id: unique identifier
# - title: publication title
# - authors: array of author objects with name
# - year: publication year
# - type: publication type (journal-article, conference-paper, preprint, etc.)
# - journal: journal name (optional, for journal articles)
# - conference: conference name (optional, for conference papers)
# - doi: DOI identifier (optional)
# - code: link to code repository (optional)
# - abstract: abstract text (optional)
# - bibtex: BibTeX entry (optional)
# - description: short description (optional)
# - preview: image filename for preview (optional, should be in /assets/img/papers/)

"""
                f.write(header)
                yaml.dump(publications, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
                print(f"Exported {len(publications)} publications to {filepath}")
                
            elif style == 'biobib':
                classified_bibs = {'article': [], 'review': [], 'book_chap': [], 'preprint': []}
                for publication in reversed(self.data['publications']):
                    classification = self._classify(publication)
                    classified_bibs[classification].append(self._format(publication, style))
                for classification in classified_bibs:
                    f.write(f"{classification}: {len(classified_bibs[classification])}\n")
                    id = 1  
                    for bib in classified_bibs[classification]:
                        f.write(f"  {id:>3}. {bib}\n")
                        id += 1
                print(f"Exported publications to {filepath}")
                
            elif style == 'cv':
                classified_bibs = {'Articles': [], 'Preprints': []}
                for publication in self.data['publications']:
                    classification = self._classify(publication)
                    formatted = self._format(publication, style)
                    if classification == 'preprint':
                        classified_bibs['Preprints'].append(formatted)
                    else:
                        classified_bibs['Articles'].append(formatted)
                for classification in classified_bibs:
                    f.write(f"### {classification}:\n")
                    id = 1  
                    for bib in classified_bibs[classification]:
                        f.write(f"  {id}. {bib}\n")
                        id += 1
                print(f"Exported publications to {filepath}")
                
            elif style == 'bibtex':
                for publication in self.data['publications']:
                    f.write(self._format(publication, style) + "\n\n")
                print(f"Exported publications to {filepath}")
                
            elif style == 'medline':
                for publication in self.data['publications']:
                    f.write(self._format(publication, style) + "\n\n")
                print(f"Exported publications to {filepath}")

def title_case(text):
    # List of prepositions and other words to keep lowercase
    lowercase_words = {
        'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 
        'to', 'from', 'by', 'with', 'in', 'of', 'as', 'per', 'via', 'vs',
        'versus', 'et', 'al', 'de', 'la', 'le', 'les', 'du', 'des'
    }
    
    # Split the text into words
    words = text.split()
    
   # Process each word
    processed_words = []
    for i, word in enumerate(words):
        if re.match(r'^arxiv:\d+\.\d+$', word.lower()):
            processed_words.append('arXiv:' + word[6:])
        elif i == 0:
            processed_words.append(word[0].upper() + word[1:])
        elif word.lower() in lowercase_words:
            processed_words.append(word.lower())
        else:
            processed_words.append(word[0].upper() + word[1:])
    
    # Join the words back together
    return ' '.join(processed_words)


def main():
    """Main function to run the crawler and export to YAML"""
    crawler = ScholarCrawler("PLFbeHMAAAAJ")
    crawler.crawl()
    crawler.save_data('_scripts/data/publications.json')
    print(f"\nData saved to _scripts/data/publications.json")
    
    # Export to YAML
    print("\nExporting to YAML format...")
    formatter = PublicationFormatter(crawler.data)
    formatter.export_publications('_data/publications.yml', style='yaml')
    print(f"YAML exported to _data/publications.yml")
    print("Done!")


if __name__ == '__main__':
    main()

