.PHONY: book clean
BOOK?=book
JB:=$(shell python -c 'import sysconfig, os; print(os.path.join(sysconfig.get_path("scripts"), "jupyter-book"))')
book:
	"$(JB)" build $(BOOK)
clean:
	rm -rf $(BOOK)/_build
