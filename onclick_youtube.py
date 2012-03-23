#!/usr/bin/python

#system imports
import os
import sys

#my imports
import youtube	
import addyoutube	

#PyQt import
from PyQt4.QtCore import *
from PyQt4 import QtGui

 #--------globals! ------------
global_uname = " "
global_passwd = " "
global_videoTitle = " "
 #-------------------------------------

#defining the uplod function
def uploadfirst():
 print "uploading!..."  
 
 global global_uname
 global global_videoTitle
 global global_passwd
 
 global_uname = str(unameLineEdit.text())
 global_passwd=str(passwdLineEdit.text())
 global_videoTitle=str(videoTitleLineEdit.text())

 fouttest = open("login.log","w")
 fouttest.write("hello1")
       
 s1="notfirsttime"
 f1=open("/home/gowtham/countyoutube.txt","w")

 string1=global_uname
 string2=global_passwd
 string3=global_videoTitle
 string4=sys.argv[1]

 f1.write(s1)
 f1.close()
		
 fouttest.write("hello4")
 fout=open("log.txt","w")
 fout.write(string4)
 fout.close()
 fouttest.write("hello*")
 print "calling upload! in if"
 
 addyoutube.details(string1,string2)
 print string4
 print string3
 print string1
 print string2
 youtube.post_to_youtube(string4,string3,string1,string2)
 print "done!"

 fouttest.write("hello5")
#.............................................................................
def uploadsecond():
	global global_videoTitle
	global_videoTitle = str(videoTitleLineEdit.text())
	f3=open("detailsyoutube.txt","r")
	username=f3.readline()
	passwrd=f3.readline()
	title=global_videoTitle
	filepath=sys.argv[1]

	#global global_uname
	username= username.strip()
	passwrd= passwrd.strip()
	#global global_passwd
	
	#global global_albumTitle
	print (filepath)
	print (title)
	print (username)
	print (passwrd)
	
	youtube.post_to_youtube(filepath,title,username,passwrd)
        print "done!"
#-------------------------
#The logic starts here
fout=open("/home/gowtham/countyoutube.txt","r")
s1=fout.readline()
s2="firsttime"
if s1==s2:
  app = QtGui.QApplication(sys.argv)

  win=QtGui.QWidget()   

  grid = QtGui.QGridLayout()
	
  okButton = QtGui.QPushButton("ok")
  cancelButton = QtGui.QPushButton("cancel")

  unameLabel = QtGui.QLabel("username")
  passwdLabel = QtGui.QLabel("password")
  videoTitleLabel = QtGui.QLabel("title")

  unameLabel.setToolTip("enter username")
  passwdLabel.setToolTip("enter password")
  videoTitleLabel.setToolTip("enter title")

  grid.addWidget(unameLabel, 3, 2)
  grid.addWidget(passwdLabel,4, 2)
  grid.addWidget(videoTitleLabel,5, 2)
      
  grid.addWidget(okButton,8,5 )
  grid.addWidget(cancelButton,8,6 )

  unameLineEdit = QtGui.QLineEdit()
  grid.addWidget(unameLineEdit,3,3 )
      
  passwdLineEdit = QtGui.QLineEdit()
  passwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
  grid.addWidget(passwdLineEdit,4,3 )
    
  videoTitleLineEdit = QtGui.QLineEdit()
  grid.addWidget(videoTitleLineEdit,5,3)

  win.setLayout(grid) 
  
  QObject.connect(okButton,SIGNAL("clicked()"),uploadfirst)
  QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)

  win.move(400, 300)
  win.setWindowTitle('easyshare')    
  win.show()	
  sys.exit(app.exec_())
else:
  app = QtGui.QApplication(sys.argv)

  win=QtGui.QWidget()   

  grid = QtGui.QGridLayout()
	
  okButton = QtGui.QPushButton("ok")
  cancelButton = QtGui.QPushButton("cancel")

  videoTitleLabel = QtGui.QLabel("title")

  grid.addWidget(videoTitleLabel,5, 2)
      
  grid.addWidget(okButton,8,5 )
  grid.addWidget(cancelButton,8,6 )
      
  videoTitleLineEdit = QtGui.QLineEdit()
  grid.addWidget(videoTitleLineEdit,5,3)

  win.setLayout(grid) 
  
  QObject.connect(okButton,SIGNAL("clicked()"),uploadsecond)
  QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)

  win.move(400, 300)
  win.setWindowTitle('easyshare')    
  win.show()	
  sys.exit(app.exec_())
 