@echo off
REM ����ļ���·�����ļ���
SET OutputFile=info.txt
echo ===========������Ϣ=========== > %OutputFile%
REM ������Ϣ
systeminfo >> %OutputFile%

echo ===========������Ϣ=========== >> %OutputFile%
REM �����򸲸��ļ���д��IP������Ϣ
ipconfig /all >> %OutputFile%

REM ��ѡ�����ļ�׷�Ӹ������������Ϣ
REM ���磬�鿴·�ɱ�
route print >> %OutputFile%

REM ��ѡ���鿴��ǰ��ARP��
arp -a >> %OutputFile%

REM �����ʾ
echo Information has been saved to %OutputFile%
pause
