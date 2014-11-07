from django.template import Context, Template
t = Template('My name is {{ name }}.')
c = Context({'name': 'nowamagic'})
t.render(c)
u'My name is nowamagic.'
我们必须指出的一点是，t.render(c) 返回的值是一个 Unicode 对象，
不是普通的 Python 字符串。 你可以通过字符串前的 u 来区分。
在框架中，Django 会一直使用 Unicode 对象而不是普通的字符串。
如果你明白这样做给你带来了多大便利的话，
尽可能地感激 Django 在幕后有条不紊地为你所做这这么多工作吧。
如果不明白你从中获益了什么，别担心。你只需要知道 Django 对 Unicode 的支持，
将让你的应用程序轻松地处理各式各样的字符集，而不仅仅是基本的A-Z英文字符。