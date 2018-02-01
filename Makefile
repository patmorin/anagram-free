
ipefigs=$(wildcard figs/*.ipe)
slidefigs=$(wildcard figs/*.ipe)

anagram.pdf : figs anagram.tex anagram.bib $(ipefigs)
	latexmk -pdf anagram.tex 	

figs: $(ipefigs)
	(cd figs; make)

clean :
	rm -f anagram.pdf figs/*.pdf
