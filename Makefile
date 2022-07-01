.PHONY: all build mkdirs clean venv

all: build

mkdirs: clean
	mkdir -p build

build: mkdirs
	make -C clib
	python3 setup.py build_ext --inplace

clean:
	rm -rf build *.egg-info *.so loop.c
	make -C clib clean

