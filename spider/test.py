from DrissionPage._pages.chromium_page import ChromiumPage
import configparser
from spider import SpiderVerify

config = configparser.ConfigParser()
config.read('../configData.ini')  # 读取配置文件

page = ChromiumPage()

page.get('https://item.jd.com/10099267090738.html')

SpiderVerify.login(page)


