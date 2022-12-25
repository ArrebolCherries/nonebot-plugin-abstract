#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='nonebot_plugin_abstract',
    version='1.0.6',
    author='CherryCherries',
    author_email='cherrycherries@foxmail.com',
    url='https://github.com/CherryCherries/nonebot-plugin-abstract',
    description=u'Plugin for nonebot2 that abstracts statements',
    packages=['nonebot_plugin_abstract'],
    install_requires=["python", "jieba", "pinyin", "nonebot2", "nonebot-adapter-onebot"],
)