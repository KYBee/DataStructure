#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#pragma warning (disable: 4996)

#define MAX_DEGREE 11
#define MAX(a, b) (((a) >= (b)) ? (a) : (b))
#define MIN(a, b) (((a) <= (b)) ? (a) : (b))

typedef struct {
	int degree;
	int coef[MAX_DEGREE];
} polynomial;

int power(int x, int y) {
	if (y == 0) return 1;
	return x * power(x, y - 1);
}

polynomial poly_add(polynomial * A, polynomial * B) {
	polynomial C;

	int degree_diff = MAX(A->degree, B->degree) - MIN(A->degree, B->degree);	
	C.degree = MAX(A->degree, B->degree);

	if (A->degree > B->degree) {
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

polynomial poly_mul(polynomial * A, polynomial * B) {
	polynomial D;
	D.degree = A->degree + B->degree;

	for (int i = 0; i <= D.degree; i++)
		D.coef[i] = 0;

	for (int i = 0; i <= A->degree; i++)
		for (int j = 0; j <= B->degree; j++) {
			D.coef[i + j] += A->coef[i] * B->coef[j];
		}
	return D;
}

void poly_init(char str[], polynomial poly[]) {
	char* number = strtok(str, " ");
	int i = 0;

	while (number != NULL) {
		poly->coef[i++] = atoi(number);
		number = strtok(NULL, " ");
	}
	poly->degree = i - 1;
}

void poly_print(polynomial poly[]) {
	for (int i = 0; i <= poly->degree; i++) {
		printf("%d ", poly->coef[i]);
	}
}

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
	polynomial poly[4] = {0};

	for (int i = 0; i < 2; i++) {
		printf("수식 %d을 입력하세요 : ", i + 1);
		gets(str);
		poly_init(str, &poly[i]);
	}

	poly[2] = poly_add(&poly[0], &poly[1]);
	poly[3] = poly_mul(&poly[0], &poly[1]);

	for (int i = 2; i < 4; i++) {
		printf("수식 1 %c 2 는 ", op[i % 2]);
		poly_print(&poly[i]);
		printf("\n");
	}

	while (1) {
		printf("수식에 값을 넣으세요 ");
		scanf("%d %d", &y ,&x);
		printf("결과값은 %d\n", poly_get_value(&poly[y - 1], x));
	}

	return 0;
}