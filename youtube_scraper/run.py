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
save_img.saveFromFile()
print("parsing images")
os.system("python parse_images.py %s" % (sys.argv[1]))
print("arranging files...")
os.system("mv %s downloaded" % (sys.argv[1]))
os.system("mv %s_parsed parsed" % (sys.argv[1]))
os.system("mkdir %s" % (sys.argv[1]))
os.system("mv downloaded %s" % (sys.argv[1]))
os.system("mv parsed %s" % (sys.argv[1]))

