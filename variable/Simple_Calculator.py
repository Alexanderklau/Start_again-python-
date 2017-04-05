# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
princle = 1000

rate = 0.5

numyears = 5  # 计算次数

year = 1

while year <= numyears:
    princle = princle * (1 + rate)
    print year,princle
    year += 1










# if __name__ == '__main__':