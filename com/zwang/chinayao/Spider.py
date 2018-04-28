import random
import time

from bs4 import BeautifulSoup

from com.zwang.chinayao.Item import Item


def doSpider(self, names):
    items = []
    for name in names:
        if name != '':
            self.log.info(u'尝试爬取 %s 信息' % name)
            url = 'http://www.china-yao.com/?act=search&typeid=1&keyword=' + name
            htmlcontent = self.getresponsecontent(url)
            soup = BeautifulSoup(htmlcontent, 'lxml')
            tagul = soup.find('ul', attrs={'class': 'pagination'})
            tagpage = tagul.find_all('a')
            self.log.info(u'此药品信息共%d 页' % len(tagpage))
            time.sleep(1)
            if len(tagpage) == 0:
                page = 0
            else:
                try:
                    page = int(tagpage[-1].get_text().strip())
                except:
                    page = int(tagpage[-2].get_text().strip())

            "取前5页"
            if(page > 2):
                page = 2
            for i in range(1, page + 1):
                newurl = url + '&page=' + str(i)
                newhtmlcontent = self.getresponsecontent(newurl)
                soup = BeautifulSoup(newhtmlcontent, 'lxml')
                tagtbody = soup.find('tbody')
                tagtr = tagtbody.find_all('tr')
                self.log.info(u'该页面共有记录 %d 条，开始爬取' % len(tagtr))
                for tr in tagtr:
                    tagtd = tr.find_all('td')
                    item = Item()
                    item.mc = tagtd[0].get_text().strip()
                    item.jx = tagtd[1].get_text().strip()
                    item.gg = tagtd[2].get_text().strip()
                    item.ghj = tagtd[3].get_text().strip()
                    item.lsj = tagtd[4].get_text().strip()
                    item.scqy = tagtd[5].get_text().strip()
                    items.append(item)
                self.log.info(u'页面%s 数据已保存' % newurl)
                sleeptime = random.randint(7, 12)
                time.sleep(sleeptime)  # 给程序适当降速，防止被服务器拦截

    self.log.info(u'数据爬取结束，共获取 %d条数据。' % len(items))
    return items

