.ONESHELL:

.PHONY: all build clean install

all: build

build: clean
	make -C clib
	python3 setup.py build_ext --inplace

clean:
	rm -rf build *.egg-info *.so loop.c
	make -C clib clean

install: clean
	rm -rf .venv
	python3 -m venv .venv
	. .venv/bin/activate
	python3 -m pip install Cython numpy
	python3 -m pip install -e .

