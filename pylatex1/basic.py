from pylatex import Document, Section, Subsection, Package, Command, Math
from pylatex.utils import italic, NoEscape


if __name__ == '__main__':
    # Basic document
    doc = Document('basic',
                   documentclass='exam',
                   document_options='11pt',
                   fontenc=None,
                   inputenc=None,
                   font_size=None,
                   textcomp=False,
                   lmodern=False,
                   page_numbers=False
                   )
    #    doc.documentclass = Command(
    #        'documentclass',
    #        options=['11pt'],
    #        arguments=['exam'],
    #    )

    with doc.create(Section('dddd')):
        doc.append('111')
        doc.append('222')
        q1=1
        doc.append(Math(data=['F=',q1],inline=1))
    #        env=Env

    doc.packages.append(Package('amssymb, amsfonts, latexsym, verbatim, xspace, setspace,tikz,multicol'))

    doc.packages.append(Command('usetikzlibrary','plotmarks'))

    doc.packages.append(Command('singlespacing'))

    doc.packages.append(Command('parindent 0ex'))

    #    doc.packages.append(Package('geometry',
    #        options=['a6paper', 'showframe']))

    doc.generate_tex()
#    doc.generate_pdf(compilers = ('latexmk',[]),clean_tex=False)
    