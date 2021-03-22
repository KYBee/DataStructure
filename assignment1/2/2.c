#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#pragma warning (disable: 4996)

void add_normal(int** A, int** B, int matrix_space) {
	int** C;

	C = (int**)malloc(sizeof(int) * matrix_space);
	for (int i = 0; i < matrix_space; i++)
		C[i] = (int*)malloc(sizeof(int) * matrix_space);

	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			C[i][j] = A[i][j] + B[i][j];
		}
	}

	printf("행렬1+2(%d)\n", matrix_space * matrix_space);
	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			printf("%d ", C[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	for (int j = 0; j < matrix_space; j++)
		free(C[j]);
	free(C);
}

void multiply_normal(int** A, int** B, int matrix_space) {
	int** D;

	D= (int**)malloc(sizeof(int) * matrix_space);
	for (int i = 0; i < matrix_space; i++)
		D[i] = (int*)malloc(sizeof(int) * matrix_space);

	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			D[i][j] = 0;
			for (int k = 0; k < matrix_space; k++)
				D[i][j] = D[i][j] + A[i][k] * B[k][j];
		}
	}

	printf("행렬1*2(%d)\n", matrix_space * matrix_space);
	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			printf("%d ", D[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	for (int j = 0; j < matrix_space; j++)
		free(D[j]);
	free(D);
}

void add_sparse(void);

void multiply_sparse(void);

int main(void) {

	int matrix_space;
	int** matrix_normal[2];
	char* str;
	char* number;
	int* temp;
	int temp_index = 0;


	printf("행렬의 규격을 입력하세요. ");
	scanf("%d", &matrix_space);
	getchar();

	for (int i = 0; i < 2; i++) {
		matrix_normal[i] = (int**)malloc(sizeof(int) * matrix_space);
		for (int j = 0; j < matrix_space; j++)
			matrix_normal[i][j] = (int*)malloc(sizeof(int) * matrix_space);
	}
	str = (char*)malloc(matrix_space * matrix_space * 2 + 1);
	temp = (int*)malloc(sizeof(int) * matrix_space * matrix_space);


	for (int i = 0; i < 2; i++) {
		printf("행렬 %d의 데이터를 입력하세요. ", i % 2 + 1);
		gets(str);

		temp_index = 0;
		number = strtok(str, " ");
		while (number != NULL) {
			temp[temp_index++] = atoi(number);
			number = strtok(NULL, " ");
		}

		temp_index = 0;
		for (int j = 0; j < matrix_space; j++) {
			for (int k = 0; k < matrix_space; k++) {
				matrix_normal[i][j][k] = temp[temp_index++];
			}
		}
	}

	free(str);
	free(temp);

	for (int i = 0; i < 2; i++) {
		printf("행렬%d(%d)\n", i % 2 + 1, matrix_space * matrix_space);
		for (int j = 0; j < matrix_space; j++) {
			for (int k = 0; k < matrix_space; k++)
				printf("%d ", matrix_normal[i][j][k]);

			printf("\n");
		}
		printf("\n");
	}

	add_normal(matrix_normal[0], matrix_normal[1], matrix_space);
	multiply_normal(matrix_normal[0], matrix_normal[1], matrix_space);


	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < matrix_space; j++)
			free(matrix_normal[i][j]);
		free(matrix_normal[i]);
	}

	return 0;
}