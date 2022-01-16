import subprocess
import time

subprocess.call('start python server.py', shell=True)
time.sleep(2)
subprocess.call('start python client.py', shell=True)
