TEXFILES = report notes
SRCDIR = docs
BUILDDIR = bin

GIT_HASH := $(shell git rev-parse --short HEAD)
BUILD_DATE := $(shell date "+%Y-%m-%d")

define VERSION_INFO
\def\gitcommit{$(GIT_HASH)}
\def\builddate{$(BUILD_DATE)}
endef

export VERSION_INFO

latex:
	@echo "$$VERSION_INFO" > $(SRCDIR)/version.tex
	@for file in $(TEXFILES); do \
		echo "Compiling $$file..."; \
		(cd $(SRCDIR) && latexmk -pdf -silent $$file.tex); \
		mv $(BUILDDIR)/$$file.pdf $(SRCDIR)/$$file.pdf; \
	done

clean:
	@echo "Cleaning $(BUILDDIR)..."
	@rm -f $(BUILDDIR)/*.aux \
	        $(BUILDDIR)/*.log \
	        $(BUILDDIR)/*.fls \
	        $(BUILDDIR)/*.out \
	        $(BUILDDIR)/*.synctex.gz \
	        $(BUILDDIR)/*.fdb_latexmk
