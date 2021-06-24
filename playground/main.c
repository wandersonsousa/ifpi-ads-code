#include <stdio.h>

int* create_pointer(){
    int num = 10;
    int* myPointer = &num;
    return myPointer;
}


int main(int argc, char const *argv[])
{
    int* pointer;

    pointer = create_pointer();
    printf("%p\n", pointer);
    return 0;
}
