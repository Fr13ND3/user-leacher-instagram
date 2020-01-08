# -Coded By : Zed-Team
# -Channel Telegram : @FR13ND3
# -Id programer in telegram : @Cra3ked
import os
try:
    from selenium import webdriver
except Exception:
    if os.name == "nt":
        os.system('pip install selenium --user')
        os.system('cls')
    else:
        os.system('pip install selenium')
        os.system('clear')
from time import sleep
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except Exception:
    if os.name == "nt":
        os.system('pip install Pyqt5 --user')
        os.system('cls')
    else:
        os.system('pip install Pyqt5')
        os.system('clear')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(656, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/x2ico.1.2.3.9/x2ico/Icons/2394490_0.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TX_RESULT = QtWidgets.QTextEdit(self.centralwidget)
        self.TX_RESULT.setGeometry(QtCore.QRect(330, 20, 301, 401))
        self.TX_RESULT.setObjectName("TX_RESULT")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 291, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(18, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(167, 29, 111, 28))
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 291, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.B_START = QtWidgets.QPushButton(self.groupBox_2)
        self.B_START.setGeometry(QtCore.QRect(15, 70, 121, 31))
        self.B_START.setObjectName("B_START")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 251, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.B_CLEAR = QtWidgets.QPushButton(self.groupBox_2)
        self.B_CLEAR.setGeometry(QtCore.QRect(150, 70, 121, 31))
        self.B_CLEAR.setObjectName("B_CLEAR")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 350, 291, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.L_RESULT = QtWidgets.QLabel(self.groupBox_3)
        self.L_RESULT.setGeometry(QtCore.QRect(80, 30, 191, 16))
        self.L_RESULT.setObjectName("L_RESULT")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 291, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.L_username = QtWidgets.QLineEdit(self.groupBox_4)
        self.L_username.setGeometry(QtCore.QRect(20, 28, 251, 22))
        self.L_username.setAlignment(QtCore.Qt.AlignCenter)
        self.L_username.setObjectName("L_username")
        self.L_password = QtWidgets.QLineEdit(self.groupBox_4)
        self.L_password.setGeometry(QtCore.QRect(20, 64, 251, 22))
        self.L_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.L_password.setAlignment(QtCore.Qt.AlignCenter)
        self.L_password.setObjectName("L_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.B_START.clicked.connect(self.btn_start)
        self.B_CLEAR.clicked.connect(self.btn_clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def btn_start(self):
        counnt = 0
        if self.comboBox.currentText() == "Comment":

            self.L_RESULT.setText('Start Leaching')
            self.TX_RESULT.clear()

            try:
                u = self.lineEdit.text()
                if u == "":
                    self.TX_RESULT.append("Please Enter username")
                    self.L_RESULT.setText('ERROR')
                    exit()
                driver = webdriver.Firefox()
                self.L_RESULT.setText('opening firefox')
                app.processEvents()
                try:
                    with open('user_leached.txt','x'):
                        pass
                except Exception:
                    pass
                
                self.TX_RESULT.append(f"The Target Username : {u}")
                self.L_RESULT.setText('Going to page target')
                driver.get(f'https://www.instagram.com/{u}')

                app.processEvents()
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                sleep(0.5)
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                sleep(0.5)
                driver.execute_script('window.scrollTo(0,0)')
                link_address_p = []
                self.L_RESULT.setText('Now get link posts')
                for i in range(0,5):
                    try:
                        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                        app.processEvents()
                        link_p = driver.find_elements_by_tag_name('a')
                        for elem in link_p:
                            if ".com/p/" in elem.get_attribute('href') :
                                link_address_p.append(elem.get_attribute('href'))
                                app.processEvents()
                    except Exception:
                        continue
                        app.processEvents()
                self.L_RESULT.setText('Getting more comment...')
                for iii in link_address_p:
                    driver.get(iii)
                    app.processEvents()
                    for i in range(1,20):
                        try:
                            more = driver.find_element_by_xpath('//html/body/div[1]/section/main/div/div/article/div[2]/div[1]/ul/li/div/button/span')
                            more.click()
                            sleep(2)
                            app.processEvents()
                        except Exception:
                            continue
                    all_user = driver.find_elements_by_tag_name('a')
                    al = []
                    alll = []
                    self.L_RESULT.setText('Please Wite ! now leaching users')
                    for e in range(0,10):
                        try:
                            for elem in all_user:
                                if "FPmhX notranslate  TlrDj" in elem.get_attribute('class') :
                                    if elem.get_attribute('href') not in alll:
                                        app.processEvents()
                                        al.append(elem.get_attribute('href'))
                                else:
                                    continue
                                    
                        except Exception:
                            continue
                    
                    for ii in al:
                        app.processEvents()
                        s = "".join(ii)
                        s = s.split('https://www.instagram.com/')
                        s = "".join(s)
                        s = s.replace('/','')

                        sleep(0.01)
                        app.processEvents()
                        if ii not in alll:
                            app.processEvents()
                            self.TX_RESULT.append(s)
                            with open('user_leached.txt','a') as af:
                                af.write(s)
                                af.write('\n')
                            alll.append(ii)                        
                            counnt +=1
                        self.L_RESULT.setText(f'Leach : {counnt}')
                self.L_RESULT.setText('Finished !')
            except Exception as e:
                print(e)
                app.processEvents()
        elif self.comboBox.currentText() == "Follower":
            self.TX_RESULT.clear()
            u_username = self.L_username.text()
            u_password = self.L_password.text()
            if u_username == "" or u_username == "your username" or u_password == "" or u_password == "your password":
                print('Error ! Please Enter username or password')
                exit()
            if len(u_password) < 6:
                print("len Password < 6")
                exit()
            
            app.processEvents()
            self.L_RESULT.setText('opening firefox')
            driver = webdriver.Firefox()
            app.processEvents()
            try:
                driver.get('https://www.instagram.com/accounts/login/')
                self.L_RESULT.setText('login in your account')
                sleep(4)
                app.processEvents()
                input_username = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(u_username)
                sleep(1)
                app.processEvents()
                input_password = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(u_password)
                sleep(1)
                app.processEvents()
                btn_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]")
                sleep(1)
                btn_login.click()
                sleep(4)
                
                try:
                    driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
                    self.TX_RESULT.append('login failed !')
                    exit()
                except Exception:
                    self.TX_RESULT.append("logined in your account")
                app.processEvents()
            except Exception as ee:
                self.TX_RESULT.append(ee)
                exit()
            app.processEvents()
            self.L_RESULT.setText('go page target')
            driver.get(f'https://www.instagram.com/{u_username}/')
            app.processEvents()
            u = self.lineEdit.text()
            if u == "":
                self.TX_RESULT.append("Please Enter username")
                exit()


            try:
                with open('user_leached.txt','x'):
                    pass
            except Exception:
                pass
                
            self.TX_RESULT.append(f"The Target Username : {u}")
            app.processEvents()
            driver.get(f'https://www.instagram.com/{u}')
            sleep(3)
            b_fw = driver.find_element_by_xpath('//a[@class="-nal3 "]')
            b_fw.click()
            app.processEvents()
            al = [u]
            alll = []
            sleep(2)
            app.processEvents()
            self.L_RESULT.setText('leaching username!')
            counnt = 0
            while True:
                app.exec_()
                al.clear()
                eula = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
                app.processEvents()
                sleep(1)
                driver.execute_script('arguments[0].scrollTo(0,600)', eula)
                app.processEvents()
                sleep(2)
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', eula)
                app.processEvents()
                try:
                    all_user = driver.find_elements_by_tag_name('a')
                    app.processEvents()
                    for elem in all_user:
                        if "FPmhX notranslate  _0imsa " in elem.get_attribute('class') :
                            if elem.get_attribute('href') not in alll:
                                app.processEvents()
                                al.append(elem.get_attribute('href'))
                            else:
                                continue
                    app.processEvents()
                    # print(al)
                    for ii in al:
                        s = "".join(ii)
                        s = s.split('https://www.instagram.com/')
                        s = "".join(s)
                        s = s.replace('/','')
                        app.processEvents()
                            
                        if ii not in alll:
                            app.processEvents()
                            sleep(0.01)                            
                            self.TX_RESULT.append(s)
                            alll.append(ii)
                            counnt +=1
                            with open('user_leached.txt','a') as af:
                                af.write(s)
                                app.processEvents()
                                af.write('\n')
                            sleep(0.01)
                        self.L_RESULT.setText(f'Leached : {counnt}')

                        
                    
                    
                        
                except Exception as ee:
                    continue
                    app.processEvents()
                    self.TX_RESULT.append(ee)
                    
        elif self.comboBox.currentText() == "Following":
            self.TX_RESULT.clear()
            u_username = self.L_username.text()
            u_password = self.L_password.text()
            if u_username == "" or u_username == "your username" or u_password == "" or u_password == "your password":
                print('Error ! Please Enter username or password')
                exit()
            if len(u_password) < 6:
                print("len Password < 6")
                exit()
            
            app.processEvents()
            self.L_RESULT.setText('opening firefox')
            driver = webdriver.Firefox()
            app.processEvents()
            try:
                driver.get('https://www.instagram.com/accounts/login/')
                self.L_RESULT.setText('login in your account')
                sleep(4)
                app.processEvents()
                input_username = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(u_username)
                sleep(1)
                app.processEvents()
                input_password = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(u_password)
                sleep(1)
                app.processEvents()
                btn_login = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]")
                sleep(1)
                btn_login.click()
                sleep(4)
                app.processEvents()
            except Exception as ee:
                self.TX_RESULT.append(ee)
                exit()
            app.processEvents()
            self.L_RESULT.setText('go page target')
            driver.get(f'https://www.instagram.com/{u_username}/')
            app.processEvents()
            u = self.lineEdit.text()
            if u == "":
                self.TX_RESULT.append("Please Enter username")
                exit()


            try:
                with open('user_leached.txt','x'):
                    pass
            except Exception:
                pass
                
            self.TX_RESULT.append(f"The Target Username : {u}")
            app.processEvents()
            driver.get(f'https://www.instagram.com/{u}')
            sleep(3)
            b_fw = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
            b_fw.click()
            app.processEvents()
            al = [u]
            alll = []
            sleep(2)
            app.processEvents()
            self.L_RESULT.setText('leaching username!')
            counnt = 0
            while True:
                app.exec_()
                al.clear()
                eula = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
                app.processEvents()
                sleep(1)
                driver.execute_script('arguments[0].scrollTo(0,600)', eula)
                app.processEvents()
                sleep(2)
                driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', eula)
                app.processEvents()
                try:
                    all_user = driver.find_elements_by_tag_name('a')
                    app.processEvents()
                    for elem in all_user:
                        if "FPmhX notranslate  _0imsa " in elem.get_attribute('class') :
                            if elem.get_attribute('href') not in alll:
                                app.processEvents()
                                al.append(elem.get_attribute('href'))
                            else:
                                continue
                    app.processEvents()
                    for ii in al:
                        s = "".join(ii)
                        s = s.split('https://www.instagram.com/')
                        s = "".join(s)
                        s = s.replace('/','')
                        app.processEvents()
                            
                        if ii not in alll:
                            app.processEvents()
                            self.TX_RESULT.append(s)
                            alll.append(ii)
                            counnt +=1
                            with open('user_leached.txt','a') as af:
                                af.write(s)
                                app.processEvents()
                                af.write('\n')
                            sleep(0.01)
                        self.L_RESULT.setText(f'Leached : {counnt}')
                except Exception as ee:
                    continue
                    app.processEvents()
                    self.TX_RESULT.append(ee)  
    def btn_clear(self):
        self.TX_RESULT.clear()
        self.L_RESULT.setText('Clear all result')
    def btn_telegram(self):
        pass
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instgram User Leacher Coded By Zed-Team | Telegram : @FR13ND3"))
        self.TX_RESULT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                     ***** Result *****</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Type Leach"))
        self.label.setText(_translate("MainWindow", "Please choese type : "))
        self.comboBox.setCurrentText(_translate("MainWindow", "Comment"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Comment"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Follower"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Following"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Option"))
        self.B_START.setText(_translate("MainWindow", "Start Leach"))
        self.lineEdit.setText(_translate("MainWindow", "Target username"))
        self.B_CLEAR.setText(_translate("MainWindow", "Clear Result"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Status"))
        self.label_2.setText(_translate("MainWindow", "Status :"))
        self.L_RESULT.setText(_translate("MainWindow", "..."))
        self.groupBox_4.setTitle(_translate("MainWindow", "Login in instagram"))
        self.L_username.setText(_translate("MainWindow", "your username"))
        self.L_password.setText(_translate("MainWindow", "your password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
