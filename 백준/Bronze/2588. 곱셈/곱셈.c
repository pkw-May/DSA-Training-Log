#include <stdio.h>

int main(void)
{
    int n1;
    int n2;

    scanf("%d\n", &n1);
    scanf("%d", &n2);

    printf("%d\n", n1 * (n2 % 10));
    printf("%d\n", n1 * ((n2 % 100)/10));
    printf("%d\n", n1 * ((n2)/100));
    printf("%d", n1 * n2);

    return 0;
}