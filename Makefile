.PHONY: pdf empty

TEXFILES = task_report
SRCDIR = latex
BUILDDIR = bin
ENDDIR = docs

GIT_HASH := $(shell git rev-parse --short HEAD)
BUILD_DATE := $(shell date "+%Y-%m-%d")

define VERSION_INFO
\def\gitcommit{$(GIT_HASH)}
\\def\\builddate{${BUILD_DATE}}
endef

export VERSION_INFO

pdf:
	@echo "$$VERSION_INFO" > $(SRCDIR)/version.tex
	@for file in $(TEXFILES); do \
		echo "Compiling $$file..."; \
		(cd $(SRCDIR) && latexmk -pdf -silent $$file.tex); \
		mv $(BUILDDIR)/$$file.pdf $(ENDDIR)/$$file.pdf; \
	done
	jupyter nbconvert --to pdf --output-dir=docs notebooks/wine_analysis.ipynb

empty:
	@echo "Cleaning $(BUILDDIR)..."
	@rm -f $(BUILDDIR)/*.aux \
	        $(BUILDDIR)/*.log \
	        $(BUILDDIR)/*.fls \
	        $(BUILDDIR)/*.out \
	        $(BUILDDIR)/*.synctex.gz \
	        $(BUILDDIR)/*.fdb_latexmk

task1A:
	python src/task1A.py

task1B:
	python src/task1B.py

task1C:
	python src/task1C.py

notebook:
	jupyter nbconvert --to pdf --execute notebooks/wine_analysis.ipynb --output-dir=docs
