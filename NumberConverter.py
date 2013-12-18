'''
@Date: I don't remeber xD 
@Author: Abrelrahman Moez (aka - Hydra)
@Script: NumberConverter.py
@Description: Number systems converter
@Version: 1.0
'''
from PyQt4 import QtGui, QtCore
import sys
import webbrowser
# ----------------------------

class UI(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		#
		self.number_conversion = QtGui.QLabel('Number Converter', self)
		self.number_conversion.setStyleSheet('color: #9B2022; font-size: 18px; font: bold ')
		self.number_conversion.move(65,30)
		# Number
		self.number_gb = QtGui.QGroupBox(self)
		self.number_gb.setStyleSheet('QGroupBox {background: #d9d9d9; border-radius: 5px;}')
		self.number_gb.move(20,80)
		self.number_gb.resize(250,120)

		self.bin_rad = QtGui.QRadioButton('Bin', self.number_gb)
		self.bin_rad.move(10,10)

		self.oct_rad = QtGui.QRadioButton('Oct', self.number_gb)
		self.oct_rad.move(65,10)

		self.dec_rad = QtGui.QRadioButton('Dec', self.number_gb)
		self.dec_rad.move(115,10)

		self.hex_rad = QtGui.QRadioButton('Hex', self.number_gb)
		self.hex_rad.move(170,10)

		self.number_label = QtGui.QLabel('Number to convert',self.number_gb)
		self.number_label.move(10,50)

		self.number = QtGui.QLineEdit(self.number_gb)
		self.number.textChanged.connect(self.initConversion)
		self.number.move(10,80)
		self.number.resize(230,30)		

		# GroupBox Shadow
		self.groubbox_shadow = QtGui.QGraphicsDropShadowEffect(self)
		self.groubbox_shadow.setBlurRadius(8)
		self.groubbox_shadow.setOffset(1,1)
		self.groubbox_shadow.setColor(QtGui.QColor(63, 63, 63, 180))
		self.number_gb.setGraphicsEffect(self.groubbox_shadow)

		# Conversion
		self.conversion = QtGui.QGroupBox(self)
		self.conversion.setStyleSheet('QGroupBox {background: #d9d9d9; border-radius: 5px;}')
		self.conversion.move(20,220)
		self.conversion.resize(250,190)
		# Groupbox Shadow
		self.groubbox_shadow = QtGui.QGraphicsDropShadowEffect(self)
		self.groubbox_shadow.setBlurRadius(8)
		self.groubbox_shadow.setOffset(1,1)
		self.groubbox_shadow.setColor(QtGui.QColor(63, 63, 63, 180))
		self.conversion.setGraphicsEffect(self.groubbox_shadow)

		self.decimal_label = QtGui.QLabel('Dec:', self.conversion)
		self.decimal_label.move(20,20)
		self.dec = QtGui.QLineEdit(self.conversion)
		self.dec.move(70,15)

		self.bin_label = QtGui.QLabel('Bin:', self.conversion)
		self.bin_label.move(20,60)
		self.bin = QtGui.QLineEdit(self.conversion)
		self.bin.move(70,55)

		self.oct_label = QtGui.QLabel('Oct:', self.conversion)
		self.oct_label.move(20,100)
		self.oct = QtGui.QLineEdit(self.conversion)
		self.oct.move(70,95)
		
		self.hex_label = QtGui.QLabel('Hex:', self.conversion)
		self.hex_label.move(20,140)
		self.hex = QtGui.QLineEdit(self.conversion)
		self.hex.move(70,135)		
		#
		self.contact_button = QtGui.QPushButton('Contact?', self)
		self.contact_button.move(190,425)
		self.contact_button.clicked.connect(self.contact)
		#
		self.resize(290,460)
		self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())
		self.setWindowTitle('Numbers Systems - v1.0')
	def initConversion(self):
		if self.bin_rad.isChecked():
			dec = int(str(self.number.text()), 2)
		
		elif self.oct_rad.isChecked():
			dec = int(str(self.number.text()), 8)
		
		elif self.dec_rad.isChecked():
			dec = int(str(self.number.text()), 10)

		elif self.hex_rad.isChecked():
			dec = int(str(self.number.text()), 16)
			
		else:
			msg_box = QtGui.QMessageBox.critical(self, 'Error', 'You did not enter number system.', QtGui.QMessageBox.Ok)
			return
		
		if not dec:
			return

		try:
			dec_value = dec
		except:
			dec_value = ''
		
		try:
			bin_value = bin(dec)[2:]
		except:
			bin_value = ''
		
		try:
			oct_value = oct(dec)
		except:
			oct_value = ''
		try:
			hex_value = hex(dec)[2:]
		except:
			hex_value = ''
		#
		self.dec.setText(str(dec_value))
		self.bin.setText(str(bin_value))
		self.oct.setText(str(oct_value))
		self.hex.setText(str(hex_value))
	def openURL(self):
		webbrowser.open('http://www.facebook.com/Hacker.Bedo')
	def contact(self):
		self.goContact = Contact()
		self.goContact.show()
#
class Contact(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.resize(300,150)
		self.setWindowTitle('Contact')
		#
		self.contact_container = QtGui.QGroupBox(self)
		self.contact_container.move(20,20)
		self.contact_container.resize(260,110)
		#self.contact_container.setStyleSheet('QLabel{color: red;')		
		#
		self.twitter = QtGui.QLabel('<b>Follow: <a style="text-decoration: none" href="http://twitter.com/abdelrahmanmoez">Twitter</a>', self.contact_container)
		self.twitter.move(20,20)
		self.twitter.linkActivated.connect(self.twitterOpener)
		#
		self.facebook = QtGui.QLabel('<b>Like:   <a style="text-decoration: none" href="https://www.facebook.com/The.Hydra.Python.Programmer"> Facebook </a>', self.contact_container)
		self.facebook.move(20,40)
		self.facebook.linkActivated.connect(self.facebookOpener)
		#
		self.github = QtGui.QLabel('<b> Follow: <a style="text-decoration: none" href="https://github.com/Hydr4/"> Github </a>', self.contact_container)
		self.github.move(20,60)
		self.github.linkActivated.connect(self.githubOpener)
		#
		self.mail = QtGui.QLabel('<b> Email: <a style="text-decoration: none" href="mailto:abdelrahman.moez@gmail.com"> abdelrahman.moez@gmail.com </a><b>', self.contact_container)
		self.mail.move(20,80)
		self.mail.linkActivated.connect(self.mailOpener)
	def twitterOpener(self):
		webbrowser.open('http://twitter.com/abdelrahmanmoez')
	def facebookOpener(self):
		webbrowser.open('https://www.facebook.com/The.Hydra.Python.Programmer')
	def githubOpener(self):
		webbrowser.open('https://github.com/Hydr4/')
	def mailOpener(self):
		webbrowser.open('mailto:abdelrahman.moez@gmail.com')

def main():
	app =  QtGui.QApplication(sys.argv)
	foo = UI()
	foo.show()
	sys.exit(app.exec_())
#
main()
