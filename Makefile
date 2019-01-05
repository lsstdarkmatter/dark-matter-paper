main:
	#latexmk -g -f -pdf -interaction=nonstopmode main
	latexmk -g -pdf  main


clean:
	rm -f *.blg *.fdb_latexmk *.fls main.log main.bbl  mainNotes.bib *.aux
