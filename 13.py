import requests
my_files2 = open("urls.txt")
for url in my_files2.readlines():
    current_url = url.strip()
    response = requests.get(current_url)
    if response.status_code == 200:
        print(f"{current_url.split('//')[1]} is up and running")


import requests
my_files2 = open("urls.txt")
for url in my_files2.readlines():
    current_url = url.strip()
    response = requests.get(current_url)
    if response.status_code == 200:
        print(f"{current_url.split('//')[1]} is up and running")