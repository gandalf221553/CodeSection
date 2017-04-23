# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:30:29 2017

@author: Von Braun
"""

#import os
#a=os.getcwd()
#os.chdir("kivy-examples\\canvas")
import PyInstaller.__main__
print(dir())
#PyInstaller.__main__.run(["-y", "-w","circle.py"])
#os.chdir(a)
#import PyInstaller.__main__
PyInstaller.__main__.run(["-y", "-w","kivy_matplotlib.py"])


"""
api-ms-win-core-errorhandling-l1-1-0.dll
api-ms-win-core-file-l2-1-0.dll
api-ms-win-core-processthreads-l1-1-1.dll
api-ms-win-core-synch-l1-1-0.dll
api-ms-win-core-localization-l1-2-0.dll
api-ms-win-core-datetime-l1-1-0.dll
api-ms-win-core-handle-l1-1-0.dll
api-ms-win-core-interlocked-l1-1-0.dll
api-ms-win-core-memory-l1-1-0.dll
api-ms-win-core-processenvironment-l1-1-0.dll
api-ms-win-core-namedpipe-l1-1-0.dll
api-ms-win-core-processthreads-l1-1-0.dll
api-ms-win-core-synch-l1-2-0.dll
api-ms-win-core-profile-l1-1-0.dll
api-ms-win-core-libraryloader-l1-1-0.dll
api-ms-win-core-string-l1-1-0.dll
api-ms-win-core-console-l1-1-0.dll
api-ms-win-core-sysinfo-l1-1-0.dll
api-ms-win-core-file-l1-2-0.dll
api-ms-win-core-heap-l1-1-0.dll
api-ms-win-core-debug-l1-1-0.dll
api-ms-win-core-file-l1-1-0.dll
api-ms-win-core-timezone-l1-1-0.dll
api-ms-win-core-rtlsupport-l1-1-0.dll
api-ms-win-core-util-l1-1-0.dll
"""