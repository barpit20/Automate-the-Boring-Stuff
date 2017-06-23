import requests, os, bs4
url = 'http://explosm.net/comics/4650/'  
os.makedirs('CandH') 
#while url!='http://explosm.net/comics/15/':
for i in range(5):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('#comic-container img') 
    if comicElem == []:
         print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()
    imageFile = open(os.path.join('CandH', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    prevLink = soup.find_all("a", class_="previous-comic ")
    url = 'http://explosm.net' + prevLink[0].get('href')
print('Done.')