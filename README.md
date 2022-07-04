# pyclib-test

Tests the performance of various techniques for calling `c` functions from `python`.

## Build and run

```
make install
source .venv/bin/activate
make build
export LD_LIBRARY_PATH=$PWD/clib/build
./main.py
```
