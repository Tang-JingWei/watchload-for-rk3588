# 项目描述 / Description
本项目提供的python脚本实现可以方便、实时观察 RK3588 平台的 NPU 和 CPU 负载情况的功能，并提供两种显示模式，方便观察负载情况、负载对比。
The python script provided by this project realizes the function of observing the load conditions of the NPU and CPU of the RK3588 platform in real time, and provides two display modes for convenient observation of load conditions and load comparison.
- [x] 终端显示模式 (Terminal display mode)
- [x] matplot绘制模式 (Matplotlib plotting mode)

# 运行画面 / Running Screenshots
<img src="[img/terminal_mode.png](https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/matplot_mode.png)" title="terminal_mode"/>
<img src="[img/matplot_mode.png](https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/terminal_mode.png)" title="matplot_mode"/>


# 使用方法 / Usage
1. 克隆项目 (Clone the project)
```
git clone https://github.com/Tang-JingWei/watchload-for-rk3588.git
```
2. 进入项目目录 (Enter the project directory)
```
cd watchload-for-rk3588
```
3. 使用 ```pip3``` 安装需要的库 (Install the required libraries using ```pip3```)
```
# 如果还没有安装 pip3 请先安装 (If pip3 is not installed, please install it first)
sudo apt install python3-pip

# 安装需要的库 (Install the required libraries)
pip3 install -r requirements.txt
```
4. 运行脚本，需要提供参数 (The script needs to provide parameters)
```
# 查看帮助 (View help)
python3 watchload.py -h 
```
```
# 使用 matplot 绘制模式运行 (Use matplot plotting mode to run)
python3 watchload.py -m g
```
```
# 使用终端显示模式运行 (Use terminal display mode to run)
python3 watchload.py -m t
```

# 异常情况 / Exception
1. 终端窗口太小，无法绘制图形 (The terminal window is too small to draw the graph):
   请适当拉伸窗口 (Please stretch the window appropriately)
<img src="[img/sizeerror.png](https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/sizeerror.png)" title="sizeerror"/>


