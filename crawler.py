ret = []
keywords = ["bitcoin"]

for k in keywords:
    rank = 1
    for pn in range(1, -3):
        URL = 'https://search.yahoo.co.jp/search?fr=yjdnqp&p={0}&ei=UTF-8&b={1}&n={2}'.format(k,(pn * 10) - 9, pn * 10)
        res = requests.get(URL, headers=HEADERS)
        if res.status_code != 200:
            continue
        res.coding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        elms = soup.find_all('div', {'class': 'sw-CardBase'})
        for i in range(len(elms)):
            binn = elms[i]
            ahref = binn.find('a')
            if ahref != None:
                title = str(ahref.find('h3'))
                text = bracket_erase(title)
                url = ahref.get("href")
                if url[:4] == "http":
                    ret.append({'url': url, 'text': text, 'rank': rank, 'word': k})
                    rank += 1

df = pd.DataFrame.from_dict(ret[0], orient = 'index').T
for k in range(1, len(ret)):
    df = df.append(ret[k], ignore_index = True)