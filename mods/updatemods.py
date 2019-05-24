import requests
from os import listdir
from os import remove

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

    
inst = open('installed.txt', 'r')
installed = inst.read().split("\n")
inst.close()

new_list = ["{0}\n".format(item, index)
            for (index, item) in enumerate(installed)]

toWriteInst = new_list

m = open('mods.txt', 'r')
mods = m.read().replace("\r\n"  ,"\n").split("\n")

for i in range(0,len(mods)):
    x = mods[i]
    if "files/" in x:
        continue
    if i < len(mods)-1:
        if x not in mods[i+1]:
            index = installed[installed.index(x)+2]
            a = requests.get(x + "/files/latest")
            url = str(a.url)
            r = requests.get(url, stream=True)
            latest = (url[url.rfind("/")+1:])
            print(x)
            if index == latest:
                print("up to date!")
                continue
            else:
                print("newer version available...")
                remove(index)
                toWriteInst[installed.index(index)] = latest + '\n'
                dlfile(x + "/files/latest")


inst = open('installed.txt', 'w')
inst.writelines(toWriteInst)
inst.close()
