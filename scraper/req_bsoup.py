# real python
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

col = [
    (
        job_ele.find("h2", class_="title"),
        job_ele.find("h3", class_="company"),
        job_ele.find("p", class_="location"),
    )
    for job_ele in job_elements
]

txt = [f"Get total {len(col)} jobs info:\n\n"]
for job in col:
    desc = job[0].text.strip()
    if "python" in desc.lower():
        company = job[1].text.strip()
        location = job[2].text.strip()
        txt.append(f"{desc}\nat {company}\nin {location}\n\n")

with open("soupResultsContainer", "w+") as f:
    f.writelines(txt)
