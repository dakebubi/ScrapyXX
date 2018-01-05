一、scrapycmd项目目前包含两个spider：dmoz和image_spider，
   scrapy startproject scrapycmd 命令生成的scrapycmd/spiders目录已经删除，
   并一分为二


二、启动爬虫的方式由默认的配置文件settings.py中设置项指定：
1、SPIDER_MODULES来指定启动的爬虫，可以有多个
2、item_pipeline由ITEM_PIPELINES指定，可以有多个且后面的数字代表执行的优先顺序
   如果定义多个的话，所有定义的pipeline都会作用到spider构造的Item上



三、image_spider爬虫说明：
1、ITEM_PIPELINES指定为scrapycmd.pipelines.MyImagesPipeline
2、并且启动参数中不指定-o items.json(否则只是会存储图片url至items.json)
则会直接下载图片文件至IMAGES_STORE指定的目录

四、shell方式启动
scrapy shell "http://www.importnew.com/"