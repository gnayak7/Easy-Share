#!/usr/bin/python

#system imports
import os
import sys

import twitter	

#PyQt imports
from PyQt4.QtCore import *
from PyQt4 import QtGui
from optparse import OptionParser

global_tweet= " "
global global_tweet

def klipper(args):
    # from simplycode import run
    import os, commands
    args = " ".join([commands.mkarg(str(arg)) for arg in args])
    # For KDE3 which uses dcop instead of dbus:
    s, o = commands.getstatusoutput("qdbus org.kde.klipper /klipper " + args)
    if s == 0:
        return o
    return ""

#code to access clip board contents
parser = OptionParser(__doc__, version="0.2.0")

parser.add_option("-i", "--item", type="int", default=0,
         help="get the Nth item in clipboard history", metavar="N")
parser.add_option("--strip", action="store_true", default=True,
         help="strip leading or trailing whitespace (default)")
parser.add_option("-n", "--no-strip", action="store_false", dest="strip",
         help="don't strip leading or trailing whitespace")
parser.add_option("-x", "--clear", action="store_true", default=False,
         help="clear the clipboard history")

(options, args) = parser.parse_args()

if options.clear:
     klipper(["clearClipboardHistory"])
elif len(args) == 0:
     content = klipper(["getClipboardHistoryItem", options.item])
     if options.strip:
          content = content.strip()
     print content
else:
        content = " ".join(args)
        if content == "-":
            import sys
            content = sys.stdin.read()
        if options.strip:
            content = content.strip()
           
            global_tweet=content
        klipper(["setClipboardContents", content])
  
def upload():
 tweet=global_tweet
 twitter.post_to_twitter(tweet)
 print "done!"

#upload action for tweet statement
app = QtGui.QApplication(sys.argv)
win=QtGui.QWidget()   
grid = QtGui.QGridLayout()
okButton = QtGui.QPushButton("ok")
cancelButton = QtGui.QPushButton("cancel")

usertoken = QtGui.QLabel("Enter token appearing on browser")
usertoken.setToolTip("enter username")

grid.addWidget(usertoken, 3, 2) 
grid.addWidget(okButton,8,5 )
grid.addWidget(cancelButton,8,6 )

usertokenLineEdit = QtGui.QLineEdit()
grid.addWidget(usertokenLineEdit,3,3 )
    
QObject.connect(okButton,SIGNAL("clicked()"),upload)
QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)
win.setLayout(grid) 
win.move(400, 300)
win.setWindowTitle('easyshare')    
win.show()	
sys.exit(app.exec_())
  
		

