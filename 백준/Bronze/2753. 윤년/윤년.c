#include <stdio.h>
#include <string.h>

int main(void)
{

    int year;
    int yes = 0;

    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    {
        yes = 1;
    }

    printf("%d", yes);

    return 0;
}