import os
import sys
import time
import csv
import save_img

print(sys.argv)
os.system("casperjs youtube_login.js '%s' '%s'" % (sys.argv[1], sys.argv[2]))
# timeElapsed = time.time() - now
# print "Time Elapsed: " + str(timeElapsed)
print("saving images")
save_img.saveFromFile(sys.argv[1])
prin("parsing images")
os.system("python parse_images.py %s %s" % (sys.argv[1]))

