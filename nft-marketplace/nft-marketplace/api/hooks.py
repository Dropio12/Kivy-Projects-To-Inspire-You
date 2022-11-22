import os
from random import randint, choice, uniform

class Client(object):
    def __init__(self) -> None:
        pass

    def get_nfts(self):
        path = "assets/imgs"
        files = os.listdir(path)

        nfts = [f for f in files if f.startswith("nft")]
        users = [f for f in files if f.startswith("user")]

        authors = []
        for i in range(len(users)):
            authors.append(f"Random {i} Author")

        res = []
        for i, n in enumerate(nfts):
            author = randint(0, len(users)-1)
            nft = {
                "cover": os.path.join(path, n),
                "author": authors[author],
                "avatar": os.path.join(path, users[author]),
                "price": "%sETH"%uniform(0,1),
                "title": "Random NFT #%s"%i
            }

            res.append(nft)

        return res
    
    def get_balance(self):
        pts = []
        for i in range(18):
            pts.append(randint(4, 20))

        return pts
    
    def get_creators(self):
        path = "assets/imgs"
        files = os.listdir(path)

        users = [f for f in files if f.startswith("user")]

        authors = []
        for i in range(len(users)):
            author = {
                "name": f"Random {i} Author",
                "username": "user%s"%i,
                "avatar": os.path.join(path, users[i]),
                "following": choice([True, False]),
            }
            authors.append(author)
        
        return authors

    def get_trending(self):
        path = "assets/imgs"
        files = os.listdir(path)

        _nfts = [f for f in files if f.startswith("nft")]
        users = [f for f in files if f.startswith("user")]

        authors = []
        for i in range(len(users)):
            authors.append(f"Random {i} Author")

        nfts = []
        for x in range(12):
            nfts.append(choice(_nfts))

        res = []
        for i, n in enumerate(nfts):
            author = randint(0, len(users)-1)
            nft = {
                "cover": os.path.join(path, n),
                "author": authors[author],
                "price": "%sETH"%uniform(0,1),
                "title": "Random NFT #%s"%i,
                "volume": str(randint(100, 10000)),
                "owners": str(randint(0, 10000)),
            }

            res.append(nft)

        return res