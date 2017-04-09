# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
passwdList = [
    '123',
    '456',
    '789']
valid = False
count = 3
while count > 0:
    input = raw_input("Enter password")
    for eachpassword in passwdList:
        if input == eachpassword:
            valid = True
            break
    if not valid:
        print "Bad!"
        count -= 1
        continue
    else:
        break









# if __name__ == '__main__':