import re
import os
import json
from pathlib import Path
import text_processing

data = []

# Walk Dir
for root, dirs, files in os.walk("./second-brain"):
    for f in files:
        if f.endswith(".md"):
            file_path = os.path.join(root, f)
            try:
                markdown_file = open(file_path, "r")

                content = markdown_file.read()

                title = text_processing.get_title(content)
                url = text_processing.get_url(content)

                cleaned_content = text_processing.clean_text(content)

                

                item = {"title": title, "url": url, "content":content}

                data.append(item)
            except Exception as e:
                print(f'Error reading file: {file_path}. {str(e)}')




with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
