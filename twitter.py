import webbrowser
import tweepy
from compiler.ast import Raise
import os
import sys
#import twitter
from PyQt4.QtCore import *
from PyQt4 import QtGui
from optparse import OptionParser

global_tweet= " "
global_token=" "
pin=" "
usertokenLineEdit=" "
auth=" "
tweet= " "

#import globals
twitter_consumer_key = 'l6M7pMaqmJew5r1lAf3jyw'
twitter_consumer_secret = '8aMrvDlbpmWN1evk9JPBsGQ3Mcg4urR0Cfat97BA4'

"""
    Query the user for their consumer key/secret
    then attempt to fetch a valid access token.
"""
def klipper(args):
    import os, commands
    args = " ".join([commands.mkarg(str(arg)) for arg in args])
    s, o = commands.getstatusoutput("qdbus org.kde.klipper /klipper " + args)
    if s == 0:
        return o
    return ""
 
#..................................PROGRAM BEGINS HERE......................................
#code to select clipboard content
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
          global_tweet=content
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
  global global_token
  global auth
  global tweet
  print("in upload")
  global_token=str(usertokenLineEdit.text())
  print global_token
  global pin
  pin=global_token
  print pin
  try :
            token = auth.get_access_token(verifier=pin)
            print("pin is obtained")
  except :
            raise NameError('Authorization error')
            return 0
    
  twitter_oauth_key = token.key
  twitter_oauth_secret = token.secret
        
  try :
         auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
         auth.set_access_token(twitter_oauth_key, twitter_oauth_secret)
         print("access token is set")
  except : 
         raise NameError('Could not authorize user')
         return 0
  twit_user = tweepy.API()
    
  try :
         api = tweepy.API(auth)
         print 'uploading now............!!!'
         api.update_status(tweet+"tweet from easy share application :)")
         print("done..!")
  except :
         raise NameError('Error in connecting to the network')
         return 0

  return 1



def post_to_twitter(link):
	global usertokenLineEdit
        global auth
        global tweet
        tweet = link
	auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
    	# Open authorization URL in browser
    	#-----------------------
    	#temp_credentials = auth.getRequestToken()
    	#webbrowser.open(auth.get_authorization_url(temp_credentials))
    	#--------------------------
        webbrowser.open(auth.get_authorization_url())
          
        # Ask user for verifier pin using UI
        app = QtGui.QApplication(sys.argv)

        win=QtGui.QWidget()   

        grid = QtGui.QGridLayout()
       
        okButton = QtGui.QPushButton("ok")
        cancelButton = QtGui.QPushButton("cancel")

        usertoken = QtGui.QLabel("Enter token appearing on browser")

        grid.addWidget(usertoken, 3, 2)

        grid.addWidget(okButton,8,5 )
        grid.addWidget(cancelButton,8,6 )

        usertokenLineEdit = QtGui.QLineEdit()

        global_token = usertokenLineEdit
        grid.addWidget(usertokenLineEdit,3,3 )

        QObject.connect(okButton,SIGNAL("clicked()"),upload)
        QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)
        win.setLayout(grid) 
        win.move(400, 300)
        win.setWindowTitle('easyshare')    
        win.show()	
        sys.exit(app.exec_())
#................................................UPLOAD USING CLIPBOARD CONTENT................................

print global_tweet
post_to_twitter(global_tweet)