# -*- coding: utf-8 -*-
__author__ = "Yemilice_lau"
statck = []
def pushit():
    statck.append(raw_input('Enter New string: ').strip())

def popit():
    if len(statck) == 0:
        print 'Cannot pop from an empty stack!'
    else:
        print 'Removed [', 'stack.pop()',']'
def viewStack():
    print statck
CMDS = {'u':pushit,'o':popit,'v':viewStack}

def showmenu():
    pr="""
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    Enter choice:"""
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print  '\nYou picked:[%s]' % choice
            if choice not in 'uovq':
                print 'Invalid option try again'
            else:
                break
        if choice == 'q':
            break
        CMDS[choice]()

if __name__ == '__main__':
    showmenu()