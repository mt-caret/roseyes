#!/usr/bin/env python

import os
import sys
import subprocess

import rospy
from roseyes.msg import Look

def main():
    rospy.init_node("roseyes")
    os.environ["DISPLAY"] = ":0"
    process = subprocess.Popen([sys.argv[1]], stdin=subprocess.PIPE)
    subprocess.check_call('xdotool windowsize `xdotool search --name xeyes` 100% 100%', shell=True)

    def look_callback(look):
        process.write("{} {}\n".format(look.x, look.y))

    def shutdown_callback():
        process.terminate()

    rospy.on_shutdown(shutdown_callback)
    rospy.Subscriber("/look", Look, look_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
