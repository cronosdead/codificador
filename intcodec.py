# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intcodec.ui'
#
# Created: dom mar 2 23:57:54 2014
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!

import sys
from qt import *
import Str2Bin as s2b
import binascii
import numpy as np


class Form1(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form1")

        pal = QPalette()
        cg = QColorGroup()
        cg.setColor(QColorGroup.Foreground,Qt.white)
        cg.setColor(QColorGroup.Button,QColor(0,255,0))
        cg.setColor(QColorGroup.Light,QColor(127,255,127))
        cg.setColor(QColorGroup.Midlight,QColor(63,255,63))
        cg.setColor(QColorGroup.Dark,QColor(0,127,0))
        cg.setColor(QColorGroup.Mid,QColor(0,170,0))
        cg.setColor(QColorGroup.Text,Qt.white)
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,Qt.white)
        cg.setColor(QColorGroup.Base,Qt.black)
        cg.setColor(QColorGroup.Background,Qt.black)
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,Qt.black)
        cg.setColor(QColorGroup.LinkVisited,Qt.black)
        pal.setActive(cg)
        cg.setColor(QColorGroup.Foreground,Qt.white)
        cg.setColor(QColorGroup.Button,QColor(0,255,0))
        cg.setColor(QColorGroup.Light,QColor(127,255,127))
        cg.setColor(QColorGroup.Midlight,QColor(38,255,38))
        cg.setColor(QColorGroup.Dark,QColor(0,127,0))
        cg.setColor(QColorGroup.Mid,QColor(0,170,0))
        cg.setColor(QColorGroup.Text,Qt.white)
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,Qt.white)
        cg.setColor(QColorGroup.Base,Qt.black)
        cg.setColor(QColorGroup.Background,Qt.black)
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,QColor(0,0,255))
        cg.setColor(QColorGroup.LinkVisited,QColor(255,0,255))
        pal.setInactive(cg)
        cg.setColor(QColorGroup.Foreground,QColor(128,128,128))
        cg.setColor(QColorGroup.Button,QColor(0,255,0))
        cg.setColor(QColorGroup.Light,QColor(127,255,127))
        cg.setColor(QColorGroup.Midlight,QColor(38,255,38))
        cg.setColor(QColorGroup.Dark,QColor(0,127,0))
        cg.setColor(QColorGroup.Mid,QColor(0,170,0))
        cg.setColor(QColorGroup.Text,QColor(128,128,128))
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,QColor(128,128,128))
        cg.setColor(QColorGroup.Base,Qt.black)
        cg.setColor(QColorGroup.Background,Qt.black)
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,QColor(0,0,255))
        cg.setColor(QColorGroup.LinkVisited,QColor(255,0,255))
        pal.setDisabled(cg)
        self.setPalette(pal)
        f = QFont(self.font())
        self.setFont(f)


        self.textEdit1 = QTextEdit(self,"textEdit1")
        self.textEdit1.setGeometry(QRect(20,20,360,240))
        self.textEdit1.setHScrollBarMode(QTextEdit.AlwaysOn)

        self.pushButton1 = QPushButton(self,"pushButton1")
        self.pushButton1.setGeometry(QRect(390,100,81,31))

        self.textEdit1_3 = QTextEdit(self,"textEdit1_3")
        self.textEdit1_3.setGeometry(QRect(250,320,360,240))
        self.textEdit1_3.setHScrollBarMode(QTextEdit.AlwaysOn)

        self.pushButton2 = QPushButton(self,"pushButton2")
        self.pushButton2.setGeometry(QRect(80,400,111,31))

        self.textEdit1_2 = QTextEdit(self,"textEdit1_2")
        self.textEdit1_2.setGeometry(QRect(480,20,360,240))
        self.textEdit1_2.setHScrollBarMode(QTextEdit.AlwaysOn)

        self.languageChange()

        self.resize(QSize(857,612).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton1,SIGNAL("clicked()"),self.code)
        self.connect(self.pushButton2,SIGNAL("clicked()"),self.decode)


    def languageChange(self):
        self.setCaption(self.__tr("COD/DECOD"))
        self.pushButton1.setText(self.__tr("Code"))
        self.pushButton2.setText(self.__tr("Decode"))


    def code(self):
        e = self.textEdit1.text().ascii()
        e = s2b.Str2Bin(e)
        n = np.array(e)
        print n, len(n)
        ar = []
        #ns = np.transpose(n)
        
        for i in range(len(n)):
			vec = np.array([])
			aux = [0]
			v = len(n[i])
			if v < 8:
				for j in range(8 - v):
					vec = np.append(n[i], aux)
					aux.append(0)
				ar.append(vec)
			else:
				ar.append(vec)
        
        mat = np.array(ar)
        mat = np.transpose(mat)				
       	self.textEdit1_2.setText(str(mat))

    def decode(self):
        print "Form1.decode(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Form1()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()

