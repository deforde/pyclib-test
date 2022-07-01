.PHONY: all

all: libfoo

builddir: clean
	mkdir build

libfoo: builddir
	$(CC) -g3 -Wall -Wextra -Werror -pedantic -shared -fPIC foo.c -o build/libfoo.so

clean:
	rm -rf build

