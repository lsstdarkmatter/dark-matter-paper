main:
	#latexmk -g -f -pdf -interaction=nonstopmode main
	latexmk -g -pdf main

plot:
	python plotting/plot_macho.py
	python plotting/plot_bsdm.py
	python plotting/plot_id_ann.py

clean:
	rm -f *.blg *.fdb_latexmk *.fls main.log main.bbl  mainNotes.bib *.aux
