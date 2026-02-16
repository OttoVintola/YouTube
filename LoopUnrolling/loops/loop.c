#include <stdio.h>          // printf()
#include <stdint.h>         // uint64_t
#include <x86intrin.h>      // __rdtsc()

int main(void) {
    int n = 1 << 20;
    int j = 0;

    uint64_t start = __rdtsc();

    for (int i = 0; i < n; i++) {
        j += 5;
    }

    uint64_t end = __rdtsc();

    printf("Result: %d, Cycles: %llu\n", j, (unsigned long long)(end - start));
    return j;
}
