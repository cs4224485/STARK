该组件可实现对表的快速增删查改
使用方法类似于Django Admin需要在APP中创建stark.py文件。 然后注册需要进行增删查看的表

example：


from stark.service import starkAdmin
from django.shortcuts import HttpResponse
from .models import *
from django.urls import reverse
print('star123')

class BookConfig(starkAdmin.StarkModel):

    def delete_action(self, request, query_set):
        query_set.delete()
        return HttpResponse('删除成功')

    delete_action.short_description = '批量删除'
    actions = [delete_action]
    search_field = ['title', 'price']
    list_display = ['title', 'price', 'author', 'publish']
    list_display_links = ['title', 'author']
    list_filter = ['title', 'author']



starkAdmin.site.register(Book, BookConfig)
starkAdmin.site.register(Author)
starkAdmin.site.register(Publish)