REM Batch file to build PyQt-win-nc-3.5, -3.6 or 3.7.
REM Put this file in PyQt-win-nc-3.5, -3.6 or 3.7 and run it.
REM You may have to adapt it for your Python installation.

python build.py
nmake

REM Doing 'nmake' has put all library files in C:\python22\Lib\site-packages
REM Doing 'nmake install' may delete some necessary library files.
REM Copying the *.py files leaves the *.{exp,lib,pyd} files in place.
copy /y qt\qt.py C:\python22\lib\site-packages
copy /y qtcanvas\qtcanvas.py C:\python22\Lib\site-packages
copy /y qtgl\qtgl.py C:\python22\Lib\site-packages
copy /y qtnetwork\qtnetwork.py C:\python22\Lib\site-packages
copy /y qttable\qttable.py C:\python22\Lib\site-packages
copy /y qtxml\qtxml.py C:\Python22\Lib\site-packages
REM Add more copy commands, if appropriate
