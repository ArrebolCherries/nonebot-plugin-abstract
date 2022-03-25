import setuptools

setuptools.setup(
    name='nonebot_plugin_abstract',
    version='1.0.1',
    author='CherryCherries',
    author_email='cherrycherries@foxmail.com',
    url='https://github.com/CherryCherries/nonebot-plugin-abstract',
    description="适用于 Nonebot2 的语句抽象化插件",
    long_description=u'适用于 Nonebot2 的语句抽象化插件，可以将你的语句变得抽象起来~',
    packages=setuptools.find_packages(),
    install_requires=[
        "jieba",
        "pinyin"
    ],
)