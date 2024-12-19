#include <stdio.h>
#include <omp.h>
#include <limits.h>

/* this is my input hand dis-assembled */
int run(unsigned long a) {
    unsigned long b = 0;
    unsigned long c = 0;
    int ip = 0;

    int output[20];
    int outsize = 0;

    do {
        b = a & 7;  // 2 4
        b = b ^ 3;  // 1 3
        c = a >> b; // 7 5
        b = b ^ 5;  // 1 5
        a = a >> 3; // 0 3
        b = b ^ c;  // 4 1
        output[outsize++] = (b & 7); // 5 5
        if (outsize > 16) {
            return 0;
        }
        
        // 3 0
    } while (a != 0);

    int answer [] = {2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 1, 5, 5, 3, 0};
    if (outsize != 16) return 0;
    for (int i = 0; i < 16; i++) {
        if (output[i] != answer[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
#pragma omp parallel for num_threads(16)
    for (unsigned long a = 0; a < 0x1000000000000; a++) {
        if (a & 10000000 == 0x10000000000) printf("%lu\n", a);
        if (run(a)) {
            printf("FOUND ONE: %lu\n", a);
        }
    }

    return 0;
}

