#hw code below
#0309hw--------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

username = widgets.Text(
    value='',
    placeholder='請輸入你的名字',
    description='使用者名稱:',
    disabled=False
)
display(username)



Breakfast_dic={"原味蛋餅":"25",
             "起司薯餅蛋餅":"30",
             "肉蛋蔬菜總匯土司":"50",
             "鮪魚蛋餅":"30",
             "蜂蜜法式土司":"20",
             "墨西哥煎雞堡":"60",
             "麥克雞":"55",
             "滷肉飯":"35"
            }
Drink_dic={"紅茶":"25",
             "招牌奶茶":"30",
             "鮮奶茶":"50",
             "無糖綠茶":"30",
             "鮮奶":"20",
             "豆漿":"60",
             "美式咖啡":"55",
             "拿鐵":"35"
            }
Dessert_dic={"香腸":"40",
             "薯餅":"30",
             "小熱狗":"50",
             "雞塊":"30",
             "地瓜球":"20",
             "沙拉":"60",
             "薯餅":"55",
             "起司塔":"35"
            }

breakfast = widgets.Dropdown(
    options=Breakfast_dic.keys(),
    value='原味蛋餅',
    description='早餐主食：',
    disabled=False,
)
breakfast1=widgets.Dropdown(
    options=Breakfast_dic.keys(),
    value='原味蛋餅',
    description='早餐主食：',
    disabled=False
)

nums=123456780
b_num=widgets.Dropdown(
    options= str(nums),
    value='1',
    description='數量：',
    disabled=False
)
dr_num=widgets.Dropdown(
    options= str(nums),
    value='1',
    description='數量：',
    disabled=False
)
des_num=widgets.Dropdown(
    options= str(nums),
    value='1',
    description='數量：',
    disabled=False
)


drink = widgets.RadioButtons(
    options=Drink_dic.keys(),
    value='紅茶',
    description='飲料：',
    disabled=False,
)


dessert = widgets.Select(
    options=Dessert_dic.keys(),
    #value='薯餅',
    description='小點心：',
    disabled=False,
)
dessert_price = Dessert_dic.values()


yes_or_no = widgets.Checkbox(
    #value = True,
    description = "需要袋子？？(加1元)",
    disabled = False
)

breakfastT=widgets.HBox([breakfast,b_num])
drinkT=widgets.HBox([drink,dr_num])
dessertT=widgets.HBox([dessert,des_num])
menu = widgets.Tab([breakfastT,drinkT,dessertT,yes_or_no]) 
menu.set_title(0,"主食")
menu.set_title(1,"飲料")
menu.set_title(2,"小點心")
menu.set_title(3,"袋子?")
display(menu)


btn_checkout = widgets.Button(description="結帳")
out = widgets.Output()

def Checkout(_):
      with out:
        clear_output()
        a=int(Breakfast_dic[breakfast.value])*int(b_num.value)
        b=int(Drink_dic[drink.value])*int(dr_num.value)
        c=int(Dessert_dic[dessert.value])*int(des_num.value)
        
        if yes_or_no.value:
            bagNum=1
        else:
            bagNum=0
        
        order = "你的訂單如下：主食為{}{}份{}元，飲料為{}{}份{}元，小點心是{}{}份{}元! ".format(breakfast.value,b_num.value,a, drink.value,dr_num.value, b, dessert.value,des_num.value,c)
        total=int(a)+int(b)+int(c)+bagNum
        print(order)
        print("共"+str(total)+"元")
        print("請耐心稍候片刻～")
          
            
btn_checkout.on_click(Checkout)
results = widgets.VBox([btn_checkout,out])
results




