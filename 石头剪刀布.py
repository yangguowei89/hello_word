import sys,random      #导入标准库sys
from PyQt5.QtWidgets import QApplication, QWidget,QToolTip,QLabel,QLineEdit,QPushButton,QCheckBox
from PyQt5.QtGui import QIcon , QFont,QPixmap
class Example(QWidget):
    '''
    QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.cb=QCheckBox("是否新手",self)
        self.cb.move(280,10)
        self.setGeometry(800,100,400,150)
        self.setWindowTitle("猜拳游戏"+sys.argv[0])
        self.setWindowIcon(QIcon("剪子.png"))
        shitou=QPushButton("石头",self)
        shitou.setIcon(QIcon("shitou.ico"))
        shitou.move(30,50)
        shitou.clicked.connect(self.buttonClicked)
        jiandao=QPushButton("剪刀",self)
        jiandao.setIcon(QIcon("jiandao.ico"))
        jiandao.move(160, 50)
        jiandao.clicked.connect(self.buttonClicked)
        bu = QPushButton("布", self)
        bu.setIcon(QIcon("bu.ico"))
        bu.move(290, 50)
        bu.clicked.connect(self.buttonClicked)
        self.jieguo=QLabel(self)
        self.jieguo.setText("请点击按钮出拳")
        self.jieguo.setFont(QFont("",20))
        self.jieguo.move(105,100)
        self.chuquan=QLabel(self)
        self.chuquan.setText("你的出拳：    ")
        self.chuquan.move(20,10)
        self.dnchuquan = QLabel(self)
        self.dnchuquan.setText("电脑出拳：    ")
        self.dnchuquan.move(170, 10)

        self.show()

    def buttonClicked(self):
        ls=["石头","剪刀","布"]
        a=random.choice(ls)
        self.dnchuquan.setText("电脑出拳:"+a)
        self.chuquan.setText("你的出拳:"+self.sender().text())
        if a==self.sender().text() :
            self.jieguo.setText("平局")
        if a=="石头" and self.sender().text()=="剪刀" :
            self.jieguo.setText("你输了")
        if a == "石头" and self.sender().text() == "布":
            self.jieguo.setText("你赢了")
        if a == "剪刀" and self.sender().text() == "布":
            self.jieguo.setText("你输了")
        if a == "剪刀" and self.sender().text() == "石头":
            self.jieguo.setText("你赢了")
        if a == "布" and self.sender().text() == "剪刀":
            self.jieguo.setText("你赢了")
        if a == "布" and self.sender().text() == "石头":
            self.jieguo.setText("你输了")


        # username = QLabel(self)
        # username.setText("用户名：")
        # username.setToolTip("请输入您的用户名：")
        # username.move(70,150)
        # usernameedit=QLineEdit(self)
        # usernameedit.setPlaceholderText("请输入用户名")
        # usernameedit.move(120,145)
        # pass_word =QLabel(self)
        # pass_word.setText("密码：")
        # pass_word.move(70,175)
        # pass_wordedit=QLineEdit(self)
        # pass_wordedit.setPlaceholderText("请输入密码")
        # pass_wordedit.move(120,170)
        # logo_enter=QLabel(self)
        # logo_enter.setPixmap(QPixmap("剪子.png"))
        # logo_enter.move(90,30)
        # QToolTip.setFont(QFont("",20))


if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())