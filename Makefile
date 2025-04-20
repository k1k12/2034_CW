.PHONY: pdf empty

TEXFILES = report task1A
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

notebook:
	jupyter nbconvert --to notebook --execute notebooks/wine_analysis.ipynb \
		--output wine_analysis_output.ipynb \
		--output-dir notebooks
