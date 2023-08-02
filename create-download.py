from pathlib import Path
import requests
import shutil

x = input("Lotfan esme poshe khod ra type namaeed: ")

path = Path(x)

print(path.mkdir())

url = input("Link Aks ba paswand .jpg ra type namaeed: ")

y = input("name aks jahate zakhire ra vared namaeed: ")

aks = requests.get(url)

with open(y, 'wb') as file:
    file.write(aks.content)

source = Path(y)
target = Path(x)

shutil.copy(source, target)


#

