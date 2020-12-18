@echo off 

Set count=0
python to.py
:a 
if %count% gtr 1000 (goto :a) else (set /a count+=1)
set /P name="--------------->"
python to.py %name%

goto :a 
