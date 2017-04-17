# -×- coding: utf-8 -*-
__author__ = "Yemilice_lau"
from time import ctime,sleep

def tsf(func):
    def wrappen():
        print '[%s] %s() called' % (
            ctime(),func.__name__ )
        return func()
    return wrappen()

@tsf
def foo():
    print '123'



foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
