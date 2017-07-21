#include <stdio.h>

int main()
{
    char str[8] = "abcdefg";
    char *alt = str;

    printf("str= %p\n", str);
    printf("&str= %p\n", &str);
    printf("*str=    %c\n", *(str));
    printf("*(&str)= %s\n", *(&str));

    printf("alt= %p\n", alt);
    printf("&alt= %p\n", &alt);
    printf("*alt=    %c\n", *(alt));
    printf("*(&alt)= %s\n", *(&alt));
    return 0;
}
