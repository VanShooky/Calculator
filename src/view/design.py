# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from view.custom_label import CustomLabel
import view.files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(325, 470)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #5B7065;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #4D585B;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #B4B4B4;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(12, 12))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignRight)

        
        self.lbl_temp = CustomLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy1)
        self.lbl_temp.setStyleSheet(u"color: #B4B4B4;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy2)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_C_8 = QPushButton(self.centralwidget)
        self.pushButton_C_8.setObjectName(u"pushButton_C_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_C_8.sizePolicy().hasHeightForWidth())
        self.pushButton_C_8.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.pushButton_C_8, 0, 0, 1, 1)

        self.pushButton_C_12 = QPushButton(self.centralwidget)
        self.pushButton_C_12.setObjectName(u"pushButton_C_12")
        sizePolicy3.setHeightForWidth(self.pushButton_C_12.sizePolicy().hasHeightForWidth())
        self.pushButton_C_12.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.pushButton_C_12, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_8)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(12, 12))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_div = QPushButton(self.tab)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_3 = QPushButton(self.tab)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy4.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_7 = QPushButton(self.tab)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy4.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_neg = QPushButton(self.tab)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy4.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_add = QPushButton(self.tab)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy4.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_9 = QPushButton(self.tab)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy4.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_sub = QPushButton(self.tab)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy4.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_8 = QPushButton(self.tab)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy4.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_5 = QPushButton(self.tab)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy4.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_backspace = QPushButton(self.tab)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy4.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_ce = QPushButton(self.tab)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy4.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_4 = QPushButton(self.tab)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy4.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.tab)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy4.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_calc = QPushButton(self.tab)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy4.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_calc, 4, 3, 1, 1)

        self.btn_1 = QPushButton(self.tab)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy4.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_0 = QPushButton(self.tab)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy4.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_mul = QPushButton(self.tab)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy4.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_point = QPushButton(self.tab)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy4.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_6 = QPushButton(self.tab)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy4.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_clear = QPushButton(self.tab)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy4.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_log = QPushButton(self.tab_2)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_log, 2, 0, 1, 1)

        self.btn_in2 = QPushButton(self.tab_2)
        self.btn_in2.setObjectName(u"btn_in2")
        sizePolicy5.setHeightForWidth(self.btn_in2.sizePolicy().hasHeightForWidth())
        self.btn_in2.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_in2, 0, 0, 1, 1)

        self.btn_otkl = QPushButton(self.tab_2)
        self.btn_otkl.setObjectName(u"btn_otkl")
        sizePolicy5.setHeightForWidth(self.btn_otkl.sizePolicy().hasHeightForWidth())
        self.btn_otkl.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_otkl, 3, 1, 1, 1)

        self.btn_fact = QPushButton(self.tab_2)
        self.btn_fact.setObjectName(u"btn_fact")
        sizePolicy5.setHeightForWidth(self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_fact, 2, 1, 1, 1)

        self.btn_in_n = QPushButton(self.tab_2)
        self.btn_in_n.setObjectName(u"btn_in_n")
        sizePolicy5.setHeightForWidth(self.btn_in_n.sizePolicy().hasHeightForWidth())
        self.btn_in_n.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_in_n, 1, 0, 1, 1)

        self.btn_mediana = QPushButton(self.tab_2)
        self.btn_mediana.setObjectName(u"btn_mediana")
        sizePolicy5.setHeightForWidth(self.btn_mediana.sizePolicy().hasHeightForWidth())
        self.btn_mediana.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_mediana, 3, 0, 1, 1)

        self.btn_sqrt_n = QPushButton(self.tab_2)
        self.btn_sqrt_n.setObjectName(u"btn_sqrt_n")
        sizePolicy5.setHeightForWidth(self.btn_sqrt_n.sizePolicy().hasHeightForWidth())
        self.btn_sqrt_n.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_sqrt_n, 1, 1, 1, 1)

        self.btn_sqrt2 = QPushButton(self.tab_2)
        self.btn_sqrt2.setObjectName(u"btn_sqrt2")
        sizePolicy5.setHeightForWidth(self.btn_sqrt2.sizePolicy().hasHeightForWidth())
        self.btn_sqrt2.setSizePolicy(sizePolicy5)

        self.gridLayout_2.addWidget(self.btn_sqrt2, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_C_5 = QPushButton(self.centralwidget)
        self.pushButton_C_5.setObjectName(u"pushButton_C_5")
        sizePolicy3.setHeightForWidth(self.pushButton_C_5.sizePolicy().hasHeightForWidth())
        self.pushButton_C_5.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_C_5, 0, 0, 1, 1)

        self.pushButton_C_6 = QPushButton(self.centralwidget)
        self.pushButton_C_6.setObjectName(u"pushButton_C_6")
        sizePolicy3.setHeightForWidth(self.pushButton_C_6.sizePolicy().hasHeightForWidth())
        self.pushButton_C_6.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.pushButton_C_6, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0438\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_C_8.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_C_12.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.btn_neg.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"<-", None))
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "")
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.btn_in2.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0432\u0430\u0434\u0440\u0430\u0442", None))
        self.btn_otkl.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435", None))
        self.btn_fact.setText(QCoreApplication.translate("MainWindow", u"\u0444\u0430\u043a\u0442\u043e\u0440\u0438\u0430\u043b", None))
        self.btn_in_n.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0435\u043f\u0435\u043d\u044c", None))
        self.btn_mediana.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0435\u0434\u0438\u0430\u043d\u0430", None))
        self.btn_sqrt_n.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u0440\u0435\u043d\u044c\u2800\u0441\u0442\u0435\u043f\u0435\u043d\u0438", None))
        self.btn_sqrt2.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u0440\u0435\u043d\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "")
        self.pushButton_C_5.setText(QCoreApplication.translate("MainWindow", u"\u0438\u043c\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton_C_6.setText(QCoreApplication.translate("MainWindow", u"\u044d\u043a\u0441\u043f\u043e\u0440\u0442 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430", None))
    # retranslateUi

