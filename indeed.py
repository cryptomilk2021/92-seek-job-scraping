import requests
from bs4 import BeautifulSoup
import time
import random

site_root = 'https://au.indeed.com'
no_no_jobs = ['SALE', 'RECEPTIONIST', 'RETAIL', 'COLES', 'SALES', 'JUNIOR', 'NURSE', 'BAR', 'NURSES', 'MEDICAL',
              'SECURITY', 'ADMIN', 'PHYSIOTHERAPIST', 'OCCUPATIONAL', 'ENROLLED', 'TRAINEE', 'TABLELANDS', 'PODIATRIST',
              'CARER', 'MASSAGE', 'THERAPIST', 'TOWNSVILLE', 'CHEF', 'BEAUTY', 'PATHOLOGIST', 'THERAPIST', 'BAR',
              'AGED', 'RECEPTION', 'MAREEBA', 'CONSTRUCTION', 'BEVERAGE', 'LIBRARY', 'PHARMACY', 'ATTENDANT',
              'HOSPITALITY', 'CLEANER', 'HOUSEKEEPING', 'CASINO', 'BARISTA', 'LINGERIE', 'MEDICAL', 'RETAIL',
              'MERCHANDISER', 'MERCHANDISERS', 'WAIT', 'WAITING', 'YOUTH', 'RESTAURANT', 'BWS', 'HEALTH', 'WOOLWORTHS',
              'WEIPA', 'HOTEL']

job_title_list = []
job_company_name_list = []
job_link_list = []
new_list = []
#START loop
for page in range(0, 50, 10):
    # response = requests.get(f"https://au.indeed.com/jobs?q&l=Cairns%20QLD&start=1&vjk=4005550de89de391")
    response = requests.get(f"https://au.indeed.com/jobs?q&l=Cairns%20QLD&start={page}&vjk=4005550de89de391")
    n = response.text

    soup = BeautifulSoup(n, "html.parser")

    myas = soup.find_all('a', class_="jcs-JobTitle")
    print(f'found {len(myas)} entries')
    ws_list = []
    for div in myas:
        ws_list.append([div.getText(), site_root + str(div['href'])])

    myspan = soup.find_all('span', class_="companyName")
    for i in range(len(myspan)):
        # print(f"{myspan[i].getText()}")
        ws_list[i].extend([myspan[i].getText()])

    for i in range(len(ws_list)):
        split_list = ws_list[i][0].replace('/', ' ').replace('-', ' ').replace(',', ' ').replace('.', ' ').replace('&', ' ').split()
        keep_this = True
        for y in range(len(split_list)):
            if split_list[y].upper() in no_no_jobs:
                print(f"job title dropping {split_list[y].upper()}")
                keep_this = False
        split_list = ws_list[i][2].replace('/', ' ').replace('-', ' ').replace(',', ' ').replace('.', ' ').replace('&', ' ').split()
        for y in range(len(split_list)):
            if split_list[y].upper() in no_no_jobs:
                print(f"company name dropping {split_list[y].upper()}")
                keep_this = False

        if keep_this:
            new_list.append(ws_list[i])

    # for i in new_list:
    #     print(i)
    # print(len(i))

    print(f"processed page {page}, {len(new_list)} entries added")
    time.sleep(random.randint(0, 10))


for i in new_list:
    print(str(i))

print(len(new_list))


