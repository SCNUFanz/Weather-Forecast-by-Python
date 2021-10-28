import os, sys, csv, requests, base64     #加载 requests 库，用于网页获取

from bs4 import BeautifulSoup      #加载 BeautifulSoup 库，用于解析获取的网页

from PyQt5.QtWidgets import (QApplication, QMainWindow, QActionGroup, QLineEdit,
                             QLabel, QProgressBar, QSpinBox, QFontComboBox)
#from PyQt5.QtChart import QChartView
from PyQt5.QtCore import Qt, pyqtSlot

from PyQt5.QtGui import QTextCharFormat, QFont, QIcon, QPixmap, QPalette, QBrush

from PyQt5.QtChart import *#QChartView, QChart, QLineSeries, QValueAxis

from ui_Dialog import Ui_Dialog
from ui_WWW import Ui_Tanyunxi

class QmyMainWindow(QMainWindow):
   def __init__(self, parent=None):
      super().__init__(parent)    #调用父类构造函数，创建窗体
      self.ui=Ui_Dialog()         #创建UI对象
      self.ui.setupUi(self)       #构造UI界面
      self.setWindowTitle("城市天气查询系统——By Fanz")    #设置窗体标题

      tempicon = QIcon()     #设置窗体图标
      tempicon.addPixmap(QPixmap('Title.png'))
      self.setWindowIcon(tempicon)

      temppalette = QPalette()   #设置主界面背景
      temppalette.setBrush(QPalette.Background, QBrush(QPixmap('Background.jpg')))
      self.setPalette(temppalette)

      #设置短时预报的文本格式
      self.ui.textEdit.setFontItalic(True)
      self.ui.textEdit.setFontFamily("幼圆")
      self.ui.textEdit.setFontPointSize(15)

      self.setWeatherDay()    #获取未来7天的日期信息并显示在屏幕上


      self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)






   ##----------------------------------自定义槽函数-------------------------------##

   def setWeatherDay(self):       #获取未来七天的日期和星期的具体信息
      url = 'https://www.tianqi.com/tianhequ/'  #
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
      strHtml = requests.get(url, headers=headers)
      strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
      soup = BeautifulSoup(strHtml.text, 'lxml')
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(1)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_2.setText(temp1)
      self.ui.label_3.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(2)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_4.setText(temp1)
      self.ui.label_5.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(3)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_6.setText(temp1)
      self.ui.label_11.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(4)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_7.setText(temp1)
      self.ui.label_12.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(5)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_8.setText(temp1)
      self.ui.label_13.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(6)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_9.setText(temp1)
      self.ui.label_14.setText(temp2)
      nowday = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.week > li:nth-child(7)')
      temp1 = nowday[0].contents[0].get_text()
      temp2 = nowday[0].contents[1].get_text()
      self.ui.label_10.setText(temp1)
      self.ui.label_15.setText(temp2)


   def on_pushButton_clicked(self):                         #获取s四个城市短时预报
      if (self.ui.comboBox2.currentText() == "广州"):        #广州
         url = 'https://www.weaoo.com/guangzhou-181278.html'
         strHtml = requests.get(url)
         strHtml.encoding = strHtml.apparent_encoding       #指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p:nth-child(6)')
         self.ui.textEdit.setText(str1[0].get_text())
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p.mt1.mb2 > span:nth-child(2)')
         self.ui.label_23.setAlignment(Qt.AlignCenter)
         font = QFont()
         font.setBold(True)
         self.ui.label_23.setFont(font)
         self.ui.label_23.setText(str1[0].get_text())

      elif (self.ui.comboBox2.currentText() == "北京"):       #北京
         url = 'https://www.weaoo.com/beijing-181438.html'
         strHtml = requests.get(url)
         strHtml.encoding = strHtml.apparent_encoding        #指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p:nth-child(6)')
         self.ui.textEdit.setText(str1[0].get_text())
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p.mt1.mb2 > span:nth-child(2)')
         self.ui.label_23.setAlignment(Qt.AlignCenter)
         font = QFont()
         font.setBold(True)
         self.ui.label_23.setFont(font)
         self.ui.label_23.setText(str1[0].get_text())

      elif (self.ui.comboBox2.currentText() == "上海"):       #上海
         url = 'https://www.weaoo.com/shanghai-181282.html'
         strHtml = requests.get(url)
         strHtml.encoding = strHtml.apparent_encoding        #指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p:nth-child(6)')
         self.ui.textEdit.setText(str1[0].get_text())
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p.mt1.mb2 > span:nth-child(2)')
         self.ui.label_23.setAlignment(Qt.AlignCenter)
         font = QFont()
         font.setBold(True)
         self.ui.label_23.setFont(font)
         self.ui.label_23.setText(str1[0].get_text())

      else:                                                   #成都
         url = 'https://www.weaoo.com/chengdu-181403.html'
         strHtml = requests.get(url)
         strHtml.encoding = strHtml.apparent_encoding         #指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p:nth-child(6)')
         self.ui.textEdit.setText(str1[0].get_text())
         str1 = soup.select('body > div.forecast-sevendays > div.week-wrapper > div > div > div.pure-u-1-2.curr > p.mt1.mb2 > span:nth-child(2)')
         self.ui.label_23.setAlignment(Qt.AlignCenter)
         font = QFont()
         font.setBold(True)
         self.ui.label_23.setFont(font)
         self.ui.label_23.setText(str1[0].get_text())


   @pyqtSlot(str)
   def on_comboBox2_currentIndexChanged(self, curText1):   #设置两个ComboBox之间的联动,当城市变化时,区也要跟着变化
      if (curText1 == "北京"):
         self.ui.comboBox.clear()
         self.ui.textEdit.clear()
         District = ["海淀区", "朝阳区", "顺义区", "怀柔区", "通州区", "昌平区", "丰台区", "石景山区", "大兴区", "房山区", "门头沟区", "平谷区", "东城区", "西城区", "密云区", "延庆区"]
         self.ui.comboBox.addItems(District)
      elif (curText1 == "上海"):
         self.ui.comboBox.clear()
         self.ui.textEdit.clear()
         District = ["闵行区", "宝山区", "嘉定区", "金山区", "青浦区", "松江区", "奉贤区", "虹口区", "黄浦区", "长宁区", "浦东区", "崇明区", "徐汇区", "静安区", "杨浦区", "南汇区", "徐家汇区"]
         self.ui.comboBox.addItems(District)
      elif (curText1 == "成都"):
         self.ui.comboBox.clear()
         self.ui.textEdit.clear()
         District = ["龙泉驿区", "新都区", "温江区", "锦江区", "青羊区", "金牛区", "武侯区", "成华区", "青白江区", "双流区", "大邑区", "蒲江区", "新津区", "都江堰区", "彭州区", "邛崃区", "崇州区", "简阳区", "金堂区", "郫县区"]
         self.ui.comboBox.addItems(District)
      else:
         self.ui.comboBox.clear()
         self.ui.textEdit.clear()
         District = ["天河区", "白云区", "越秀区", "海珠区", "荔湾区","番禺区","从化区","增城区","黄埔区","花都区","南沙区"]
         self.ui.comboBox.addItems(District)

   @pyqtSlot(str)
   def on_comboBox_currentIndexChanged(self, curText2):
      ######---------------广州---------------######
      if (curText2 == "天河区"):
         url = 'https://www.tianqi.com/tianhequ/'
         self.url_pass(url)
      elif (curText2 == "白云区"):
         url = 'https://www.tianqi.com/baiyun/'
         self.url_pass(url)
      elif (curText2 == "越秀区"):
         url = 'https://www.tianqi.com/yuexiuqu/'
         self.url_pass(url)
      elif (curText2 == "海珠区"):
         url = 'https://www.tianqi.com/haizhuqu/'
         self.url_pass(url)
      elif (curText2 == "荔湾区"):
         url = 'https://www.tianqi.com/liwan/'
         self.url_pass(url)
      elif (curText2 == "番禺区"):
         url = 'https://www.tianqi.com/panyu/'
         self.url_pass(url)
      elif (curText2 == "从化区"):
         url = 'https://www.tianqi.com/conghua/'
         self.url_pass(url)
      elif (curText2 == "增城区"):
         url = 'https://www.tianqi.com/zengcheng/'
         self.url_pass(url)
      elif (curText2 == "黄埔区"):
         url = 'https://www.tianqi.com/huangpuqu/'
         self.url_pass(url)
      elif (curText2 == "花都区"):
         url = 'https://www.tianqi.com/huadu/'
         self.url_pass(url)
      elif (curText2 == "南沙区"):
         url = 'https://www.tianqi.com/nanshaqu/'
         self.url_pass(url)
      ######---------------北京---------------######
      elif (curText2 == "海淀区"):
         url = 'https://www.tianqi.com/haidian/'
         self.url_pass(url)
      elif (curText2 == "朝阳区"):
         url = 'https://www.tianqi.com/chaoyang/'
         self.url_pass(url)
      elif (curText2 == "顺义区"):
         url = 'https://www.tianqi.com/shunyi/'
         self.url_pass(url)
      elif (curText2 == "怀柔区"):
         url = 'https://www.tianqi.com/huairou/'
         self.url_pass(url)
      elif (curText2 == "通州区"):
         url = 'https://www.tianqi.com/tongzhou/'
         self.url_pass(url)
      elif (curText2 == "昌平区"):
         url = 'https://www.tianqi.com/changping/'
         self.url_pass(url)
      elif (curText2 == "丰台区"):
         url = 'https://www.tianqi.com/fengtai/'
         self.url_pass(url)
      elif (curText2 == "石景山区"):
         url = 'https://www.tianqi.com/shijingshan/'
         self.url_pass(url)
      elif (curText2 == "大兴区"):
         url = 'https://www.tianqi.com/daxing/'
         self.url_pass(url)
      elif (curText2 == "房山区"):
         url = 'https://www.tianqi.com/fangshan/'
         self.url_pass(url)
      elif (curText2 == "门头沟区"):
         url = 'https://www.tianqi.com/mentougou/'
         self.url_pass(url)
      elif (curText2 == "平谷区"):
         url = 'https://www.tianqi.com/pinggu/'
         self.url_pass(url)
      elif (curText2 == "东城区"):
         url = 'https://www.tianqi.com/dongchengqu/'
         self.url_pass(url)
      elif (curText2 == "西城区"):
         url = 'https://www.tianqi.com/xichengqu/'
         self.url_pass(url)
      elif (curText2 == "密云区"):
         url = 'https://www.tianqi.com/miyun/'
         self.url_pass(url)
      elif (curText2 == "延庆区"):
         url = 'https://www.tianqi.com/yanqing/'
         self.url_pass(url)
      ######---------------上海---------------######
      elif (curText2 == "闵行区"):
         url = 'https://www.tianqi.com/minhang/'
         self.url_pass(url)
      elif (curText2 == "宝山区"):
         url = 'https://www.tianqi.com/baoshan/'
         self.url_pass(url)
      elif (curText2 == "嘉定区"):
         url = 'https://www.tianqi.com/jiading/'
         self.url_pass(url)
      elif (curText2 == "金山区"):
         url = 'https://www.tianqi.com/jinshan/'
         self.url_pass(url)
      elif (curText2 == "青浦区"):
         url = 'https://www.tianqi.com/qingpu/'
         self.url_pass(url)
      elif (curText2 == "松江区"):
         url = 'https://www.tianqi.com/songjiang/'
         self.url_pass(url)
      elif (curText2 == "奉贤区"):
         url = 'https://www.tianqi.com/fengxian/'
         self.url_pass(url)
      elif (curText2 == "虹口区"):
         url = 'https://www.tianqi.com/hongkou1/'
         self.url_pass(url)
      elif (curText2 == "黄浦区"):
         url = 'https://www.tianqi.com/huangpu1/'
         self.url_pass(url)
      elif (curText2 == "长宁区"):
         url = 'https://www.tianqi.com/changningqu/'
         self.url_pass(url)
      elif (curText2 == "浦东区"):
         url = 'https://www.tianqi.com/pudong/'
         self.url_pass(url)
      elif (curText2 == "崇明区"):
         url = 'https://www.tianqi.com/chongming/'
         self.url_pass(url)
      elif (curText2 == "徐汇区"):
         url = 'https://www.tianqi.com/xuhui/'
         self.url_pass(url)
      elif (curText2 == "静安区"):
         url = 'https://www.tianqi.com/jinganqu/'
         self.url_pass(url)
      elif (curText2 == "杨浦区"):
         url = 'https://www.tianqi.com/yangpuqu/'
         self.url_pass(url)
      elif (curText2 == "南汇区"):
         url = 'https://www.tianqi.com/nanhui/'
         self.url_pass(url)
      elif (curText2 == "徐家汇区"):
         url = 'https://www.tianqi.com/xujiahui/'
         self.url_pass(url)
      ######---------------成都---------------######
      elif (curText2 == "龙泉驿区"):
         url = 'https://www.tianqi.com/longquanyi/'
         self.url_pass(url)
      elif (curText2 == "新都区"):
         url = 'https://www.tianqi.com/xindu/'
         self.url_pass(url)
      elif (curText2 == "温江区"):
         url = 'https://www.tianqi.com/wenjiang/'
         self.url_pass(url)
      elif (curText2 == "锦江区"):
         url = 'https://www.tianqi.com/jinjiangqu/'
         self.url_pass(url)
      elif (curText2 == "青羊区"):
         url = 'https://www.tianqi.com/qingyangqu/'
         self.url_pass(url)
      elif (curText2 == "金牛区"):
         url = 'https://www.tianqi.com/jinniuqu/'
         self.url_pass(url)
      elif (curText2 == "武侯区"):
         url = 'https://www.tianqi.com/wuhouqu/'
         self.url_pass(url)
      elif (curText2 == "成华区"):
         url = 'https://www.tianqi.com/chenghuaqu/'
         self.url_pass(url)
      elif (curText2 == "青白江区"):
         url = 'https://www.tianqi.com/qingbaijiangqu/'
         self.url_pass(url)
      elif (curText2 == "双流区"):
         url = 'https://www.tianqi.com/shuangliu/'
         self.url_pass(url)
      elif (curText2 == "大邑区"):
         url = 'https://www.tianqi.com/dayi/'
         self.url_pass(url)
      elif (curText2 == "蒲江区"):
         url = 'https://www.tianqi.com/pujiang1/'
         self.url_pass(url)
      elif (curText2 == "新津区"):
         url = 'https://www.tianqi.com/xinjin/'
         self.url_pass(url)
      elif (curText2 == "都江堰区"):
         url = 'https://www.tianqi.com/dujiangyan/'
         self.url_pass(url)
      elif (curText2 == "彭州区"):
         url = 'https://www.tianqi.com/pengzhou/'
         self.url_pass(url)
      elif (curText2 == "邛崃区"):
         url = 'https://www.tianqi.com/qionglai/'
         self.url_pass(url)
      elif (curText2 == "崇州区"):
         url = 'https://www.tianqi.com/chongzhou/'
         self.url_pass(url)
      elif (curText2 == "简阳区"):
         url = 'https://www.tianqi.com/jianyang1/'
         self.url_pass(url)
      elif (curText2 == "金堂区"):
         url = 'https://www.tianqi.com/jintang/'
         self.url_pass(url)
      elif (curText2 == "郫县区"):
         url = 'https://www.tianqi.com/pixian/'
         self.url_pass(url)






   def url_pass(self, url):      #画出白天和夜间的气温图像
      self.chart1 = QChart()  # 创建白天温度折线Chart1
      self.chart2 = QChart()  # 创建夜晚温度折线Chart2
      # 创建曲线序列
      series1 = QLineSeries()
      series2 = QLineSeries()
      series1.setName("日间气温折线图")
      series2.setName("夜间气温折线图")

      self.chart1.addSeries(series1)  # 序列添加到图表
      self.chart2.addSeries(series2)  # 序列添加到图表

      temp1 = []
      temp2 = []
      what = []
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
      strHtml = requests.get(url, headers=headers)
      strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
      soup = BeautifulSoup(strHtml.text, 'lxml')

      #设置天气图标
      weather_day7_information = soup.select('body > div.weatherbox > div > div.right > div.day7 > ul.txt.txt2')
      str = weather_day7_information[0].contents[1].get_text()
      str = str.split("转")[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_16.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_16.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_16.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_16.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_16.setPixmap(self.pix)
      self.ui.label_16.setScaledContents(True)
      
      str = weather_day7_information[0].contents[3].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_17.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_17.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_17.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_17.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_17.setPixmap(self.pix)
      self.ui.label_17.setScaledContents(True)

      str = weather_day7_information[0].contents[5].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_18.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_18.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_18.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_18.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_18.setPixmap(self.pix)
      self.ui.label_18.setScaledContents(True)

      str = weather_day7_information[0].contents[7].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_19.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_19.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_19.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_19.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_19.setPixmap(self.pix)
      self.ui.label_19.setScaledContents(True)

      str = weather_day7_information[0].contents[9].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_20.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_20.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_20.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_20.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_20.setPixmap(self.pix)
      self.ui.label_20.setScaledContents(True)

      str = weather_day7_information[0].contents[11].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_21.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_21.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_21.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_21.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_21.setPixmap(self.pix)
      self.ui.label_21.setScaledContents(True)
      
      str = weather_day7_information[0].contents[13].get_text()
      str = str.split('转')[0]
      if (str == "晴"):
         self.pix = QPixmap('sunny.png')
         self.ui.label_22.setPixmap(self.pix)
      elif (str == "阴"):
         self.pix = QPixmap('overcast.png')
         self.ui.label_22.setPixmap(self.pix)
      elif (str == "小雨"):
         self.pix = QPixmap('drizzle.png')
         self.ui.label_22.setPixmap(self.pix)
      elif (str == "大雨"):
         self.pix = QPixmap('downpour.png')
         self.ui.label_22.setPixmap(self.pix)
      else:
         self.pix = QPixmap('cloudy.png')
         self.ui.label_22.setPixmap(self.pix)
      self.ui.label_22.setScaledContents(True)



      str = soup.select('body > div.weatherbox > div > div.right > div.day7 > div > ul')
      for i in range(1, 14, 2):
         temp1.append(int(str[0].contents[i].contents[0].get_text()))
         temp2.append(int(str[0].contents[i].contents[1].get_text()))

      # 序列1添加数值
      t = 1
      for i in range(7):
         y = temp1[i]
         series1.append(t, y)
         t = t + 1
      ##创建坐标轴
      axisX = QValueAxis()  # X 轴
      axisX.setRange(0, 8)  # 设置坐标轴范围
      axisX.setTitleText("day(D)")  # 标题
      axisY = QValueAxis()  # Y 轴
      axisY.setRange(10, 32)
      axisY.setTitleText("白天温度(°C)")
      # 为序列设置坐标轴
      self.chart1.setAxisX(axisX, series1)  # 为序列设置坐标X轴
      self.chart1.setAxisY(axisY, series1)  # 为序列设置坐标X轴
      axisX.setVisible(False)  # X轴不可见
      series1.setColor(Qt.red)
      series1.setPointLabelsVisible(True)
      series1.setPointLabelsFormat("@yPoint")  # 显示点的Y值

      # 序列2添加数值
      t = 1
      for i in range(7):
         y = temp2[i]
         series2.append(t, y)
         t = t + 1
      ##创建坐标轴
      axisX2 = QValueAxis()  # X 轴
      axisX2.setRange(0, 8)  # 设置坐标轴范围
      axisX2.setTitleText("day(D)")  # 标题
      axisY2 = QValueAxis()  # Y 轴
      axisY2.setRange(0, 25)
      axisY2.setTitleText("夜间温度(°C)")
      # 为序列设置坐标轴
      self.chart2.setAxisX(axisX2, series2)  # 为序列设置坐标X轴
      self.chart2.setAxisY(axisY2, series2)  # 为序列设置坐标X轴
      axisX2.setVisible(False)  # X轴不可见
      series2.setColor(Qt.blue)
      series2.setPointLabelsVisible(True)
      series2.setPointLabelsFormat("@yPoint")  # 显示点的Y值
      #shape = QScatterSeries.MarkerShapeRectangle
      series1.setPointsVisible(True)
      series2.setPointsVisible(True)


      self.ui.widget.setChart(self.chart1)
      self.ui.widget_2.setChart(self.chart2)
      self.ui.widget.setCursor(Qt.CrossCursor)      #设置鼠标指针为十字星
      self.ui.widget_2.setCursor(Qt.CrossCursor)    #设置鼠标指针为十字星





class QchindWindow(QMainWindow):    #子窗体
   def __init__(self, parent=None):
      super().__init__(parent)  # 调用父类构造函数，创建窗体
      self.ui = Ui_Tanyunxi()  # 创建UI对象
      self.ui.setupUi(self)  # 构造UI界面
      self.setWindowTitle("24小时空气质量")    #设置窗体标题

      tempicon2 = QIcon()  # 设置窗体图标
      tempicon2.addPixmap(QPixmap('Title2.png'))
      self.setWindowIcon(tempicon2)


      temppalette2 = QPalette()  #设置子界面背景
      temppalette2.setBrush(QPalette.Background, QBrush(QPixmap('Background2.jpg')))
      self.setPalette(temppalette2)


   def decode_base64(data):
      missing_padding = len(data) % 4
      if missing_padding != 0:
         data += b'=' * (4 - missing_padding)
      return base64.b64decode(data)

   @pyqtSlot(str)
   def on_comboBox4_currentIndexChanged(self, curText):
      if (curText == "广州"):
         url = 'https://www.weaoo.com/aqi/guangdong-guangzhou.html'
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
         strHtml = requests.get(url, headers=headers)
         strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         strx = soup.select('body > div.container.aqi-detail > img')
         string1 = str(strx[0])
         string1 = string1.split(';')
         string2 = string1[1]
         string2 = string2.split(',')
         string3 = string2[1]
         string3 = string3.split('"')
         string4 = string3[0]
         missing_padding = len(string4) % 4
         if missing_padding != 0:
            string4 += b'=' * (4 - missing_padding)
         imgdata = base64.b64decode(string4)
         file = open('123.jpg', 'wb')
         file.write(imgdata)
         file.close()
         temp = QPixmap('123.jpg')
         self.ui.label_2.setScaledContents(True)  # 图片自适应大小
         self.ui.label_2.setPixmap(temp)

      elif (curText == "北京"):
         url = 'https://www.weaoo.com/aqi/beijing-beijing.html'
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
         strHtml = requests.get(url, headers=headers)
         strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         strx = soup.select('body > div.container.aqi-detail > img')
         string1 = str(strx[0])
         string1 = string1.split(';')
         string2 = string1[1]
         string2 = string2.split(',')
         string3 = string2[1]
         string3 = string3.split('"')
         string4 = string3[0]
         missing_padding = len(string4) % 4
         if missing_padding != 0:
            string4 += b'=' * (4 - missing_padding)
         imgdata = base64.b64decode(string4)
         file = open('123.jpg', 'wb')
         file.write(imgdata)
         file.close()
         temp = QPixmap('123.jpg')
         self.ui.label_2.setScaledContents(True)  # 图片自适应大小
         self.ui.label_2.setPixmap(temp)

      elif (curText == "上海"):
         url = 'https://www.weaoo.com/aqi/shanghai-shanghai.html'
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
         strHtml = requests.get(url, headers=headers)
         strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         strx = soup.select('body > div.container.aqi-detail > img')
         string1 = str(strx[0])
         string1 = string1.split(';')
         string2 = string1[1]
         string2 = string2.split(',')
         string3 = string2[1]
         string3 = string3.split('"')
         string4 = string3[0]
         missing_padding = len(string4) % 4
         if missing_padding != 0:
            string4 += b'=' * (4 - missing_padding)
         imgdata = base64.b64decode(string4)
         file = open('123.jpg', 'wb')
         file.write(imgdata)
         file.close()
         temp = QPixmap('123.jpg')
         self.ui.label_2.setScaledContents(True)  # 图片自适应大小
         self.ui.label_2.setPixmap(temp)

      else:
         url = 'https://www.weaoo.com/aqi/sichuan-chengdu.html'
         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
         strHtml = requests.get(url, headers=headers)
         strHtml.encoding = strHtml.apparent_encoding  # 指定源网页编码方式作为文字解码方式
         soup = BeautifulSoup(strHtml.text, 'lxml')
         strx = soup.select('body > div.container.aqi-detail > img')
         string1 = str(strx[0])
         string1 = string1.split(';')
         string2 = string1[1]
         string2 = string2.split(',')
         string3 = string2[1]
         string3 = string3.split('"')
         string4 = string3[0]
         missing_padding = len(string4) % 4
         if missing_padding != 0:
            string4 += b'=' * (4 - missing_padding)
         imgdata = base64.b64decode(string4)
         file = open('123.jpg', 'wb')
         file.write(imgdata)
         file.close()

         temp = QPixmap('123.jpg')
         self.ui.label_2.setScaledContents(True)  # 图片自适应大小
         self.ui.label_2.setPixmap(temp)


   def open(self):
      self.show()   #子窗口显示




##  ===========窗体测试程序=================================        
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   Mainwindow = QmyMainWindow()            #创建主窗体
   Childwindow = QchindWindow()
   Mainwindow.show()
   Mainwindow.ui.pushButton3.clicked.connect(Childwindow.open)
   sys.exit(app.exec_())
