from ping3 import ping
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pynput import keyboard

WIDTH = 50     # 同时显示的 ping 次数
PAUSE = 0.45   # ping 间隔
TIMEOUT = 1    # ping 超时时间
a, n = {}, 0

fig = plt.figure(figsize=(9, 3), dpi=120)
plt.suptitle('Ping')
fig.canvas.manager.set_window_title('Pinger')
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
test = 500    # stop after <test> times

def on_press(key):
    global test
    if key == keyboard.Key.esc:
        test = -1000
        plt.close("all")
        return False
listener = keyboard.Listener(on_press=on_press)
listener.start()

while test > 0:
    test -= 1
    s = ping("www.baidu.com", timeout=TIMEOUT)
    if (s is None):
        s = TIMEOUT
    n += 1
    a[n] = round(s * 1000)

    if (n >= WIDTH):
        a.pop(n - WIDTH + 1)

    ave = sum(a.values()) / len(a)
    plt.clf()
    plt.plot(a.keys(), [ave] * len(a), color="orange", label='average')
    plt.plot(a.keys(), a.values(), color="blue", label='ping')
    # plt.plot(
    #     [],[],
    #     label = 'instability' + '%.2f' %sta +'%')
    plt.xlabel('times')
    plt.ylabel('ms')
    plt.legend()
    plt.pause(PAUSE)
