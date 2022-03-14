#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:59:27 2022

@author: hanklin
"""


#0302 hw python-----------------------------------------

'''
lucky_number = input("隨機輸入你今日的幸運數字:")
while not str.isdigit(lucky_number):
    lucky_number = input("Not number, please enter again:")
if int(lucky_number)%3==0:
    print("大吉大利，今晚吃雞")
elif int(lucky_number)%3==1:
    print("本日小吉，不會被吉")
else:
    print("本日吉。")

'''

#if 與 else if 會因為當 if 判斷正確之後直接跳過 else if 部分的判斷
#在特別條件下會有問題，例如 if x>50 if x>100，當x=110，兩者都會被判斷到，而在 if x>50 elseif x>100
#則在if x>50時，就會判斷，且跳過elseif x>100

'''
x=int(input())

if x>50:
    print("a")
elif x>100:
    print("b") 

if x>50:
    print("c")
if x>100:
    print("d") 
'''


#--------------------------------------------------------

#0309hw--------------------------------------------------

# Spyder imports

import ipywidgets as widgets
from IPython.display import display, clear_output


# Dropdown

breakfast = widgets.Dropdown(
    options=['原味蛋餅', '起司薯餅蛋餅', '肉蛋蔬菜總匯土司',
            '鮪魚蛋餅', '蜂蜜法式土司', '墨西哥煎雞堡' , '麥克雞', '滷肉飯'],
    value='原味蛋餅',
    description='早餐主食：',
    disabled=False,
)
display(breakfast) #breakfast.valueee































