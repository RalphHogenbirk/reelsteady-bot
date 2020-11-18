#!/usr/bin/python
import sys
import signal
from main import ReelSteadyGoRunner

# quick n dirty debug arg
debug = False
if len(sys.argv)> 1:
    if sys.argv[1] == 'debug':
        debug = 1

# create a runner
runner = ReelSteadyGoRunner(debug)

# exit stragegy
def signal_handler(sig, frame):
    print('Exiting! Leaving all instances running as they are')
    # runner.stop() # doesn't work for some reason. threading issue?
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# start program
runner.start()
