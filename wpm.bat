set workdir=%~dp0
cd %workdir%
where python > tmp
set /p PYPATH= < tmp
del tmp
%PYPATH% wpm.py > wpm.log 2>&1