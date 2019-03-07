# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RsscraperPipeline(object):

    def process_item(self, item, spider):
        #  FIXME I know it's not the best idea to ping the db for every item in the pipeline, but the task was time restricted and this was the quickest solution :)
        model_class = getattr(item, 'django_model')
        try:
            model_class.objects.get(currency=item['currency'], rate_from=item['rate_from'])
        except model_class.DoesNotExist:
            item.save()
        return item
