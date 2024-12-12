# ��Ŀ���� / Description
����Ŀ�ṩ��python�ű�ʵ�ֿ��Է��㡢ʵʱ�۲� RK3588 ƽ̨�� NPU �� CPU ��������Ĺ��ܣ����ṩ������ʾģʽ������۲츺����������ضԱȡ�
The python script provided by this project realizes the function of observing the load conditions of the NPU and CPU of the RK3588 platform in real time, and provides two display modes for convenient observation of load conditions and load comparison.
- [x] �ն���ʾģʽ (Terminal display mode)
- [x] matplot����ģʽ (Matplotlib plotting mode)

# ���л��� / Running Screenshots
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/terminal_mode.png" title="terminal_mode"/>
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/matplot_mode.png" title="matplot_mode"/>


# ʹ�÷��� / Usage
1. ��¡��Ŀ (Clone the project)
```
git clone https://github.com/Tang-JingWei/watchload-for-rk3588.git
```
2. ������ĿĿ¼ (Enter the project directory)
```
cd watchload-for-rk3588
```
3. ʹ�� ```pip3``` ��װ��Ҫ�Ŀ� (Install the required libraries using ```pip3```)
```
# �����û�а�װ pip3 ���Ȱ�װ (If pip3 is not installed, please install it first)
sudo apt install python3-pip

# ��װ��Ҫ�Ŀ� (Install the required libraries)
pip3 install -r requirements.txt
```
4. ���нű�����Ҫ�ṩ���� (The script needs to provide parameters)
```
# �鿴���� (View help)
python3 watchload.py -h 
```
```
# ʹ�� matplot ����ģʽ���� (Use matplot plotting mode to run)
python3 watchload.py -m g
```
```
# ʹ���ն���ʾģʽ���� (Use terminal display mode to run)
python3 watchload.py -m t
```
5. ��Ȼ����������python�ű�������һ�ֺܷ���ķ����������� V1.2�汾 �м����� ```watchload``` �ű�����ֻ��Ҫ��һЩ�򵥵����þͿ���������Ŀ¼��ʹ�øü�⹦�� (In V1.2 version, the ```watchload``` script is added, and you only need to make a few simple settings to run the monitoring function in any directory)
```
# ���ȣ��༭ ~/.bashrc �ļ������ļ�ĩβ��� watchload-for-rk3588 ��ĿĿ¼·���� (First, edit the ~/.bashrc file and add the path of the watchload-for-rk3588 project directory to the end of the file.)
sudo nano ~/.bashrc
export PATH="/path/to/the/watchload-for-rk3588:$PATH"
source ~/.bashrc
```
```
# ���ű������ִ��Ȩ�� (Give the script executable permissions)
sudo chmod +x watchload
```
```
# ���� watchload �ű���ͬ���ģ���Ҫָ������ -t ���� -g (The same as the python script, you need to specify the parameter -t or -g)
watchload -t
watchload -g
```

# ������ʷ
1. v1.0: 
   1. ��ʼ�汾 (Initial version)
2. v1.1: 
   1. ������ʾ RKNPU driver �汾��Ϣ (Add display of RKNPU driver version information)
   2. �Ż�����ṹ (Optimize code structure)
3. v1.2:
   1. ���� watchload �ű�������������Ŀ¼�������Ե��������� (Add watchload script, which can be called up in any directory)

# �쳣��� / Exception
1. �ն˴���̫С���޷�����ͼ�� (The terminal window is too small to draw the graph):
   ���ʵ����촰�� (Please stretch the window appropriately)
<img src="https://github.com/Tang-JingWei/watchload-for-rk3588/blob/master/imgs/sizeerror.png" title="sizeerror"/>


