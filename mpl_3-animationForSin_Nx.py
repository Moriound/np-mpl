import random
import threading
import time
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.geometry("700x700")
can = tk.Canvas(width=600, height=600, bg='lightgreen')
can.place(x=0, y=0)
btn = tk.Button(text='start', font=("", 12, ""))
btn.place(x=600, y=660)

x = np.linspace(0, np.pi * 2, 200)


def drawFlowers():
    # global num
    st = time.time()
    for num in np.arange(0, 199, 0.1):
        ax.clear()
        ax.set_title("ρ=sin(nθ)")
        ax.grid(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.plot(x, np.sin(num * x), color='red')
        ax.fill(x, np.sin(num * x), alpha=0.8, color='pink')
        print(num)
        can_plt.draw()

    et = time.time()
    print(et - st)
    btn.config(state='normal')

# 多线程
def subTreading():
    threading.Thread(target=drawFlowers, daemon=True).start()
    btn.config(state='disabled')


fig = plt.figure(1, figsize=(7, 7))

ax = plt.subplot(projection='polar')
ax.set_title("ρ=sin(nθ)")
ax.grid(False)
ax.set_xticklabels([])
ax.set_yticklabels([])

# 将plot绘制传递至tk的画布上
can_plt = FigureCanvasTkAgg(fig, master=can)
can_plt.draw()
can_plt.get_tk_widget().pack()


btn.config(command=subTreading)

root.mainloop()
