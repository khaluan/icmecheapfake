from .summary import summary_text
import sys
sys.path.append('../Config')
from Config.config import *
from os.path import exists, join, isfile 
from os import listdir, remove, stat

def summary():
    filenames = [f for f in listdir(CONTEXT_DIR) if isfile(join(CONTEXT_DIR, f))]   
    for filename in filenames:
        try:
            with open(join(CONTEXT_DIR, filename), 'r', encoding='utf8') as file:
                content = eval(file.read())
            summary = summary_text(content['heading'] + content['context'])
            with open(join(CONTEXT_REFINED_DIR, filename), 'w+', encoding='utf8') as file:
                file.write(summary)
            
        except Exception as e:
            # print(e)
            # print(filename)
            pass