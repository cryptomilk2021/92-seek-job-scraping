import requests
from bs4 import BeautifulSoup, SoupStrainer
import time
import random

site_root = 'https://www.seek.com.au'
no_no_jobs = ['SALE', 'RECEPTIONIST', 'RETAIL', 'COLES', 'SALES', 'JUNIOR', 'NURSE', 'BAR', 'NURSES', 'MEDICAL',
              'SECURITY', 'ADMIN', 'PHYSIOTHERAPIST', 'OCCUPATIONAL', 'ENROLLED', 'TRAINEE', 'TABLELANDS', 'PODIATRIST',
              'CARER', 'MASSAGE', 'THERAPIST', 'TOWNSVILLE', 'CHEF', 'BEAUTY', 'PATHOLOGIST', 'THERAPIST', 'BAR',
              'AGED', 'RECEPTION', 'MAREEBA', 'CONSTRUCTION', 'BEVERAGE', 'LIBRARY', 'PHARMACY', 'ATTENDANT',
              'HOSPITALITY', 'CLEANER', 'HOUSEKEEPING', 'CASINO', 'BARISTA', 'LINGERIE', 'MEDICAL', 'RETAIL',
              'MERCHANDISER', 'MERCHANDISERS']

job_title_list = []
job_title_minor_list = []
job_link_list = []
#START loop
for page in range(1, 2):
    response = requests.get(f"https://www.seek.com.au/part-time-casual-jobs/in-Cairns-&-Far-North-QLD?page={page}")
    n = response.text

    soup = BeautifulSoup(n, "html.parser")

    mydivs = soup.find_all('a', class_="_1tmgvw5 _1tmgvw8 _1tmgvwb _1tmgvwc _1tmgvwf yvsb870 yvsb87f _14uh994h")

    for div in mydivs:
        job_title_list.append(div.getText())
        job_link_list.append(site_root + str(div['href']))

    mydivs = soup.find_all('a', class_="l2mi890")
    for div in mydivs:
        job_title_minor_list.append(div.getText())

    new_list = []
    for i in range(len(job_title_list)):
        split_list = job_title_list[i].replace('/', ' ').replace('-', ' ').replace(',', ' ').replace('.', ' ').replace('&', ' ').split()
        keep_this = True
        for y in range(len(split_list)):
            if split_list[y].upper() in no_no_jobs:
                keep_this = False
        if keep_this:
            new_list.append([job_title_list[i], job_title_minor_list[i], job_link_list[i]])
    # print("processing second column")
    new_list2 = []
    for i in range(len(new_list)):
        split_list = new_list[i][1].replace('/', ' ').replace('-', ' ').replace(',', ' ').replace('.', ' ').replace('&', ' ').split()
        # print(f"{split_list}")
        keep_this = True
        for y in range(len(split_list)):
            if split_list[y].upper() in no_no_jobs:
                print(f"dropping {split_list[y]}")
                keep_this = False
        if keep_this:
            new_list2.append(new_list[i])

    print(f"processed page {page}, {len(new_list2)} entries added")
    time.sleep(random.randint(0, 10))
#end looop
print("-----------------------new_list")
for i in new_list:
    print(str(i))

print(len(new_list))


