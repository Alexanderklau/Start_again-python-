# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
print map(lambda x:x ** 2 ,range(6))
def odd(n):
    return n % 2
print odd(125)

seq = [1,2,3,4,5,6,7,8,9]
# filter判断是否是奇数
print filter(lambda x :x % 2,seq)
print [x for x in seq if x % 2]
print [(x+1,y+1) for x in range(10) for y in range(10)]





# if __name__ == '__main__':