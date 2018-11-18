import requests
import re
import tqdm
import time
from bs4 import  BeautifulSoup


MAX_PAGE = 10
URL = 'https://weibo.cn/repost/H1rMeFWa2?uid=1826792401' # 转发链接 以uid的数字结尾
href_compiled = re.compile("(/u/)(\d{10})($)")
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 'Referer': 'https://weibo.cn/repost/H2E9Mquk3?uid=1826792401&rl=1&page=3'}
cookies =dict(ALF='1544799549',SCF='ArB_kgyoKfXW38wa1AYiq3ROqAY17WdJIKyHR3u-aSne20_yAVrTJ34P1XFT8zdjX94B1bPQO_TA31n-hEwNzec.',SUB='_2A2526EgRDeThGedG7VAX9SnJyD-IHXVSE2hZrDV6PUJbktAKLVX8kW1NUTS1qT26PRgV-tptwiDdUrLiUpIhWg3Z', SUBP='0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbhxZEkl0P7vSuHTpMZcOF5JpX5K-hUgL.Fo2RSozcSKMfe0e2dJLoI7__qgUDqNxydsHVU5tt', SUHB='03oURkwUiuWsnm', SSOLoginState='1542207553', _T_WM='7366f1a14f16e9d9dbcd1d321732fb97')
start_time = time.time()
for page_num in tqdm.trange(MAX_PAGE):
    repost_url = f'{URL}&&page={page_num+1}'
    repost_raw = requests.get(repost_url, cookies=cookies, headers=headers)
    if repost_raw.status_code != 200:
        print(f'error: code {repost_raw.status_code} page {page_num}')
    soup = BeautifulSoup(repost_raw.text, 'lxml')
    for page in soup.find_all('div', class_='c'):
        id_list = page.find_all(href=href_compiled)
        uid_list = [uid['href'] for uid in id_list]
        with open('./uid.txt', 'a+') as uid_file:
            for line in uid_list:
                uid_file.write(line)
                uid_file.write('\n')
    time.sleep(1)
print(f'time: {time.time()-start_time}s')

