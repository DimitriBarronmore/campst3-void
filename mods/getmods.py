import requests
from os import listdir

def dlfile(url):
    a = requests.get(url)
    url = str(a.url)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0
    toWriteInst.append(url[url.rfind("/")+1:] + '\n\n')
    with open(url[url.rfind("/")+1:], 'wb') as f:
        print("downloaded " + url[url.rfind("/")+1:])
        for data in r.iter_content(block_size):
            if data:
                wrote = wrote + len(data)
                f.write(data)
    if total_size != 0 and wrote != total_size:
        print("hey wait something went wrong with " + url[url.rfind("/")+1:])

    
if "installed.txt" not in listdir("."):
    inst = open('installed.txt', 'w')
    inst.close()

inst = open('installed.txt', 'r')
installed = inst.read().replace("\r\n","\n").split("\n")
inst.close()

toWriteInst = []

m = open('mods.txt', 'r')
mods = m.read().replace("\r\n"  ,"\n").split("\n")

for i in range(0,len(mods)):
    x = mods[i]
    if "files/" in x or x in installed:
        continue
    if i < len(mods)-1:
        a = requests.get(mods[i])
        txt = a.text
        toWriteInst.append(x+'\n')
        toWriteInst.append(txt[txt.find('og:description')+25 : txt.find('og:url')-22]+'\n')
        if x not in mods[i+1]:
            dlfile(x + "/files/latest")
        else:
            dlfile(mods[i+1] + "/download")

inst = open('installed.txt', 'a')
inst.writelines(toWriteInst)
inst.close()
