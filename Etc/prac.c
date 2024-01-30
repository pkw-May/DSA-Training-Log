#include <stdio.h>
 
int main(void) {
 
    // int num;    // 일반 변수 선언
    int * a;    // 포인터 선언
    
    *a = 10;    // 포인터에 num 주소 대입
    // *pnum = 10;    // 포인터로 변수 num에 10 
 
    printf("a 자체 : %d\n", a);
    printf("주소 : %d\n", &a);
    printf("a 포인터가 가리키는 값 : %d\n", *a);
 
    return 0;
}