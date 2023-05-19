import concurrent.futures
import requests
import time

start = time.perf_counter()

image_url = [
    """ADD Image Links to Download"""

]


def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[3]
    image_name = f'{image_name}.mp4'
    with open(image_name, 'wb') as image_files:
        image_files.write(image_bytes)
        print(f"{image_name} was downloaded")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, image_url)

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
