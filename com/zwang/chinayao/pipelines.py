import xlwt


def do_pipelines_xls(self, medicallist):
    filename = '西药药品价格数据.xls'
    self.log.info('准备保存数据到excel中...')
    book = xlwt.Workbook(encoding='utf8', style_compression=0)
    sheet = book.add_sheet('西药药品价格')
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '剂型')
    sheet.write(0, 2, '规格')
    sheet.write(0, 3, '供货价')
    sheet.write(0, 4, '零售价')
    sheet.write(0, 5, '生产企业')
    for i in range(1, len(medicallist) + 1):
        item = medicallist[i - 1]
        sheet.write(i, 0, item.mc)
        sheet.write(i, 1, item.jx)
        sheet.write(i, 2, item.gg)
        sheet.write(i, 3, item.ghj)
        sheet.write(i, 4, item.lsj)
        sheet.write(i, 5, item.scqy)
    book.save(filename)
    self.log.info('excel文件保存成功！')


def pipelines_csv(self, medicallist):
    pass