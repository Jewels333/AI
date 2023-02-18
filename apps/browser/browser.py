
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

# main window
class MainWindow(QMainWindow):

	# constructor
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		# creating a tab widget
		self.tabs = QTabWidget()

		
		self.tabs.setDocumentMode(True)

		
		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

		
		self.tabs.currentChanged.connect(self.current_tab_changed)

		# making tabs closeable
		self.tabs.setTabsClosable(True)

		
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.setCentralWidget(self.tabs)
		# creating a status bar
		self.status = QStatusBar()
		# setting status bar to the main window
		self.setStatusBar(self.status)
		# creating a tool bar for navigation
		navtb = QToolBar("Navigation")
		self.addToolBar(navtb)
		#back
		back_btn = QAction("Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		navtb.addAction(back_btn)
		#forward
		next_btn = QAction("Forward", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		navtb.addAction(next_btn)
		#reload
		reload_btn = QAction("Reload", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		navtb.addAction(reload_btn)
        #home
		home_btn = QAction("Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)
		#separator
		navtb.addSeparator()
		#url 
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		navtb.addWidget(self.urlbar)
		# stop
		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		navtb.addAction(stop_btn)
		#creating 1 tab
		self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')
		# showing 
		self.show()

		# set title 
		self.setWindowTitle("Scripted Browser")
#	adding tabs
	def add_new_tab(self, qurl = None, label ="Blank"):

		# if url is blank
		if qurl is None:
			# creating a google url
			qurl = QUrl('http://www.google.com')

		# creating a QWebEngineView object
		browser = QWebEngineView()

		# setting url to browser
		browser.setUrl(qurl)

		# setting tab index
		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)
		# update the url
		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))
		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))
	def tab_open_doubleclick(self, i):

		if i == -1:
			# creating a new tab
			self.add_new_tab()

	# when tab is changed
	def current_tab_changed(self, i):
		qurl = self.tabs.currentWidget().url()
		# update the url
		self.update_urlbar(qurl, self.tabs.currentWidget())
		# update the title
		self.update_title(self.tabs.currentWidget())
	# when tab is closed
	def close_current_tab(self, i):
		# if there is only one tab
		if self.tabs.count() < 2:
			# do nothing
			return
		# else remove the tab
		self.tabs.removeTab(i)

	def update_title(self, browser):
		# if signal is not from the current tab
		if browser != self.tabs.currentWidget():
			# do nothing
			return
		# get the page title
		title = self.tabs.currentWidget().page().title()
		# set the window title
		self.setWindowTitle("% s - Scripted Browser" % title)
	#home
	def navigate_home(self):

		# google
		self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))
	#navigate to url
	def navigate_to_url(self):

		#convert url
		q = QUrl(self.urlbar.text())
		if q.scheme() == "":
			
			q.setScheme("http")
		# set the url
		self.tabs.currentWidget().setUrl(q)
	# update 
	def update_urlbar(self, q, browser = None):
		#ignore
		if browser != self.tabs.currentWidget():
			return
		# set text to the url bar
		self.urlbar.setText(q.toString())
		# set cursor position
		self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)
app.setApplicationName("Scripted Browser")
window = MainWindow()
app.exec_()
