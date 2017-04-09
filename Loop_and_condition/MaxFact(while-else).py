# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' %(num,count)
            break
        count -= 1
    else:
        print num,"is prime"

for eachnum in range(1,100):
    showMaxFactor(eachnum)








# if __name__ == '__main__':