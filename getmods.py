import subprocess
import sys
import os
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ModuleNotFoundError:
    install("requests")

global toWriteInst
toWriteInst = []

if not os.path.exists("mods/"):
    os.mkdir("mods/")

def write_list():
    global toWriteInst
    inst = open('installed.txt', 'a')
    inst.writelines(toWriteInst)
    inst.close()
    toWriteInst = []

def dlfile(url):
    a = requests.get(url)
    url = str(a.url)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0
    toWriteInst.append(url[url.rfind("/")+1:] + '\n\n')
    path = "mods/" + url[url.rfind("/")+1:]
    if os.path.exists(path):
        print(percent + "skipping " +  url[url.rfind("/")+1:] + ", exists")
    else: 
        with open(path, 'wb') as f:
            print(percent + "downloaded " + url[url.rfind("/")+1:])
            for data in r.iter_content(block_size):
                if data:
                    wrote = wrote + len(data)
                    f.write(data)
        if total_size != 0 and wrote != total_size:
            print("hey wait something went wrong with " + url[url.rfind("/")+1:])

    
if "installed.txt" not in os.listdir("."):
    inst = open('installed.txt', 'w')
    inst.close()

inst = open('installed.txt', 'r')
installed = inst.read().replace("\r\n","\n").split("\n")
inst.close()

m = open('mods.txt', 'r')
mods = m.read().replace("\r\n"  ,"\n").split("\n")
m.close()

cropped_mods = []
for i in range(0,len(mods)):
    x = mods[i].strip(" ")
    if x == "" or x[:1] == "#" or x in installed or x[:x.find("/files")] in installed:
        continue
    else:
        cropped_mods.append(mods[i])

mods = cropped_mods

if len(mods) == 0:
    emptyList = True
else:
    emptyList = False


for i in range(0,len(mods)):
    x = mods[i].strip(" ")
    if x[:1] == "#":  #comment system
        continue
    if x in installed or x[:x.find("/files")] in installed:
        continue
    percent = (str(100. / len(mods) * i )[:2].strip(".") + "% ")
    if "files/" in x:
        a = requests.get(x[:x.find("files/")])
        dl_url = (x + "/download")
        x = x[:x.find("/files")]
    else:
        a = requests.get(x)
        dl_url = (x + "/files/latest")
    txt = a.text
    toWriteInst.append(x+'\n')
    toWriteInst.append(txt[txt.find('og:description')+25 :
                           txt.find('og:url')-22]+'\n')
    dlfile(dl_url)
    write_list()

if emptyList == False:
    print("100% - complete! <3")
else:
    print("You need a list of fresh new mods first!")
input("Press Enter to continue...")
