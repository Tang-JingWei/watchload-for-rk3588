#!/usr/bin/env python3

import subprocess
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import psutil
import argparse
import curses
import time
import traceback


logo = [
 "===========================================================",
 "||        __  __             _ _                         ||",
 "||       |  \/  | ___  _ __ (_) |_ ___  _ __             ||",
 "||       | |\/| |/ _ \| '_ \| | __/ _ \| '__|            ||",
 "||       | |  | | (_) | | | | | || (_) | |               ||",
 "||       |_|  |_|\___/|_| |_|_|\__\___/|_|    V1.4       ||",
 "||                                                       ||",
 "||        Author: https://github.com/Tang-JingWei        ||",
 "||                                                       ||",
 "|=========================================================|",
]


# 获取 NPU 负载的函数
def get_npu_load():
    # 执行命令获取输出字符串
    result = subprocess.run(['sudo', 'cat', '/sys/kernel/debug/rknpu/load'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()

    # 使用正则表达式提取负载数据
    try:
        # 正则匹配 Core0、Core1、Core2 的百分比
        load_data = re.findall(r'Core\d+: *(\d+)%', output)
        if len(load_data) == 3:
            # 返回三个核心的负载
            return list(map(int, load_data))
        else:
            print("Error: Could not parse all core loads")
            return 0, 0, 0
    except Exception as e:
        print("Error parsing load data:", e)
        return 0, 0, 0

# 获取 CPU 负载的函数
def get_cpu_load():
    # 获取每个核心的 CPU 使用率
    cpu_percent = psutil.cpu_percent(percpu=True)
    return cpu_percent

def get_npudriver_version():
    npuversion_str = subprocess.run(['sudo', 'cat', '/sys/kernel/debug/rknpu/version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    # return npuversion.stdout.decode('utf-8')

    # 使用正则表达式匹配版本号
    version_match = re.search(r'RKNPU driver: v(\d+\.\d+\.\d+)', npuversion_str)
    if version_match:
        version = version_match.group(1)
        return version
        
    else:
        return "Version not found"

def get_memory_usage():
    mem_info = psutil.virtual_memory()
    memory_usage_percent = mem_info.percent
    return memory_usage_percent

# 更新函数，用于实时更新图表
def matplotShow(frame):
    # 获取 NPU 负载
    npu_load = get_npu_load()
    for i, bar in enumerate(bar_npu):
        if npu_load[i] > 50:
            bar.set_color('red')
        else:
            bar.set_color('green')
        bar.set_height(npu_load[i])

    # 获取 CPU 负载
    cpu_load = get_cpu_load()
    for i, bar in enumerate(bar_cpu):
        if cpu_load[i] > 50:
            bar.set_color('red')
        else:
            bar.set_color('green')
        bar.set_height(cpu_load[i])

    return bar_npu + bar_cpu  # 返回更新后的条形图

# 绘制终端中条形图的函数
def draw_bar(win, y, x, value, label, max_width=40):
    bar_length = int((value / 100) * max_width)
    color = 1 if value < 50 else 2  # 确定条形图颜色: 低于 50% 使用颜色1，其他使用颜色2
    win.addstr(y, x, label + ": " + f"{value}% | ".rjust(9))
    win.addstr(y, x + len(label) + 11, "▩" * bar_length, curses.color_pair(color))
    win.addstr(y, x + len(label) + 11 + bar_length, " " * (max_width - bar_length))
    win.addstr(y, x + len(label) + 11 + max_width + 1, "|")

def draw_bar_vertical(win, flag, y, x, value, colorid, ch):
    if flag == 0 :
        for i in range(value):
            if colorid != 0 :
                win.addstr(y + i, x, ch, curses.color_pair(colorid))
            else :
                win.addstr(y + i, x, ch) # 0 默认色
    elif flag == 1:
        for i in range(value):
            if colorid != 0 :
                win.addstr(y - i, x, ch, curses.color_pair(colorid))
            else :
                win.addstr(y - i, x, ch) # 0 默认色

# 绘制 logo 的函数
def draw_logo(stdscr):
    for i, line in enumerate(logo):
        stdscr.addstr(i, 2, line)

def terminalShow(stdscr):
    curses.curs_set(0)  # 不显示光标
    stdscr.nodelay(1)   # 不等待输入
    stdscr.timeout(500)  # 更新间隔时间

    # 初始化颜色
    curses.start_color() 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # 负载低于 50% 使用绿色
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # 负载高于 50% 使用红色
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  

    while True:
        try:
            height, width = stdscr.getmaxyx()

            # 获取 NPU 和 CPU 负载数据
            npu_load = get_npu_load()
            cpu_load = get_cpu_load()
            npu_driver_version = get_npudriver_version()

            # 清空屏幕
            stdscr.clear()

            # 绘制 logo
            draw_logo(stdscr)

            # 绘制 NPU 驱动版本
            npu_driver_version = "RKNPU driver: v" + npu_driver_version
            npu_driver_str = npu_driver_version.center(57)
            stdscr.addstr(len(logo)+0, 2, "|" + npu_driver_str + "|")
            
            offset = 1

            # 绘制 NPU 负载
            stdscr.addstr(len(logo)+offset+0, 2, "|---------------------------------------------------------|")
            stdscr.addstr(len(logo)+offset+1, 2, "| NPU Load per Core:                                      |")
            stdscr.addstr(len(logo)+offset+2, 2, "|---------------------------------------------------------|")
            for i, load in enumerate(npu_load):
                draw_bar(stdscr, len(logo)+offset+3 + i, 2, load, f"| NPU{i}")

            # 绘制 CPU 负载
            stdscr.addstr(len(logo)+offset+6, 2, "|---------------------------------------------------------|")
            stdscr.addstr(len(logo)+offset+7, 2, "| CPU Load per Core:                                      |")
            stdscr.addstr(len(logo)+offset+8, 2, "|---------------------------------------------------------|")
            for i, load in enumerate(cpu_load[:8]):  # 只显示前 8 个核心
                draw_bar(stdscr, len(logo)+offset+9 + i, 2, load, f"| CPU{i+1}")
            stdscr.addstr(len(logo)+offset+17, 2, "-----------------------------------------------------------")

            # 绘制内存使用情况
            draw_bar_vertical(stdscr, 0, 1, 61, len(logo)+offset+16, 0, "|")
            memory_usage_percent = get_memory_usage()
            stdscr.addstr(0, 61, "=====")
            # 在条形图顶部显示标签 占用数据
            stdscr.addstr(1, 62, f"{(int)(memory_usage_percent)}%".center(4))
            # win.addstr(max_height - bar_height, x-1, f"{value}%".rjust(5)) 
            # 在条形图底部显示标签 MEM
            stdscr.addstr(len(logo)+offset+15, 62, "===")
            stdscr.addstr(len(logo)+offset+16, 62, "MEM")
            stdscr.addstr(len(logo)+offset+17, 61, "-----")
            draw_bar_vertical(stdscr, 0, 1, 65, len(logo)+offset+16, 0, "|")
            draw_bar_vertical(stdscr, 1, len(logo)+offset+14, 62, (int)(memory_usage_percent * (len(logo)+offset+13) / 100), (1 if memory_usage_percent < 50 else 2) , '▓▓▓')

            # 绘制用法
            stdscr.addstr(len(logo)+offset+18, 22, "press 'q' to exit", curses.color_pair(3))

            # 刷新屏幕
            stdscr.refresh()

            # 检查是否按下 'q' 键退出
            key = stdscr.getch()
            if key == ord('q'):
                break

            time.sleep(1)
        except Exception as e:
            stdscr.clear()
            tb = traceback.format_exc()
            stdscr.addstr(0, 0, "press 'q' to exit", curses.color_pair(3))
            stdscr.addstr(2, 0, "|| 可能因为窗口大小不足，请调整窗口大小。\n|| Maybe The window size is insufficient to draw. Please adjust the window size.")
            stdscr.addstr(5, 0, f"error: {tb}")
            
            stdscr.refresh()
            time.sleep(1)  # 等待1秒，让用户看到提示

            # 检查是否按下 'q' 键退出
            key = stdscr.getch()
            if key == ord('q'):
                break

            continue


parser = argparse.ArgumentParser(description='根据参数选择运行方式: 终端或者图形化')
parser.add_argument('--mode', '-m', type=str, help='运行方式, 可以是 "t (terminal)" 或者 "g (graph)"')
args = parser.parse_args()

if __name__ == "__main__":
    if args.mode == "t":
        curses.wrapper(terminalShow)
    elif args.mode == "g":
        # 初始化图形
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

        npu_driver_version = get_npudriver_version()

        # 设置 NPU 负载图
        ax1.set_ylim(0, 100)
        ax1.set_xlim(-0.5, 2.5)
        ax1.set_xticks([0, 1, 2])
        ax1.set_xticklabels(['Core0', 'Core1', 'Core2'])
        ax1.set_title("(RKNPU driver: v" + npu_driver_version + ') NPU Load per Core')
        bar_npu = ax1.bar([0, 1, 2], [0, 0, 0], width=0.6)

        # 设置 CPU 负载图，8 个 CPU 核心
        ax2.set_ylim(0, 100)
        ax2.set_xlim(-0.5, 7.5)  # 8 个核心
        ax2.set_xticks(range(8))
        ax2.set_xticklabels([f'CPU{i+1}' for i in range(8)])  # CPU1, CPU2, ..., CPU8
        ax2.set_title('CPU Load per Core')
        bar_cpu = ax2.bar(range(8), [0]*8, width=0.6)

        # 动画设置
        ani = FuncAnimation(fig, matplotShow, blit=True, interval=500)

        # 显示图形
        plt.tight_layout()
        plt.show()
    else :
        print("[Error] ==> Please use 't' for terminal or 'g' for graph, example:\npython3 watchload.py -m t\npython3 watchload.py -m g")