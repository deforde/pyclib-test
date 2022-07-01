#include <math.h>
#include <stddef.h>

float foo(float i)
{
    return sqrtf(i);
}

void foov(float* v, size_t n, float* u)
{
    for(size_t i = 0; i < n; ++i) {
        u[i] = foo(v[i]);
    }
}
