import os
import sys
import time
import csv


print(sys.argv)
os.system("casperjs youtube_login.js '%s' '%s'" % (sys.argv[1], sys.argv[2]))
# timeElapsed = time.time() - now
# print "Time Elapsed: " + str(timeElapsed)


