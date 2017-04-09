# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
num = input('Enter number:>')
count = num / 2
while count > 0:
    if num % count == 0:
        print count,'is the largest factor of',num
        break
    else:
        print 'bad!'
        break
    count -= 1










# if __name__ == '__main__':