# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 13:46:54 2018

@author: xinli
"""

from html.parser import HTMLParser
from html.entities import name2codepoint
import copy

class MyData():
    def __init__(self,tag=""):
        self.name=tag
        self.attr=list()
        self.isobj=True # False is strings
        self.content=list()

    def dumps(self):
        r=""
        if self.isobj is False:
            r=self.content[0]
        else:
            for cont in self.content:
                r=r+cont.dumps()
        return r

    def getname(self):
        return self.name

    def getcontent(self):
        return self.content

    def getdatafrom(self, AnData):
        self.name=AnData.getname()
        if AnData.isobj is False:
            self.content=[AnData.getcontent()[0]]
        else:
            pass

    def append(self,anything):
        self.content.append(anything)

#    def dumps(self):
#        if self.content
#        s=self.name+" : {\n"
#        for item in self.content:
#            s=s+item.dumps()+'\n'
#        s=s+"}\n"
#        return s


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        # self.maindata=MyData()
        self.currentdata=MyData('main')
        self.stack=list()

    def getdata(self):
        return self.currentdata

    def handle_starttag(self, tag, attrs):
        self.stack.append(self.currentdata)
        self.currentdata= MyData(tag)


    def handle_endtag(self, tag):
        if self.stack:
            temp=self.stack.pop()
            temp.append(self.currentdata)
            self.currentdata.getdatafrom(temp)

    def handle_data(self, data):
        self.currentdata.append(data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()

parser.feed('<html><title>Test</title></html>')
m=parser.getdata()