@echo off
echo [BATCH] Starting Server
:loop
   cls
   python run.py
   echo -------------------------------------------------------
   echo [BATCH] Server Shutdown, waiting 10 seconds before a restart.
   timeout /t 10 > nul
   goto loop