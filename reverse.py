import json
import csv
import re 
import random
import json
import pickle
import time

import bs4
import colorama
import requests
from colorama import Back, Fore

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import *
import json
import re


qbank = open("questionbank.json", 'r')

data = json.load(qbank)
dic = data.items()
rdata = {}
#remove the examples from the dataset
for name, r in dic:
    r[0] = re.sub("Example\s\d+(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Note:(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Note that(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("For example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Example(.|\s)*$", '', str(r[0]))
    r[0] = re.sub("Follow up:(.|\s)*$", '', str(r[0]))
    r[0] = r[0].rstrip('\n')

    rest = r[1:]
    rest.insert(0, name)
    rdata[str(r[0])]= rest









with open('reverse.json', 'w') as f:
    f.seek(0)
    json.dump(rdata,f, indent=4)


qbank.close()
