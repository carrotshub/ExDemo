# -*- coding: utf8 -*-
# 使用装饰器实现单例模式
# 第一种方法类作为装饰器


class Single(object):
	def __init__(self,cls):
		self._cls = cls
		self._instances = None

	def __call__(self, *args, **kwargs):
		if not self._instances:
			self._instances = self._cls(*args)
		return self._instances


@Single
class A(object):
	def __init__(self,name):
		self.name = name


a = A('zhangsan')
b = A('lisi')

print(a is b)


# 第二种，使用函数作为装饰器

def single1(cls):
	s = []

	def wrapper(*args, **kwargs):
		if not s:
			s.append(cls(*args, **kwargs))
		print(args)
		return s
	return wrapper


@single1
class B(object):
	def __init__(self, name):
		self.name = name


a1 = B('zhangsam')
b1 = B('BOb')
print(a1 is b1)
