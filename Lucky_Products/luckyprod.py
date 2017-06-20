import requests, sys, webbrowser, bs4
print('Searching for '+' '.join(sys.argv[1:])+' ...')
res=requests.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
links = soup.select('a.a-link-normal.s-access-detail-page.a-text-normal')
print(len(links))
numOpen = len(links)
for i in range(numOpen):
    webbrowser.open(links[i].get('href'))