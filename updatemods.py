import os
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ModuleNotFoundError:
    install("requests")

if not os.path.exists("mods/"):
    os.mkdir("mods/")

global toWriteInst #variable init
toWriteInst = []

def write_list(): #write to registry as it goes
    global toWriteInst
    inst = open('installed.txt', 'w')
    inst.writelines(toWriteInst)
    inst.close()
    

def dlfile(url): #file downloader
    a = requests.get(url)
    url = str(a.url)
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0
    with open("mods/" + url[url.rfind("/")+1:], 'wb') as f:
        print("downloaded " + url[url.rfind("/")+1:])
        for data in r.iter_content(block_size):
            if data:
                wrote = wrote + len(data)
                f.write(data)
    if total_size != 0 and wrote != total_size:
        print("hey wait something went wrong with " + url[url.rfind("/")+1:])

if "installed.txt" in os.listdir():
    inst = open('installed.txt', 'r') #save registry of installed mods to list
    installed = inst.read().split("\n")
    inst.close()
else:
    installed = []

new_list = ["{0}\n".format(item, index)
            for (index, item) in enumerate(installed)] 

toWriteInst = new_list #preserve newlines

m = open('mods.txt', 'r')
mods = m.read().replace("\r\n"  ,"\n").split("\n") #load modlist

cropped_mods = [] #crop filters, newlines, comments
for i in range(0,len(mods)):
    if mods[i] == "" or mods[i][:1] == "#" or "files/" in mods[i]:
        continue
    else:
        cropped_mods.append(mods[i])

mods = cropped_mods

for i in range(0,len(mods)):
    if "installed.txt" not in os.listdir(): #exit condition
        print("please download some mods first, thanks! <3")
        break
    x = mods[i].strip(" ")
    percent = (str(100. / len(mods) * i )[:2].strip(".") + "% ")
    if x in installed:
        index = installed[installed.index(x)+2] #index version from registry
    else:
        print(percent + "WARNING: [...]/" + x[x.find('projects/'):]
              + " is not installed!") #mod not installed warning
        continue
    print(percent + x + "...") #print mod name
    a = requests.get(x + "/files/latest") #find newest version
    url = str(a.url)
    r = requests.get(url)
    latest = (url[url.rfind("/")+1:])
    if index == latest: #check if latest version
        print("up to date!")
        continue
    else:
        print("newer version found...") #download new version
        os.remove("mods/" + index)
        toWriteInst[installed.index(index)] = latest + '\n'
        dlfile(x + "/files/latest")
        write_list() #update registry

if "installed.txt" in os.listdir():
    print("100%")
input("Press Enter to continue...")
