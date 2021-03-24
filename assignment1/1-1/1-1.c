#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#pragma warning (disable: 4996)

//5차식의 계산 즉 곱셈에서 가장 크게 나올 수 있는 차수는 10차 이기 때문에 MAX_DEGREE를 11로 정의
#define MAX_DEGREE 11
#define MAX(a, b) (((a) >= (b)) ? (a) : (b))
#define MIN(a, b) (((a) <= (b)) ? (a) : (b))

//다항식을 표현할 수 있는 구조체를 정의
typedef struct {
    int degree;
    int coef[MAX_DEGREE];
} polynomial;

//이후에 다항식에 특정 값을 대입했을 때의 output을 구해주기 위한 power 함수
int power(int x, int y) {
    if (y == 0) return 1;
    return x * power(x, y - 1);
}

//다항식을 더해주는 함수
polynomial poly_add(polynomial* A, polynomial* B) {
    polynomial C;

    //두 다항식의 차수의 차이를 구해서 두 다항식의 차수를 맞춰서 더하기 위해 정의한 degree_diff 변수
    int degree_diff = MAX(A->degree, B->degree) - MIN(A->degree, B->degree);
    C.degree = MAX(A->degree, B->degree);

    if (A->degree > B->degree) {
        //먼저 높은 차수를 가진 다항식을 결과 다항식인 C에 더해주고 자리가 맞춰지면 두 다항식을 더함
        for (int i = 0; i < degree_diff; i++)
            C.coef[i] = A->coef[i];

        for (int i = 0, j = degree_diff; i <= MIN(A->degree, B->degree); i++, j++)
            C.coef[j] = A->coef[j] + B->coef[i];
    }
    else {
        for (int i = 0; i < degree_diff; i++)
            C.coef[i] = B->coef[i];

        for (int i = 0, j = degree_diff; i <= MIN(A->degree, B->degree); i++, j++)
            C.coef[j] = A->coef[i] + B->coef[j];
    }
    return C;
}

//다항식의 곱셈을 위한 함수
polynomial poly_mul(polynomial* A, polynomial* B) {
    polynomial D;
    D.degree = A->degree + B->degree;

    for (int i = 0; i <= D.degree; i++)
        D.coef[i] = 0;

    //다항식의 곱을 구함
    for (int i = 0; i <= A->degree; i++)
        for (int j = 0; j <= B->degree; j++) {
            D.coef[i + j] += A->coef[i] * B->coef[j];
        }
    return D;
}

//문자열로 입력받은 다항식 정보를 실제 숫자로 변환하여 다항식에 저장하는 initialize 함수
void poly_init(char str[], polynomial poly[]) {
    char* number = strtok(str, " ");
    int i = 0;

    while (number != NULL) {
        poly->coef[i++] = atoi(number);
        number = strtok(NULL, " ");
    }
    poly->degree = i - 1;
}

//다항식을 출력하는 함수
void poly_print(polynomial poly[]) {
    for (int i = 0; i <= poly->degree; i++) {
        printf("%d ", poly->coef[i]);
    }
}

//다항식 f(x)에 특정 x 값을 넣었을 때 결과 값을 반환해주는 함수
int poly_get_value(polynomial poly[], int x) {
    int result = 0, j = 0;
    for (int i = poly->degree; i >= 0; i--) {
        result += power(x, i) * poly->coef[j++];
    }
    return result;
}

int main(void) {
    char* number;
    char str[MAX_DEGREE * 5];
    char op[] = "+*";
    int x, y;
    polynomial poly[4] = { 0 };

    //수식을 입력받고 initialize 함
    for (int i = 0; i < 2; i++) {
        printf("수식 %d을 입력하세요 : ", i + 1);
        gets(str);
        poly_init(str, &poly[i]);
    }

    //다항식의 연산을 각각 수행해서 저장함
    poly[2] = poly_add(&poly[0], &poly[1]);
    poly[3] = poly_mul(&poly[0], &poly[1]);

    //결과 출력
    for (int i = 2; i < 4; i++) {
        printf("수식 1 %c 2 는 ", op[i % 2]);
        poly_print(&poly[i]);
        printf("\n");
    }

    //x에 특정 값을 대입
    while (1) {
        printf("수식에 값을 넣으세요 ");
        scanf("%d %d", &y, &x);
        printf("결과값은 %d\n", poly_get_value(&poly[y - 1], x));
    }

    return 0;
}