from pylatex.base_classes import Environment, Command, Container, LatexObject, UnsafeCommand, CommandBase, Arguments
# from pylatex.package import Package
from pylatex.utils import dumps_list, rm_temp_dir, NoEscape,bold,italic
from pylatex import Document, Package, Command, MiniPage,LongTabu, Tabu, Center,Tabular
from pylatex.lists import List,Itemize,Enumerate


import time
from datetime import date
from datetime import datetime
from datetime import timedelta

import re
from random import randint

def outputdate(date):
    if date.month==1:
        r='Jan. '
    elif date.month==2:
        r='Feb. '
    elif date.month==3:
        r='Mar. '
    elif date.month==4:
        r='Apr. '
    elif date.month==5:
        r='May '
    elif date.month==6:
        r='Jun. '
    elif date.month==7:
        r='Jul. '
    elif date.month==8:
        r='Aug. '
    elif date.month==9:
        r='Sep. '
    elif date.month==10:
        r='Oct. '
    elif date.month==11:
        r='Nov. '
    elif date.month==12:
        r='Dec. '
    r=r+str(date.day)
    return r


doc = Document('Syllabus',
               documentclass='amsart',
               document_options='10pt',
               fontenc=None,
               inputenc=None,
               # font_size=None,
               textcomp=False,
               lmodern=False,
               # page_numbers=False
               )
# packages and some basic settings
doc.packages.append(Package('amssymb, amsfonts, latexsym, verbatim, xspace, setspace,tikz,multicol,amsmath,multirow,amsthm,mathrsfs,fancyhdr,bbm,url'))
# doc.packages.append(Package('geometry','margin=1in'))

doc.packages.append(Command('textwidth 15.3cm'))
doc.packages.append(Command('textheight 24cm'))
doc.packages.append(Command('hoffset=-3.2cm'))
doc.packages.append(Command('voffset=-1cm'))
doc.packages.append(Command('oddsidemargin=3.2cm'))
doc.packages.append(Command('evensidemargin=3.2cm'))
doc.packages.append(Command('parindent=0pt'))
doc.packages.append(Command('setlength',Arguments(Command('baselineskip'),'20pt')))
doc.packages.append(Command('renewcommand',Arguments(Command('baselinestretch'),'1.2')))


classname=r'MATH 10B: Calculus of Several Variables II'
classquarter=r'Spring'
classyear=r'2018'
firstday=date(2018,4,2)
oneday=timedelta(days=1)
# oneweek=timedelta(weeks=1)

holiday=[date(2018,5,28)]

num_of_col=3
fmt = '|l'*num_of_col+'|'
with doc.create(Tabular(fmt)) as data_table:
    header_row1 = ["Date", "Contents", "Assignments Due Date"]
    data_table.add_hline()
    data_table.add_row(header_row1, mapper=[bold])
    data_table.add_hline()

    day=firstday

    with open('coursedata.txt','r') as file:
        coursedata=file.read()

    with open('discussiondata.txt','r') as file:
        discussiondata=file.read()

    with open('assignmentdue.txt','r') as file:
        assignmentdue=file.read()

    coursedata=coursedata.split('\n')
    discussiondata=discussiondata.split('\n')
    assignmentdue=assignmentdue.split('\n')
    assdue=[]
    assweek=[]
    for a in assignmentdue:
        b=a.split('||')
        assdue.append(b[1])
        assweek.append(b[0])


    courseindex=0
    disindex=0
    assindex=0

    if firstday.weekday()!=0:
        pass
    for i in range(10):
        for j in range(5):
            firstcol=outputdate(day)
            thirdcol=''
            if day.weekday() in [0,2,4]:
                if day not in holiday:
                    secondcol=NoEscape(coursedata[courseindex])
                    courseindex=courseindex+1
                else:
                    secondcol=NoEscape(r'*Holiday*')
                if day.weekday()==0:
                    if str(i+1) in assweek:
                        thirdcol=NoEscape(assdue[assindex]+' '+outputdate(day+oneday*11))
                        assindex=assindex+1

                row=[firstcol,secondcol,thirdcol]
                data_table.add_row(row)
            elif day.weekday()==3:
                if day not in holiday:
                    secondcol=NoEscape(discussiondata[disindex])
                    disindex=disindex+1
                else:
                    secondcol=NoEscape(r'*Holiday*')

                row=[firstcol,secondcol,thirdcol]
                data_table.add_row(row)
            day=day+oneday
        data_table.add_hline()
        day=day+oneday*2


with open('try.txt','r') as file:
    dataa=file.read()


# ans=re.findall(r'\\begin{solution}(.*?)\\end{solution}',dataa,re.S)
#
# doc.append(NoEscape(ans[0]))




doc.generate_tex()

