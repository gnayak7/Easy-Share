app = QtGui.QApplication(sys.argv)

win=QtGui.QWidget()   

grid = QtGui.QGridLayout()
       
okButton = QtGui.QPushButton("ok")
cancelButton = QtGui.QPushButton("cancel")

    
unameLabel = QtGui.QLabel("username")
passwdLabel = QtGui.QLabel("password")
albumTitleLabel = QtGui.QLabel("title")

unameLabel.setToolTip("enter username")
passwdLabel.setToolTip("enter password")
albumTitleLabel.setToolTip("enter title")

grid.addWidget(unameLabel, 3, 2)
grid.addWidget(passwdLabel,4, 2)
grid.addWidget(albumTitleLabel,5, 2)
    
grid.addWidget(okButton,8,5 )
grid.addWidget(cancelButton,8,6 )

unameLineEdit = QtGui.QLineEdit()
global_uname = unameLineEdit
grid.addWidget(unameLineEdit,3,3 )
    
passwdLineEdit = QtGui.QLineEdit()
global_passwd = passwdLineEdit
passwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
grid.addWidget(passwdLineEdit,4,3 )

    
albumTitleLineEdit = QtGui.QLineEdit()
global_albumTitle = albumTitleLineEdit
grid.addWidget(albumTitleLineEdit,5,3)

win.setLayout(grid) 
 
QObject.connect(okButton,SIGNAL("clicked()"),upload)
QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)

win.move(400, 300)
win.setWindowTitle('easyshare')    
win.show()	
sys.exit(app.exec_())