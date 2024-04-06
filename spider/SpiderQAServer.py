import csv  # 内置模块 无需安装
import time
import random
from DrissionPage import SessionPage


class Spider_answer:
    # 随机User-Agent池
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/118.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; rv:11.0) like Gecko ',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5680.400 QQBrowser/10.2.1852.400',
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38."
    ]
    # 请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    # 爬取的页数
    page = 50

    def __init__(self, page=50):
        self.page = page + 1

    # 格式化CSV文件
    def clear_csv(self):
        with open("static/data/csv/data-answer.csv", mode='w', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow(['pid', 'num', 'question', 'answer'])

    # 发送请求，获取回答
    def get_product_answer(self, pid, qid, i, quest_content):
        t = int(time.time() * 1000)

        answer_page = SessionPage()

        url = f'https://api.m.jd.com/?appid=item-v3&functionId=getAnswerListById&' \
              f'client=pc&clientVersion=1.0.0&t={str(t)}&loginType=3&' \
              f'uuid=181111935.744904110.1694775482.1707650211.1707657113.45&' \
              f'page=1&questionId={qid}'
        while True:
            print(str(pid) + '---answer-----------')
            err = 'answer_page'
            answer_page.get(url=url, headers=self.headers)
            if answer_page:
                try:
                    err = 'answerList'
                    answerList = answer_page.json['answers']
                    err = 'answerList-for'
                    for answer in answerList:
                        err = 'answer-content'
                        answer_content = answer['content'].encode('GBK', 'ignore').decode('GBK', 'ignore')
                        err = 'answer-csv'
                        with open("static/data/csv/data-answer.csv", mode='a', newline='', encoding='utf-8') as f:
                            csv.writer(f).writerow(
                                [pid, i, quest_content.replace("\n", " "), answer_content.replace("\n", " ")])
                    break
                except:
                    # 获取问题列表失败，没有问题了，没有下一页，直接退出所有循环
                    print(str(pid) + '----获取回答列表失败----' + str(err))
                    return 0
            else:
                continue

    # 发送请求,获取问题
    def get_product_quest(self, pid):
        quest_headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.",
            'Cookie': 'shshshfpa=4ca191ff-53f0-8bae-8502-a1036427f352-1694775485; shshshfpx=4ca191ff-53f0-8bae-8502-a1036427f352-1694775485; __jdu=744904110; _pst=jd_51f57c6a7950b; unick=jd_51f57c6a7950b; pin=jd_51f57c6a7950b; _tp=SQwJwPhztLc0Dk6FDRUju8WLLfk3W9eDpw2%2FvY165cc%3D; pinId=ZH5brpj5GCLkLjFIQPgRILV9-x-f3wj7; unpl=JF8EAK5nNSttD0lXAkwLGRoWTQpdWwgATR4Da2MMUF0LSgMHHgQTERJ7XlVdWBRKFB9uZBRXXFNJUg4YACsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrBB4XGEpYVF5cOEonBF9XNVdVXk5TASsDKxMgCQkIXlwASREAImEAUVVZTlQFGjIaIhM; jcap_dvzw_fp=PLpx_WcJ9vyHtl-rAPikcxDx-G0JaT_jkK5UhhcazP8jpU5p5hR-vxB5vfuZ4uukeRKprup-q4H0jbK0FU9wKw==; user-key=698278b7-d600-4d80-a2a2-4450a0a41682; mt_xid=V2_52007VwUXV1VZV1ofSCkPUDIAEFtYWk5TSkxMQABkBhZOVVAGCgMbHg4EYQRFAQgNVlsvShhfAHsCEU5dWkNZH0IdXg5lAiJQbVhiUxlJGV0DYAUXV21dU1MZ; PCSYCityID=CN_440000_441900_0; TrackID=16N-wcRrA5Vs48zuUZPgx-qhv40ISx3pMK7DpxEJlmuuZtFTdCY6Y1o3kORYX0U76UGiqHsuNFxbfESOrfT5nu8aGkWDxvYdxxCLu0NzoPAk; thor=6465F1DAA2E71EAB7DDA2A69EBCA0834998A5F5832EE816E44E10F8193F7D99F3AD27D7714AC8DF392196656EE318B9B087A14D90AEF2089218C07269D3D336B0EE1BC0F98A8F379C8587D62385ABDAB2080516A3E7DEC366E709699100ADF703E46489C41665236150012ACA262B927F03D3B3D8174885156CA2A44092E757D84AF8D49B26F002A063527CCD24E8D363D7CC52C7AD20DC08F5FF84BF687A7BC; flash=2_oodH7QS8-_jvVxmSQy2GOKj1hS0uktkMkzlxtx917d4pH8cYys37qimeeERJ56OhgZO-oU-LgCiiKvIwiiklJaxiYXKX_BfE0eXF0TQXcnN*; areaId=19; 3AB9D23F7A4B3C9B=XCLROUSW47ZSUYOPTPWJJDNPVO7YRZGZMHNLSMEMDV3UDLM3QV7X74W7O23TNXKGYCWRRVRHH3LF6BXDU6BCACCKBA; ipLoc-djd=19-1655-4886-0; __jda=76161171.744904110.1694775482.1708811307.1709125417.57; __jdc=76161171; 3AB9D23F7A4B3CSS=jdd03XCLROUSW47ZSUYOPTPWJJDNPVO7YRZGZMHNLSMEMDV3UDLM3QV7X74W7O23TNXKGYCWRRVRHH3LF6BXDU6BCACCKBAAAAAMN57IDTFQAAAAACF4EUBHG4GRP5AX; _gia_d=1; shshshfpb=BApXe69bY7OhAVz_vobdlGjfLyHTf4UKIB9Y2U6pi9xJ1MuvgoIO2; __jdb=76161171.2.744904110|57.1709125417; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a379ae75074e49dcb7e1e989b6c66857|1709125422542'
        }
        i = 1
        for page in range(1, self.page):
            t = int(time.time() * 1000)
            # 等待3-10秒
            # time.sleep(random.uniform(1, 3))
            quest_page = SessionPage()
            url = f'https://api.m.jd.com/?appid=item-v3&functionId=getQuestionAnswerList&client=pc' \
                  f'&clientVersion=1.0.0&t={str(t)}&loginType=3&' \
                  f'uuid=181111935.744904110.1694775482.1707650211.1707657113.45' \
                  f'&page={page}&productId={pid}'
            while True:
                print(str(pid) + '---quest-----------')
                err = 'quest_page'
                quest_page.get(url=url, headers=quest_headers)
                print(quest_page)
                print(quest_page.json)
                if quest_page.json is None:
                    time.sleep(30)
                    continue
                if quest_page:
                    try:
                        # print('try-----code')
                        if quest_page.json['code'] == '3' :
                            # print('try-----try重新发送')
                            continue
                        # print('try-----try通过')
                    except:
                        # print('try-----except通过')
                        pass
                    try:
                        err = 'questList'
                        questList = quest_page.json['questionList']
                        err = 'questList_for'
                        for quest in questList:
                            err = 'quest_content'
                            quest_content = quest['content'].encode('GBK', 'ignore').decode('GBK', 'ignore')
                            err = 'quest_id'
                            quest_id = quest['id']
                            err = 'answerList'
                            answerList = quest['answerList']
                            err = 'answerList_for'
                            if answerList:
                                err = 'answerList_cz'
                                self.get_product_answer(pid, quest_id, i, quest_content)
                            else:
                                err = 'answerList_bcz'
                                with open("static/data/csv/data-answer.csv", mode='a', newline='',
                                          encoding='utf-8') as f:
                                    csv.writer(f).writerow([pid, i, quest_content.replace("\n", " "), '无回答'])
                            i += 1
                        break
                    except:
                        # 获取问题列表失败，没有问题了，没有下一页，直接退出所有循环
                        print(str(pid) + '----获取问题列表失败----' + str(err))
                        return 0
                else:
                    continue
