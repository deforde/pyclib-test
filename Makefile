.PHONY: all build mkdirs clean venv

all: build

mkdirs: clean
	mkdir -p build

build: mkdirs
	make -C clib
	python3 setup.py build_ext -b build -t build

clean:
	rm -rf build
	make -C clib clean

