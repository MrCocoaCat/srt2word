import tkinter
from tkinter import filedialog
from tkinter import Frame
from tkinter import *
from file import cover
import os, time
from multiprocessing import Pool,Queue
from multiprocessing import cpu_count
from tkinter import messagebox
import winreg
from multiprocessing import freeze_support

ProcessNum = cpu_count()

# filenames = {}
finepath_queue = Queue(200)


def select_srt():
    global filenames
    ret = filedialog.askopenfilenames(filetypes=[("text file", "*.srt"), ("all", "*.*")],
                                            initialdir=get_desktop())
    print(ret)
    filenames = list(ret)
    #print(type(filenames_set))
    names.set(filenames)


def select_word():
    path_ = filedialog.askdirectory (initialdir=get_desktop())
    path_2.set(path_)


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    print(key)
    return winreg.QueryValueEx(key, "Desktop")[0]


def do_file():
    out_dirpath=path_2.get()
    start = time.time()
    l = []
    if not os.path.isdir(out_dirpath):
        os.makedirs(out_dirpath)
    print('Parent process %s. strat pool of %s ' % (os.getpid(), ProcessNum))
    for i in filenames:
        res = p.apply_async(cover, args=(i, out_dirpath))
        done_file = res.get()
        l.append(done_file)


    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    end = time.time()
    error = list(set(filenames)-set(l))
    names.set(error)
    print('All subprocesses done  %0.2f seconds.' % (end - start))

    messagebox.showinfo("srt 转换工具", "转换完成 ")

# pyinstaller -w -F -i favicon-20190819102026367.ico main.py -n srt


if __name__ == '__main__':
    freeze_support()

    p = Pool(ProcessNum)
    root = tkinter.Tk()
    root.title("srt 转换工具 1.1")

    path_2 = StringVar()
    # srt 文件名
    names = StringVar()
    frame1 = Frame(root)

    Label(root, text='SRT路径：').grid(row=0, column=0)
    Listbox(root, selectmode=tkinter.SINGLE, listvariable=names, width=90, height=15, ).grid(row=0, column=1)
    Button(root, text='文件选择：', command=select_srt).grid(row=0, column=2)

    Label(root, text='WORD路径：').grid(row=1, column=0)
    Entry(root, textvariable=path_2, width=90, ).grid(row=1, column=1)
    Button(root, text='路径选择：', command=select_word).grid(row=1, column=2)

    Button(root, text="开始转换", command=do_file).grid(row=3, column=1)

    root.mainloop()

