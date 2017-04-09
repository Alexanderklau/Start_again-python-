# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
rows = [1,2,3,17]
def cols():
    yield 566
    yield 2
    yield 1
x = ((i,j) for i in rows for j in cols())
for pair in x:
    print pair









# if __name__ == '__main__':