# -*- coding: utf-8 -*-
# 这是一个类装饰器
class info(object):
	def __init__(self,func):
		self.func = func
		# self.name = name

	def __call__(self, *args, **kwargs):
		print("[DEBUG] enter function {func}()".format(func=self.func.__name__))
		print("func:\'{func}\' say : {something}".format(func=self.func.__name__, something=args[0]))
		return self.func(*args, **kwargs)
	# @staticmethod
	# def get_id():
	# 	print("here is get your id!")


@info
def say(something):
	print("say {}!".format(something))
	def test():
		print('here is a test dome!')
		# return something()
	# 这里再装饰器情况下返回的是函数名字，但是在该函数所在的函数仅作为悲壮是函数的时候注意一定以函数调用的形式返回
	return test


@say
def test_timer():
	for i in range(100):
		print(i, end='')


# say('hello world!')
# say('I am a test!')
test_timer()
