import time
import requests
import pyfiglet
banner = pyfiglet.figlet_format("KINGMAN")
print(banner)
hook = input("Please Insert WebHook URL: ")
def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n [STATUS] WRBHOOK IS DELETED NOW")
    elif check.status_code == 200:
        print("\n [STATUS] FAILD TO DELETE WEBHOOK")

kingman_top = 1
if kingman_top == 1:
    delete(hook)
