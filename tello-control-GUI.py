# python3

import sys
import threading
import time
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import Perimeter_Sweep
from main_tello import Tello

# from easytello import Tello


# my_drone = tello.Tello()


tello = Tello('192.168.10.1', True, True)


def sweep_path():
    global tello
    tello.set_interrupt(False)
    Perimeter_Sweep.main(tello)

def send(command):
    tello.send_command(command)

def interrupt():
    tello.set_interrupt(True)

# tello.get_battery()
# tello get_battery
# tello.streamon()


d = '20'
a = '1'

root = tk.Tk()
root.geometry("800x600+100+50")
root.title('Tello Drone Control')

frame0 = tk.Frame(root, width=800, height=20)
frame_scale = tk.Frame(root)

frame12 = tk.Frame(root)
frame1 = tk.Frame(frame12)
frame2 = tk.Frame(frame12)

frame_flip = tk.Frame(root)
print('gui')

button_command = ttk.Button(frame0, text='command', width=10, command=lambda: threading.Thread(
    target=tello.send_command, args=('command',)).start()).grid(row=0, column=0, padx=90, pady=10)

button_takeoff = ttk.Button(frame0, text='takeoff', width=10, command=lambda: threading.Thread(
    target=tello.send_command, args=('takeoff',)).start()).grid(row=0, column=1, padx=90, pady=10)

button_land = ttk.Button(frame0, text='land', width=10, command=lambda: threading.Thread(
    target=tello.send_command, args=('land',)).start()).grid(row=0, column=2, padx=90, pady=10)


button_sweep = ttk.Button(frame0, text='sweep', width=10, command=lambda: threading.Thread(
    target=sweep_path).start()).grid(row=1, column=0, padx=90, pady=10)

button_streamon = ttk.Button(frame0, text='stream on', width=10, command=lambda: threading.Thread(
    target=tello.streamon).start()).grid(row=1, column=1, padx=90, pady=10)

button_streamoff = ttk.Button(frame0, text='streamoff', width=10, command=lambda: threading.Thread(
    target=tello.streamoff).start()).grid(row=1, column=2, padx=90, pady=10)


# buttons to get stat
button_battery = ttk.Button(frame0, text='battery', width=10, command=lambda: tello.get_battery()
                            ).grid(row=2, column=0, padx=90, pady=10)

button_speed = ttk.Button(frame0, text='speed', width=10, command=lambda: tello.get_speed()
                          ).grid(row=2, column=1, padx=90, pady=10)

button_height = ttk.Button(frame0, text='height', width=10, command=lambda: tello.get_height(
)).grid(row=2, column=2, padx=90, pady=10)

# buttons to control flying forward, back, left and right
button_forward = ttk.Button(frame1, text='forward',  width=8,
                            command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'forward {d}',)).start()).grid(row=0, column=1)

button_back = ttk.Button(frame1, text='back',  width=8,
                         command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'back {d}',)).start()).grid(row=2, column=1)

button_left = ttk.Button(frame1, text='left',  width=8,
                         command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'left {d}',)).start()).grid(row=1, column=0)

button_right = ttk.Button(frame1, text='right',  width=8,
                          command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'right {d}',)).start()).grid(row=1, column=2)

# buttons to control flying up, down, spin left and spin right
button_up = ttk.Button(frame2, text='up',  width=8,
                       command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'up {d}',)).start()).grid(row=0, column=1)

button_down = ttk.Button(frame2, text='down',  width=8,
                         command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'down {d}',)).start()).grid(row=2, column=1)

button_spinleft = ttk.Button(frame2, text='spin left',  width=8,
                             command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'cw {a}',)).start()).grid(row=1, column=0)

button_spinright = ttk.Button(frame2, text='spin right',  width=8,
                              command=lambda: threading.Thread(
                                target=tello.send_command, args=(f'ccw {a}',)).start()).grid(row=1, column=2)

# buttons to control flipping forward, back, left and right
button_flip_f = ttk.Button(frame_flip, text='flip forward',  width=10,
                           command=lambda: threading.Thread(
                                target=tello.send_command, args=('flip f',)).start()).grid(row=0, column=1)

button_flip_b = ttk.Button(frame_flip, text='flip back',  width=10,
                           command=lambda: threading.Thread(
                                target=tello.send_command, args=('flip b',)).start()).grid(row=2, column=1)

button_flip_l = ttk.Button(frame_flip, text='flip left',  width=10,
                           command=lambda: threading.Thread(
                                target=tello.send_command, args=('flip l',)).start()).grid(row=1, column=0)

button_flip_r = ttk.Button(frame_flip, text='flip right',  width=10,
                           command=lambda: threading.Thread(
                                target=tello.send_command, args=('flip r',)).start()).grid(row=1, column=2)

button_interrupt = ttk.Button(frame_flip, text='Interrupt', width=10,
                              command=lambda: threading.Thread(target=interrupt).start()).grid(row=3, column=1, pady=20)

# scrollbar to set the angle to rotate
angle_scroll = tk.Scale(frame_scale, from_=1, to=360,
                        orient=tk.HORIZONTAL, tickinterval=60, resolution=1, length=200)
angle_scroll.grid(row=0, column=1, padx=95)


def angle_change():
    global a
    print("HERER angle_change")
    a = str(angle_scroll.get())
    print('rotate angle set: ', a)


angle = ttk.Button(frame_scale, text='angle confirm', command=lambda: threading.Thread(target=angle_change).start())
angle.grid(row=1, column=1, padx=4)

# scrollbar to set the distance to fly
distance_change = tk.Scale(frame_scale, from_=20, to=500,
                           orient=tk.HORIZONTAL, tickinterval=100, resolution=10, length=200)
distance_change.grid(row=0, column=0, padx=95)


def speed_change():
    global d
    print("HERER speed_change")
    d = str(distance_change.get())
    print('flying distance set: ', d)


distance = ttk.Button(
    frame_scale, text='distance confirm', command=lambda: threading.Thread(target=speed_change).start())
distance.grid(row=1, column=0, padx=4)


frame0.pack()
frame_scale.pack(pady=20)
frame1.grid(row=0, column=0, padx=80)
frame2.grid(row=0, column=1, padx=80)
frame12.pack(pady=0)
frame_flip.pack(pady=30)

tk.mainloop()
