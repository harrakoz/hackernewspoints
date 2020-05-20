import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
res_2 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, "html.parser")
soup_2 = BeautifulSoup(res_2.text, "html.parser")

link = soup.select(".storylink")
link_2 = soup_2.select(".storylink")
mega_link = link + link_2

subtext = soup.select(".subtext")
subtext_2 = soup.select(".subtext")
mega_subtext = subtext + subtext_2

def scraper(links, vote):
  hn = []
  for index, item in enumerate(mega_link):
    text = item.getText()
    href = item.get("href", None)
    subbo = mega_subtext[index].select(".score")
    if len(subbo):
      for i in subbo:
        points = int(i.getText().replace(" points", ""))
        if points >= 100:
          hn.append({
            "Title": text,
            "Link": href,
            "Points": points
          })

  hn.sort(key=lambda x: x["Points"], reverse=True)
  return hn
    
print(scraper(mega_link, mega_subtext))