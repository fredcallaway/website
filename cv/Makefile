# SRC = $(wildcard *.md)
SRC = cv.md

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
LATEX_TEMPLATE=template.tex

all:    clean $(PDFS) $(HTML)
	mv cv.pdf callaway-cv.pdf
	cp callaway-cv.pdf ../output
	open callaway-cv.pdf


pdf:   clean $(PDFS)
html:  clean $(HTML)

%.html: %.md
	python resume.py html $(GRAVATAR_OPTION) < $< | pandoc -f markdown+superscript -t html -c resume.css -o $@

%.pdf:  %.md $(LATEX_TEMPLATE)
	python resume.py tex < $< | pandoc -f markdown+superscript --template=$(LATEX_TEMPLATE) -H header.tex -o $@
# 	open $@

clean:
	$(RM) *.html *.pdf