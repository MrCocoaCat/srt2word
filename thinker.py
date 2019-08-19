import tkinter
from tkinter import filedialog
from tkinter import Frame
from tkinter import *
from file import cover
import os, time
from multiprocessing import Pool
from multiprocessing import cpu_count
from tkinter import messagebox
import winreg
from multiprocessing import freeze_support

ProcessNum = cpu_count()

filenames = {}


def select_RST():
    global filenames
    filenames = filedialog.askopenfilenames(filetypes=[("text file", "*.srt"), ("all", "*.*")],
                                            initialdir=get_desktop())
    print(filenames)
    names.set(filenames)


def selectPath_Word():
    path_ = filedialog.askdirectory (initialdir=get_desktop())
    path_2.set(path_)


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    print(key)
    return winreg.QueryValueEx(key, "Desktop")[0]


def do_file():
    #dirpath = path_1.get()
    out_dirpath=path_2.get()
    start = time.time()
    #os.path.isdir(dirpath)
    if not os.path.isdir(out_dirpath):
        os.makedirs(out_dirpath)
    #lit = os.listdir(dirpath)
    print('Parent process %s. strat pool of %s ' % (os.getpid(), ProcessNum))
    for i in filenames:
        p.apply_async(cover, args=(i, out_dirpath))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    end = time.time()
    print('All subprocesses done  %0.2f seconds.' % (end - start))
    messagebox.showinfo("srt 转换工具", "转换完成 ")


if __name__ == '__main__':
    freeze_support()

    p = Pool(ProcessNum)
    root = tkinter.Tk()
    root.title("srt 转换工具")

    path_2 = StringVar()
    names = StringVar()
    frame1 = Frame(root)

    # btn1 = tkinter.Button(root, text='RST 文件目录', command=openfile)
    # btn2 = tkinter.Button(root, text='WORD 文件目录', command=savefile)
    # btn3 = tkinter.Button(root, text='运行', command=do)
    #
    # btn1.pack(side='left')
    # btn2.pack(side='left')
    # btn3.pack(side='right')
    #
    # frame1.pack(padx=10, pady=10)

    Label(root, text='SRT路径：').grid(row = 0,column = 0)
    #Entry(root,textvariable=names).grid(row = 0,column = 1)
    Button(root, text='文件选择：', command=select_RST).grid(row=0, column=2)

    Label(root, text='WORD路径：').grid(row=1,column=0)
    Entry(root, textvariable=path_2, width=90, ).grid(row=1, column=1)
    Button(root, text='路径选择：', command=selectPath_Word).grid(row=1, column=2)

    #lbv = tkinter.StringVar()
    a = Listbox(root, selectmode=tkinter.SINGLE, listvariable=names, width=90, height=15,).grid(row=0, column=1, sticky=W+E+N+S)
    #for item in filenames:
    #    lb.insert(tkinter.END, item)

    #sc = Scrollbar(a)
    #sc.pack(side=RIGHT, fill=Y)

    Button(root, text="开始转换", command=do_file).grid(row=3, column=1)
    root.mainloop()
