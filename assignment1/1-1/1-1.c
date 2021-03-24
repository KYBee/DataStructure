#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#pragma warning (disable: 4996)

//5������ ��� �� �������� ���� ũ�� ���� �� �ִ� ������ 10�� �̱� ������ MAX_DEGREE�� 11�� ����
#define MAX_DEGREE 11
#define MAX(a, b) (((a) >= (b)) ? (a) : (b))
#define MIN(a, b) (((a) <= (b)) ? (a) : (b))

//���׽��� ǥ���� �� �ִ� ����ü�� ����
typedef struct {
    int degree;
    int coef[MAX_DEGREE];
} polynomial;

//���Ŀ� ���׽Ŀ� Ư�� ���� �������� ���� output�� �����ֱ� ���� power �Լ�
int power(int x, int y) {
    if (y == 0) return 1;
    return x * power(x, y - 1);
}

//���׽��� �����ִ� �Լ�
polynomial poly_add(polynomial* A, polynomial* B) {
    polynomial C;

    //�� ���׽��� ������ ���̸� ���ؼ� �� ���׽��� ������ ���缭 ���ϱ� ���� ������ degree_diff ����
    int degree_diff = MAX(A->degree, B->degree) - MIN(A->degree, B->degree);
    C.degree = MAX(A->degree, B->degree);

    if (A->degree > B->degree) {
        //���� ���� ������ ���� ���׽��� ��� ���׽��� C�� �����ְ� �ڸ��� �������� �� ���׽��� ����
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

//���׽��� ������ ���� �Լ�
polynomial poly_mul(polynomial* A, polynomial* B) {
    polynomial D;
    D.degree = A->degree + B->degree;

    for (int i = 0; i <= D.degree; i++)
        D.coef[i] = 0;

    //���׽��� ���� ����
    for (int i = 0; i <= A->degree; i++)
        for (int j = 0; j <= B->degree; j++) {
            D.coef[i + j] += A->coef[i] * B->coef[j];
        }
    return D;
}

//���ڿ��� �Է¹��� ���׽� ������ ���� ���ڷ� ��ȯ�Ͽ� ���׽Ŀ� �����ϴ� initialize �Լ�
void poly_init(char str[], polynomial poly[]) {
    char* number = strtok(str, " ");
    int i = 0;

    while (number != NULL) {
        poly->coef[i++] = atoi(number);
        number = strtok(NULL, " ");
    }
    poly->degree = i - 1;
}

//���׽��� ����ϴ� �Լ�
void poly_print(polynomial poly[]) {
    for (int i = 0; i <= poly->degree; i++) {
        printf("%d ", poly->coef[i]);
    }
}

//���׽� f(x)�� Ư�� x ���� �־��� �� ��� ���� ��ȯ���ִ� �Լ�
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

    //������ �Է¹ް� initialize ��
    for (int i = 0; i < 2; i++) {
        printf("���� %d�� �Է��ϼ��� : ", i + 1);
        gets(str);
        poly_init(str, &poly[i]);
    }

    //���׽��� ������ ���� �����ؼ� ������
    poly[2] = poly_add(&poly[0], &poly[1]);
    poly[3] = poly_mul(&poly[0], &poly[1]);

    //��� ���
    for (int i = 2; i < 4; i++) {
        printf("���� 1 %c 2 �� ", op[i % 2]);
        poly_print(&poly[i]);
        printf("\n");
    }

    //x�� Ư�� ���� ����
    while (1) {
        printf("���Ŀ� ���� �������� ");
        scanf("%d %d", &y, &x);
        printf("������� %d\n", poly_get_value(&poly[y - 1], x));
    }

    return 0;
}