#使用辗转相除法求多个数字的最大公约数
from functools import reduce

def spread(*args):
    ret=[]
    for i in args:
        if isinstance(i,list):
            ret.extend(i)
        else:
            ret.append(i)            
    return ret
    
def gcd(*args):
    numbers=[]
    numbers.extend(spread(list(args)))
    
    
    def _gcd(x,y):
        return x if not y else gcd(y,x % y)
        
    return reduce((lambda x,y: _gcd(x,y)), numbers)
    
print(gcd(120,168,328,624,320))


#通过辗转相除来计算两个数的最大公约数
def doublegcd(x,y):
    return x if not y else doublegcd(y,x % y)
print(doublegcd(27,51))


print('这是一个测试语句')