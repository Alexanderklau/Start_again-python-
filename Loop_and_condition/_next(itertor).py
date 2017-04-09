# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
myTuple = (123,456,'xtz')
i = iter(myTuple)
print i.next()
print i.next()
print i.next()

fetch = iter(myTuple)
while True:
    try:
        i = fetch.next()
        print i
    except StopIteration:
        break








# if __name__ == '__main__':