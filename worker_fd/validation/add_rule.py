import json
#taskid，columns，

# 1.创建窗口
from tkinter import *

root = Tk()

# 2.窗口标题
root.title('校验规则生成')

# 3.窗口大小以及显示位置,中间是小写的x
root.geometry('500x400+550+230')
# 窗口显示位置
# root.geometry('+573+286')

# 4.标签控件
lable = Label(root, text='请输入任务id', font=('微软雅黑', 10))
lable.grid(row=0, column=0)

taskid = Entry(root, font=('微软雅黑', 15))
taskid.grid(row=0, column=1)


lable = Label(root, text='请输入列名1', font=('微软雅黑', 10))
lable.grid(row=1, column=0)


column1 = Entry(root, font=('微软雅黑', 15))
column1.grid(row=1, column=1)


lable = Label(root, text='empty', font=('微软雅黑', 10))
lable.grid(row=2, column=0)

empty1 = Entry(root, font=('微软雅黑', 15))
empty1.grid(row=2, column=1)


lable = Label(root, text='allowed', font=('微软雅黑', 10))
lable.grid(row=3, column=0)


allowed1 = Entry(root, font=('微软雅黑', 15))
allowed1.grid(row=3, column=1)


lable = Label(root, text='请输入列名2', font=('微软雅黑', 10))
lable.grid(row=4, column=0)


column2 = Entry(root, font=('微软雅黑', 15))
column2.grid(row=4, column=1)


lable = Label(root, text='empty', font=('微软雅黑', 10))
lable.grid(row=5, column=0)

# 5.输入控件
empty2 = Entry(root, font=('微软雅黑', 15))
empty2.grid(row=5, column=1)

lable = Label(root, text='allowed', font=('微软雅黑', 10))
lable.grid(row=6, column=0)

allowed2 = Entry(root, font=('微软雅黑', 15))
allowed2.grid(row=6, column=1)

def add_rule():
    task_id = taskid.get()
    list = []
    list.append(column1.get())
    list.append(column2.get())
    print(list)
    dict1 = {}
    if empty1.get() == 'False':
        dict1['empty'] = False
    else:
        dict1['empty'] = ''
    dict1['allowed'] = allowed1.get()
    print(dict1)
    dict2 = {}
    if empty2.get() == 'False':
        dict2['empty'] = False
    else:
        dict2['empty'] = ''
    dict2['allowed'] = allowed2.get()
    with open('data.json','r') as f:
       data = json.load(f)
       data[task_id] = {}
       for i in range(len(list)):
           if list[i] != '':
               data[task_id][list[i]] = {}
               for k,v in eval('{}'.format('dict'+str(i+1))).items():
                   if v != '':
                       data[task_id][list[i]][k] = v

    with open('data.json','w') as f:
        json.dump(data,f)


# 7.按钮控件
button = Button(root, text='生成校验规则', width=10, font=('微软雅黑', 10),command = add_rule)
button.grid(row=50, column=0, sticky=W)

button1 = Button(root, text='退出', width=10, font=('微软雅黑', 10), command=root.quit)
button1.grid(row=50, column=1, sticky=E)

root.mainloop()
