import re
import yake
from nltk.corpus import stopwords

import re

def clean_text(text):
    # Remove "Created Time:"
    text = re.sub(r'^Created time:.*$', '', text, flags=re.MULTILINE)
    
    # Remove "URL:"
    text = re.sub(r'^URL:.*$', '', text, flags=re.MULTILINE)
    
    # Remove headings (#)
    text = re.sub(r'#+ ', '', text)
    
    # Remove other characters (*,``)
    text = re.sub(r'[*`_]', '', text)
    
    # Remove extra newlines
    text = re.sub(r'\n\s*\n', '\n', text)

    # Remove links
    text = re.sub(r'\[.*?\]\(.*?\)\s*', '', text, flags=re.MULTILINE)

    # Remove images
    text = re.sub(r'!\[.*?\]\(.*?\)\s*', '', text, flags=re.MULTILINE)

    # Remove links
    # pattern = re.compile(r'!\[.*?\]\(.*?\)|\[\w.*?\]\(.*?\)', re.DOTALL)
    # text = re.sub(pattern, '', text)
    # text = re.sub('\n{2,}', '\n', text).strip()
    
    
    return text


def extract_keywords(text):
    keyword_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9)
    keywords = keyword_extractor.extract_keywords(text)
    return keywords

def get_title(text):
    title_match = re.search(r'^#+\s*(.+)$', text, re.MULTILINE)
    return title_match.group(1).strip() if title_match else None

def get_url(text):
    url_match = re.search(r'^\s*URL:\s*(.+)$', text, re.MULTILINE)
    return url_match.group(1).strip() if url_match else None
    

def clean_title(text):
    text_no_parenthesis = re.sub(r'^\(\d+\)\s*', '', text)
    print(text_no_parenthesis)
