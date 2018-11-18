import requests
import re
import tqdm
import time
from bs4 import  BeautifulSoup

MAX_USER = 1000
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36', 'Referer': 'https://weibo.cn/repost/H2E9Mquk3?uid=1826792401&rl=1&page=3'}
cookies = dict(_T_WM='7366f1a14f16e9d9dbcd1d321732fb97', ALF='1544889477', SCF='ArB_kgyoKfXW38wa1AYiq3ROqAY17WdJIKyHR3u-aSneeG8rzrS3V2clHj3VxCNYYw8_UyFdReEszLNVQQG2Tyw.', SUB='_2A2526efBDeThGedG7VAX9SnJyD-IHXVSFYmJrDV6PUJbktANLUXFkW1NUTS1qTqH24iIqezzZkst6iOD8oZmZGXY', SUBP='0033WrSXqPxfM725Ws9jqgMF55529P9D9WhbhxZEkl0P7vSuHTpMZcOF5JpX5K-hUgL.Fo2RSozcSKMfe0e2dJLoI7__qgUDqNxydsHVU5tt', SUHB='0nl_u24cUo-5kY', SSOLoginState='1542297489')
data_list = []
male = 0
female = 0
with open('./uid4k.txt') as file:
    for i in tqdm.trange(MAX_USER):
        uid = next(file)
        user_page = f'https://weibo.cn{uid}'
        profile_raw = requests.get(user_page, headers=headers, cookies=cookies)
        soup = BeautifulSoup(profile_raw.text, 'lxml')
        basic_profile = soup.find('span', 'ctt').text
        sex_and_region = re.split(r'\s+', basic_profile)
        sex_and_region = re.split(r'/', sex_and_region[1])
        data_dict = {}
        data_dict['sex'] = sex_and_region[0]
        data_dict['region'] = sex_and_region[1]
        data_list.append(data_dict)
        if sex_and_region[0] == '男':
            male = male+1
        elif sex_and_region[0] == '女':
            female = female+1
        else:
            print('震惊！')
        male_percent = male / (male + female) * 100
        female_percent = female / (male + female) * 100
        print(f'男性比例{male_percent:.2f}% 女性比例{female_percent:.2f}%')
        time.sleep(1)
print(male, female)

# for i in range(len(data_list)):
#     print(data_list[i])



