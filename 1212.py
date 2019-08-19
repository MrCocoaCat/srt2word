import tkinter

win = tkinter.Tk()
win.title("yudanqu")
win.geometry("400x400+200+50")

# 绑定变量
lbv = tkinter.StringVar()

# 与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
lb.pack()

for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
 # 按顺序添加
    lb.insert(tkinter.END, item)

# 打印当前列表中的选型
print(lbv.get())

# 设置选项
# lbv.set(("1","2","3"))

# 绑定事件
def myprint(event):
    # print(lb.curselection()) # 返回下标
    print(lb.get(lb.curselection())) # 返回值
lb.bind("<Double-Button-1>", myprint)

win.mainloop()