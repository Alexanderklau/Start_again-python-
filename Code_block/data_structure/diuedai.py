# -*- coding: utf-8 -*-
__author__ = "Yemilice_lau"
#保存有限几个元素的历史记录

from collections import deque

# def search(lines,pattern,history=5):
#     previous = deque(maxlen=history)
#     for li in lines:
#         if pattern in li:
#             yield li,previous_lines
#         previous_lines.append(li)
#
#

d = {
    'a':[1,2,3],
    'b':[4,5]
}
e = {
    'a':{1,2,3},
    'b':{4,5}
}
from collections import defaultdict
d = defaultdict(list)