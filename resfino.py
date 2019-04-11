# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'harsh.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(856, 510)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 50, 111, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


###########################################################################################
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton.clicked.connect(self.download)
#########################################################################################


#########################################################################
        self.item_id = QtGui.QLineEdit(Dialog)
        self.item_id.setGeometry(QtCore.QRect(50, 50, 271, 31))
        self.item_id.setObjectName(_fromUtf8("item_id"))
        self.quantity = QtGui.QLineEdit(Dialog)
        self.quantity.setGeometry(QtCore.QRect(350, 50, 271, 31))
        self.quantity.setObjectName(_fromUtf8("quantity"))
    #######################################################################
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 170, 121, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 170, 113, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 170, 113, 31))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(510, 170, 113, 31))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(670, 170, 113, 31))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 290, 113, 31))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 290, 113, 31))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 290, 113, 31))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(510, 290, 113, 31))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(670, 290, 113, 31))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(50, 400, 771, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 150, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 150, 47, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 150, 47, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(540, 150, 47, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(700, 150, 47, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 270, 47, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(240, 270, 47, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(370, 270, 47, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(530, 270, 47, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(710, 270, 47, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(140, 30, 121, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(440, 30, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
#########################################################################################
    def buttonClicked(self):

        id = self.item_id.text()


        quant = self.quantity.text()
        f1 = open("C:\\Users\\HARSH\\Documents\\Sales Forecast\\csv\\ratio\\new\\6.csv", "r")
        f1.readline()
        nid = "'"+id+"'"
        for i in range(0,1543):
            k = f1.readline().split(",")
            if(k[0]==nid):
                self.lineEdit.setText(str(int((float(k[1])*float(quant)))))
                self.lineEdit_2.setText(str(int((float(k[2])*float(quant)))))
                self.lineEdit_3.setText(str(int((float(k[3])*float(quant)))))
                self.lineEdit_4.setText(str(int((float(k[4])*float(quant)))))
                self.lineEdit_5.setText(str(int((float(k[5])*float(quant)))))
                self.lineEdit_6.setText(str(int((float(k[6])*float(quant)))))
                self.lineEdit_7.setText(str(int((float(k[7])*float(quant)))))
                self.lineEdit_8.setText(str(int((float(k[8])*float(quant)))))
                self.lineEdit_9.setText(str(int((float(k[9])*float(quant)))))
                self.lineEdit_10.setText(str(int((float(k[10])*float(quant)))))



############################################################################################
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001

            self.progressBar.setValue(self.completed)


#############################################################################################











    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "RESFINO", None))
        self.pushButton.setText(_translate("Dialog", "ALLOCATE", None))
        self.label.setText(_translate("Dialog", "OUT010", None))
        self.label_2.setText(_translate("Dialog", "OUT013", None))
        self.label_3.setText(_translate("Dialog", "OUT017", None))
        self.label_4.setText(_translate("Dialog", "OUT018", None))
        self.label_5.setText(_translate("Dialog", "OUT019", None))
        self.label_6.setText(_translate("Dialog", "OUT027", None))
        self.label_7.setText(_translate("Dialog", "OUT035", None))
        self.label_8.setText(_translate("Dialog", "OUT045", None))
        self.label_9.setText(_translate("Dialog", "OUT046", None))
        self.label_10.setText(_translate("Dialog", "OUT049", None))
        self.label_11.setText(_translate("Dialog", "INPUT THE ITEM ID", None))
        self.label_12.setText(_translate("Dialog", "QUANTITY", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

