import time
import urllib.request

from com.zwang.chinayao.MyLog import MyLog
from com.zwang.chinayao.Spider import doSpider
from com.zwang.chinayao.pipelines import do_pipelines_xls


class GetInfor(object):
    def __init__(self):
        self.log = MyLog()
        self.starttime = time.time()
        self.log.info(u'爬虫程序开始运行，时间： %s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.starttime)))
        self.medicallist = self.getmedicallist('drugName.txt')
        self.items = self.spider(self.medicallist)
        self.pipelines_xls(self.items)
        self.endtime = time.time()
        self.log.info(u'爬虫程序运行结束，时间： %s' % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.endtime)))
        self.usetime = self.endtime - self.starttime
        self.log.info(
            u'用时  %d时 %d分%d秒' % (self.usetime // 3600, (self.usetime % 3600) // 60, (self.usetime % 3600) % 60))

    def getmedicallist(self, filename):
        '''从文件name.txt中导出所有需要查询的药品的名称
        '''
        medicallist = []
        with open(filename, 'r') as fp:
            s = fp.read()
            for name in s.split():
                medicallist.append(name)
        self.log.info(u'从文件%s 中读取药品名称成功！获取药品名称 %d 个' % (filename, len(medicallist)))
        return medicallist

    def spider(self, names):
        items = doSpider(self, names)
        return items

    def pipelines_xls(self, medicallist):
        do_pipelines_xls(self, medicallist)

    def pipelines_csv(self, medicallist):
        pass

    def getresponsecontent(self, url):
        try:
            response = urllib.request.urlopen(url).read()
        except Exception as e:
            self.log.error(u'返回 URL: %s 数据失败' % url)
            print(e)
            return ''
        else:
            self.log.info(u'返回URL: %s 数据成功' % url)
        return response


if __name__ == '__main__':
    GetInfor()
