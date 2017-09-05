# -*- coding: utf-8 -*-
# @Time    : 2017/9/5 下午10:00
# @Author  : yuzeyu
# @Site    : 
# @File    : serializer.py
# @Software: PyCharm

from rest_framework import serializers



class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    click_num = serializers.IntegerField(default=0)

