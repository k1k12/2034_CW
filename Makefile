.PHONY: pdf empty

TEXFILES = task_report
SRCDIR = latex
BUILDDIR = bin docs figures
BIN = bin
ENDDIR = docs

GIT_HASH := $(shell git rev-parse --short HEAD)
BUILD_DATE := $(shell date "+%Y-%m-%d")

define VERSION_INFO
\def\gitcommit{$(GIT_HASH)}
\\def\\builddate{${BUILD_DATE}}
endef

export VERSION_INFO

pdf:
	jupyter nbconvert --to pdf --output-dir=docs notebooks/wine_analysis.ipynb
	@echo "$$VERSION_INFO" > $(SRCDIR)/version.tex
	@for file in $(TEXFILES); do \
		echo "Compiling $$file..."; \
		(cd $(SRCDIR) && latexmk -pdf -silent $$file.tex); \
		mv $(BUILDDIR)/$$file.pdf $(ENDDIR)/$$file.pdf; \
	done

empty:
	@for dir in $(BUILDDIR); do \
		echo "Cleaning $$dir..."; \
		rm -f $$dir/*.aux $$dir/*.log $$dir/*.fls $$dir/*.out $$dir/*.synctex.gz $$dir/*.fdb_latexmk $$dir/*.pdf $$dir/*.png; \
	done

bin empty:
	@for dir in $(BIN); do \
		echo "Cleaning $$dir..."; \
		rm -f $$dir/*.aux $$dir/*.log $$dir/*.fls $$dir/*.out $$dir/*.synctex.gz $$dir/*.fdb_latexmk $$dir/*.pdf $$dir/*.png; \
	done

task1A:
	python src/task1A.py

task1B:
	python src/task1B.py

task1D:
	python src/task1D.py

task3:
	python src/task3.py

exten:
	python src/exten.py

notebook:
	jupyter nbconvert --to pdf --execute notebooks/wine_analysis.ipynb --output-dir=docs
