# -*- coding: utf-8 -*-
__author__ = "Yemilice_lau"
def hello(name):
    return 'Hello. ' + name + '!'
hello('liu')

def store(data,full_name):
    names = full_name.split()
    if len(names) == 2:names.insert(1,'')
    labels = 'first','middle','last'
    for labels,name in zip(labels,names):
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
