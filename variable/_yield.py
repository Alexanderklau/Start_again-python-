# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
def custdown(n):
    print "Counting down!"
    while n > 0:
        yield n
        n -= 1
c = custdown(5)
c.next()








# if __name__ == '__main__':