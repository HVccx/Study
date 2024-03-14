@echo off
REM 输出文件的路径和文件名
SET OutputFile=info.txt
echo ===========本机信息=========== > %OutputFile%
REM 本机信息
systeminfo >> %OutputFile%

echo ===========网络信息=========== >> %OutputFile%
REM 创建或覆盖文件，写入IP配置信息
ipconfig /all >> %OutputFile%

REM 可选：向文件追加更多网络相关信息
REM 例如，查看路由表
route print >> %OutputFile%

REM 可选：查看当前的ARP表
arp -a >> %OutputFile%

REM 完成提示
echo Information has been saved to %OutputFile%
pause
