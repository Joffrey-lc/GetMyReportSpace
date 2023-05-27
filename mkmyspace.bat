rem  mkmyspace.bat make my report workspace automatically.
rem  Joffrey lc 2023.05.27
chcp 65001
@echo off
set loc_path=%cd%
E: 
rem cd to the path of python code
cd E:\CODESPACE\pycharmworkspace\workplace\工具测试\makeDirTools
rem activate the python envs
call activate D:\anaconda\envs\mypytorch
rem mk my space !!
python mymain.py --dirpath %loc_path%
