#include <stdio.h>

int main(void)
{

    int a;
    int b;
    char res[3] = "";
    scanf("%d %d", &a, &b);

        if (a > b)
    {
        res[0] = '>';
    }
    else if (a < b)
    {
        res[0] = '<';
    }
    else if (a == b)
    {
        res[0] = '=';
        res[1] = '=';
    }

    printf("%s", res);

    return 0;
}