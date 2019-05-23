import requests
from os import listdir

def dlfile(url):
    a = requests.get(url)
    url = str(a.url)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0 
    with open(url[url.rfind("/")+1:], 'wb') as f:
        print("downloaded " + url[url.rfind("/")+1:])
        for data in r.iter_content(block_size):
            if data:
                wrote = wrote + len(data)
                f.write(data)
    if total_size != 0 and wrote != total_size:
        print("hey wait something went wrong with " + url[url.rfind("/")+1:])
    

o = open('override.txt', 'r')
override = o.read().replace("\r\n","\n").split("\n")

m = open('mods.txt', 'r')
mods = m.read().replace("\r\n","\n").split("\n")

for i in mods:
    if i not in override:
        dlfile(i + "/files/latest")

for i in override:
    if i not in mods:
        dlfile(i + "/download")
