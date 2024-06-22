@echo off
set "smp=%appdata%\microsoft\windows\start menu\programs"
cd %~dp0
echo If you want to proceed with installation, press any key. If you close this window, the installation won't begin. Installation path: "%userprofile%\Notepy"
pause > nul
echo Installing...
mkdir "%userprofile%\Notepy"
copy notepy_en "%userprofile%\Notepy"
copy notepy_pl "%userprofile%\Notepy"
copy notepy_en\src "%userprofile%\Notepy"
copy notepy_pl\src "%userprofile%\Notepy"
echo Error code (0 means everything is okay, if it isn't, use "certutil /error %errorlevel%"): %errorlevel%
echo Press any key to exit...
pause > nul