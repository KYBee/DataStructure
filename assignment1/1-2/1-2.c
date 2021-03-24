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
    int amount;
    int coef[MAX_DEGREE][2];
} polynomial;

//���Ŀ� ���׽Ŀ� Ư�� ���� �������� ���� output�� �����ֱ� ���� power �Լ�
int power(int x, int y) {
    if (y == 0) return 1;
    return x * power(x, y - 1);
}

//���׽��� �����ִ� �Լ�
void poly_add(polynomial* A, polynomial* B, polynomial* C) {
    int Apos = 0;
    int Bpos = 0;
    int Cpos = 0;
    C->amount = A->amount + B->amount;

    //�� ���׽��� ���� ����� ���� ���� �̸� �˱� ���ؼ� �Ʒ��� while���� ����
    while (Apos < A->amount && Bpos < B->amount) {
        if (A->coef[Apos][1] == B->coef[Bpos][1]) {
            Apos++; Bpos++;
            C->amount -= 1;
        }
        else if (A->coef[Apos][1] > B->coef[Bpos][1])
            Apos++;
        else
            Bpos++;
    }

    //���� ������ �ϴ� ����
    Apos = 0; Bpos = 0;
    while (Apos < A->amount && Bpos < B->amount) {
        if (A->coef[Apos][1] == B->coef[Bpos][1]) {
            C->coef[Cpos][0] = A->coef[Apos][0] + B->coef[Bpos++][0];
            C->coef[Cpos++][1] = A->coef[Apos++][1];
        }
        else if (A->coef[Apos][1] > B->coef[Bpos][1]) {
            C->coef[Cpos][0] = A->coef[Apos][0];
            C->coef[Cpos++][1] = A->coef[Apos++][1];
        }
        else {
            C->coef[Cpos][0] = B->coef[Bpos][0];
            C->coef[Cpos++][1] = B->coef[Bpos++][1];
        }
    }

    if (Apos != A->amount) {
        for (int i = Cpos; i < C->amount; i++) {
            C->coef[i][0] = A->coef[Apos][0];
            C->coef[i][1] = A->coef[Apos++][1];
        }
    }
    else {
        for (int i = Cpos; i < C->amount; i++) {
            C->coef[i][0] = B->coef[Bpos][0];
            C->coef[i][1] = B->coef[Bpos++][1];
        }
    }
}

//���׽��� ������ ���� �Լ�
void poly_mul(polynomial* A, polynomial* B, polynomial* D) {
    D->amount = A->amount * B->amount;

    int already_in_index = 0;
    int Dpos = 0;
    int contained = 0;
    int** temp;
    int* already_in;
    int top_degree = A->coef[0][1] + B->coef[0][1];

    temp = (int**)malloc(sizeof(int) * D->amount);
    for (int i = 0; i < D->amount; i++)
        temp[i] = (int*)malloc(sizeof(int) * 2);
    already_in = (int*)malloc(sizeof(int*) * (top_degree + 1));

    for (int i = 0; i < A->amount; i++)
        for (int j = 0; j < B->amount; j++) {
            temp[Dpos][0] = A->coef[i][0] * B->coef[j][0];
            temp[Dpos++][1] = A->coef[i][1] + B->coef[j][1];
        }

    //D->coef �� amount�� �˱� ����
    Dpos = 0;
    while (Dpos < A->amount * B->amount) {
        contained = 0;

        for (int i = 0; i < already_in_index; i++) {
            if (temp[Dpos][1] == already_in[i]) {
                contained = 1;
                break;
            }
        }
        if (contained)
            D->amount--;
        else
            already_in[already_in_index++] = temp[Dpos][1];
        Dpos++;
    }

    for (int i = 0; i < D->amount; i++)
        D->coef[i][0] = 0;

    for (int i = 0; i < D->amount; i++) {
        D->coef[i][1] = already_in[i];

        for (int j = 0; j < A->amount * B->amount; j++)
            if (temp[j][1] == already_in[i])
                D->coef[i][0] += temp[j][0];
    }

    for (int j = 0; j < A->amount * B->amount; j++)
        free(temp[j]);
    free(temp);
    free(already_in);
}

//���ڿ��� �Է¹��� ���׽� ������ ���� ���ڷ� ��ȯ�Ͽ� ���׽Ŀ� �����ϴ� initialize �Լ�
void poly_init(char str[], polynomial poly[]) {
    char* number = strtok(str, " ");
    int i = 0;

    //�̶� strtok�� �ι� ���ִ� ������ �������� ����Ǵ� ���� �� row�� 0���� 1�� index�� �����ϱ� ����
    while (number != NULL) {
        poly->coef[i][0] = atoi(number);
        number = strtok(NULL, " ");

        while (number != NULL) {
            poly->coef[i++][1] = atoi(number);
            number = strtok(NULL, " ");
            break;
        }
    }

    poly->amount = i;
}

//���׽��� ����ϴ� �Լ�
void poly_print(polynomial poly[]) {
    for (int i = 0; i < poly->amount; i++)
        printf("%d %d ", poly->coef[i][0], poly->coef[i][1]);
}

//���׽� f(x)�� Ư�� x ���� �־��� �� ��� ���� ��ȯ���ִ� �Լ�
int poly_get_value(polynomial poly[], int x) {
    int result = 0;
    for (int i = 0; i < poly->amount; i++) {
        result += power(x, poly->coef[i][1]) * poly->coef[i][0];
    }
    return result;
}

int main(void) {
    char str[MAX_DEGREE * 2];
    char op[] = "+*";
    int x, y;
    polynomial poly[4];

    //������ �Է¹ް� initialize ��
    for (int i = 0; i < 2; i++) {
        printf("���� %d�� �Է��ϼ��� : ", i + 1);
        gets(str);

        poly_init(str, &poly[i]);
    }

    //���׽��� ������ ���� �����ؼ� ������
    poly_add(&poly[0], &poly[1], &poly[2]);
    poly_mul(&poly[0], &poly[1], &poly[3]);

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