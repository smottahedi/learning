#include <stdio.h>
#include <tensorflow/c/c_api.h>

int main() {
    printf("hello tensorflow version %s\n", TF_Version());
    return 0;
}
