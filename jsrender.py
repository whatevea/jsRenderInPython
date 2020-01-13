from flask import Flask,request,jsonify
import requests
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import sys
import bs4 as bs
import urllib.request
class Client(QWebEnginePage):
    def __init__(self,url):
        global app
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ""
        self.loadFinished.connect(self.on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print("Load Finished")

    def Callable(self,data):
        self.html = data
        self.app.quit()

app= Flask(__name__)
@app.route('/<string:urlq>')
def nulljson(urlq):
	urlq=urlq.replace('*','/')
	response = Client(urlq).html
	# response.headers.add('Access-Control-Allow-Origin', '*')
	# response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	# response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response
app.run()