#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{

    char *alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int count[26] = {0};
    int maxIdx;
    int isDup;
    char str[1000005];

    scanf("%s", str);

    // add count to alphabet counts list
    for (int i = 0; i < strlen(str); i++)
    {
        char *idx = strchr(alph, toupper(str[i]));
        if (idx != NULL)
        {
            count[idx - alph] += 1;
        }
    }

    // find max count in alphabet counts list
    maxIdx = 0;
    for (int i = 1; i < 26; i++)
    {
        if (count[maxIdx] < count[i])
        {
            maxIdx = i;
        }
    }

    // find duplicated max count
    isDup = 0;
    for (int i = 0; i < 26; i++)
    {
        if (count[i] == count[maxIdx])
        {
            isDup++;
        }
    }

    // print result
    if (isDup >= 2)
    {
        printf("?");
    }
    else
    {
        printf("%c", alph[maxIdx]);
    }

    return 0;
}