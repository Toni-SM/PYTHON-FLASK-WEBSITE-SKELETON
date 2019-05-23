#/bin/bash
while true
do
	clear
	python3 run.py
	echo ------------------------------------------------------------
	echo [BATCH] Server Shutdown, waiting 5 seconds before a restart
	sleep 5
done
