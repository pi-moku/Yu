import os
import shutil
import requests

def download(url):
    file_name = os.path.basename(url)
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open("data/" + file_name, 'wb') as file:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, file)
while True:
    url = input("yu@otoka% ")
    if url == "q":
        break
    try:
        download(url)
    except:
        print(f"error: {url}: not found ( or inaccessible )")
