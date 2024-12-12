# 项目描述 / Description
本项目提供的python脚本实现可以方便、实时观察 RK3588 平台的 NPU 和 CPU 负载情况的功能，并提供两种显示模式，方便观察负载情况、负载对比。
The python script provided by this project realizes the function of observing the load conditions of the NPU and CPU of the RK3588 platform in real time, and provides two display modes for convenient observation of load conditions and load comparison.
- [x] 终端显示模式 (Terminal display mode)
- [x] matplot绘制模式 (Matplotlib plotting mode)

# 运行画面 / Running Screenshots
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/terminal_mode.png" title="terminal_mode"/>
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/matplot_mode.png" title="matplot_mode"/>


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
5. 当然，这样运行python脚本并不是一种很方便的方法，所以在 V1.2版本 中加入了 ```watchload``` 脚本，你只需要做一些简单的设置就可以在任意目录下使用该监测功能 (In V1.2 version, the ```watchload``` script is added, and you only need to make a few simple settings to run the monitoring function in any directory)
```
# 首先，编辑 ~/.bashrc 文件，在文件末尾添加 watchload-for-rk3588 项目目录路径。 (First, edit the ~/.bashrc file and add the path of the watchload-for-rk3588 project directory to the end of the file.)
sudo nano ~/.bashrc
export PATH="/path/to/the/watchload-for-rk3588:$PATH"
source ~/.bashrc
```
```
# 给脚本赋予可执行权限 (Give the script executable permissions)
sudo chmod +x watchload
```
```
# 运行 watchload 脚本，同样的，需要指定参数 -t 或者 -g (The same as the python script, you need to specify the parameter -t or -g)
watchload -t
watchload -g
```

# 更新历史
1. v1.0: 
   1. 初始版本 (Initial version)
2. v1.1: 
   1. 增加显示 RKNPU driver 版本信息 (Add display of RKNPU driver version information)
   2. 优化代码结构 (Optimize code structure)
3. v1.2:
   1. 增加 watchload 脚本，方便在任意目录处都可以调出监视器 (Add watchload script, which can be called up in any directory)

# 异常情况 / Exception
1. 终端窗口太小，无法绘制图形 (The terminal window is too small to draw the graph):
   请适当拉伸窗口 (Please stretch the window appropriately)
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/sizeerror.png" title="sizeerror"/>


