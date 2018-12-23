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
	@staticmethod
	def get_id():
		print("here is get your id!")


@info
def say(something):
	print("say {}!".format(something))
	def test():
		print('here is a test dome!')
	return test()


say('hello world!')
say('I am a test!')
say("submit")
