import threading
import requests
from tqdm import tqdm

u = input("Enter url:")


def send_request(url: str):
    requests.get(url=url)


print("Sending requests ...")

threads = []
for i in tqdm(range(1_000)):
    th1 = threading.Thread(target=send_request, args=(), kwargs={"url": u})
    th1.start()
    threads.append(th1)

print("Please wait...")

for th in threads:
    th.join()

print("Requests completed successfully")
