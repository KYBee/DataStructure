#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable: 4996)

//두 normal 행렬을 더하는 함수
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

//두 normal 행렬을 곱하는 함수
void multiply_normal(int** A, int** B, int matrix_space) {
	int** D;

	D= (int**)malloc(sizeof(int) * matrix_space);
	for (int i = 0; i < matrix_space; i++)
		D[i] = (int*)malloc(sizeof(int) * matrix_space);

	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			D[i][j] = 0;
			for (int k = 0; k < matrix_space; k++)
				D[i][j] += A[i][k] * B[k][j];
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

//희소 행렬 덧셈
void add_sparse(int** A, int** B, int A_size, int B_size) {
	int** C;
	int malloc_size = A_size + B_size;
	int C_pos = 0;
	int A_pos = 0;
	int B_pos = 0;

	C = (int**)malloc(sizeof(int) * malloc_size);
	for (int i = 0; i < malloc_size; i++)
		C[i] = (int*)malloc(sizeof(int) * 3);

	for (int i = 0; i < malloc_size; i++) 
		for (int j = 0; j < 3; j++)
			C[i][j] = 0;

	// adding algorithm
	while (A_pos < A_size && B_pos < B_size){
		if (A[A_pos][0] < B[B_pos][0]) {
			C[C_pos][0] = A[A_pos][0];
			C[C_pos][1] = A[A_pos][1];
			C[C_pos++][2] += A[A_pos++][2];
		}
		else if (A[A_pos][0] > B[B_pos][0]) {
			C[C_pos][0] = B[B_pos][0];
			C[C_pos][1] = B[B_pos][1];
			C[C_pos++][2] += B[B_pos++][2];
		}
		else {
			if (A[A_pos][1] < B[B_pos][1]) {
				C[C_pos][0] = A[A_pos][0];
				C[C_pos][1] = A[A_pos][1];
				C[C_pos++][2] += A[A_pos++][2];
			}
			else if (A[A_pos][1] > B[B_pos][1]) {
				C[C_pos][0] = B[B_pos][0];
				C[C_pos][1] = B[B_pos][1];
				C[C_pos++][2] += B[B_pos++][2];
			}
			else {
				C[C_pos][0] = A[A_pos][0];
				C[C_pos][1] = A[A_pos][1];
				C[C_pos++][2] += A[A_pos++][2] + B[B_pos++][2];
			}
		}
	}

	if (A_pos < A_size) {
		for (int i = 0; i < A_size - A_pos; i++) {
			C[C_pos][0] = A[A_pos][0];
			C[C_pos][1] = A[A_pos][1];
			C[C_pos++][2] += A[A_pos++][2];
		}
	}
	else if (B_pos < B_size) {
		for (int i = 0; i < B_size - B_pos; i++) {
			C[C_pos][0] = B[B_pos][0];
			C[C_pos][1] = B[B_pos][1];
			C[C_pos++][2] += B[B_pos++][2];
		}
	}

	printf("행렬3+4(%d)\n", C_pos * 3);
	for (int i = 0; i < C_pos; i++) {
		for (int j = 0; j < 3; j++) {
			printf("%d ", C[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	for (int j = 0; j < malloc_size; j++)
		free(C[j]);
	free(C);
}

//희소 행렬 곱셈
void multiply_sparse(int** A, int** B, int A_size, int B_size, int matrix_space) {
	int** D;
	int malloc_size = matrix_space * matrix_space;
	int D_pos = 0;
	int A_pos = 0;
	int B_pos = 0;
	int result = 0;

	D = (int**)malloc(sizeof(int) * malloc_size);
	for (int i = 0; i < malloc_size; i++)
		D[i] = (int*)malloc(sizeof(int) * 3);

	for (int i = 0; i < malloc_size; i++)
		for (int j = 0; j < 3; j++)
			D[i][j] = 0;

	//multiply algorithm
	for (int i = 0; i < matrix_space; i++) {
		for (int j = 0; j < matrix_space; j++) {
			result = 0;
			A_pos = 0;
			while (A_pos < A_size) {
				B_pos = 0;
				while (B_pos < B_size) {
					if (A[A_pos][0] == i && B[B_pos][1] == j){
						if (A[A_pos][1] == B[B_pos][0])
							result += A[A_pos][2] * B[B_pos][2];
					}
					B_pos++;
				}
				A_pos++;
			}
			if (result) {
				D[D_pos][0] = i;
				D[D_pos][1] = j;
				D[D_pos++][2] = result;
			}
		}
	}

	printf("행렬3*4(%d)\n", D_pos * 3);
	for (int i = 0; i < D_pos; i++) {
		for (int j = 0; j < 3; j++) {
			printf("%d ", D[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	for (int j = 0; j < malloc_size; j++)
		free(D[j]);
	free(D);
}

int main(void) {

	int matrix_space;
	int** matrix_normal[2];
	int** matrix_sparse[2];
	int matrix_sparse_index[2] = { 0 };

	char* str;
	char* number;
	int* temp;
	int temp_index = 0;

	//2이상 9이하 범위 외의 숫자 입력 시 예외 처리
	while (1) {
		printf("행렬의 규격을 입력하세요. ");
		scanf("%d", &matrix_space);
		getchar();

		if (matrix_space < 2 || matrix_space > 9)
			printf("2이상 9이하의 숫자를 입력하세요\n");
		else
			break;
	}

	//matrix normal malloc
	for (int i = 0; i < 2; i++) {
		matrix_normal[i] = (int**)malloc(sizeof(int) * matrix_space);
		for (int j = 0; j < matrix_space; j++)
			matrix_normal[i][j] = (int*)malloc(sizeof(int) * matrix_space);
	}
	//matrix sparse malloc
	for (int i = 0; i < 2; i++) {
		matrix_sparse[i] = (int**)malloc(sizeof(int) * (matrix_space * matrix_space));
		for (int j = 0; j < matrix_space * matrix_space; j++)
			matrix_sparse[i][j] = (int*)malloc(sizeof(int) * 3);
	}

	//str에 사용자로부터 입력 받은 string 을 받고, 
	str = (char*)malloc(matrix_space * matrix_space * 2 + 1);
	temp = (int*)malloc(sizeof(int) * (matrix_space * matrix_space));


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

		temp_index = 0;
		while (temp_index < matrix_space * matrix_space) {
			if (temp[temp_index] != 0) {
				matrix_sparse[i][matrix_sparse_index[i]][0] = temp_index / matrix_space;
				matrix_sparse[i][matrix_sparse_index[i]][1] = temp_index % matrix_space;
				matrix_sparse[i][matrix_sparse_index[i]][2] = temp[temp_index];
				matrix_sparse_index[i] += 1;
			}
			temp_index++;
		}

	}

	for (int i = 0; i < 2; i++)
		printf("%d\n", matrix_sparse_index[i]);


	free(str);
	free(temp);

	//matrix normal print
	printf("방식 1\n\n");
	for (int i = 0; i < 2; i++) {
		printf("행렬%d(%d)\n", i % 2 + 1, matrix_space * matrix_space);
		for (int j = 0; j < matrix_space; j++) {
			for (int k = 0; k < matrix_space; k++)
				printf("%d ", matrix_normal[i][j][k]);
			printf("\n");
		}
		printf("\n");
	}

	//matrix normal computation
	add_normal(matrix_normal[0], matrix_normal[1], matrix_space);
	multiply_normal(matrix_normal[0], matrix_normal[1], matrix_space);
	printf("\n");


	//matrix sparse print
	printf("방식 2\n\n");
	for (int i = 0; i < 2; i++) {
		printf("행렬%d(%d)\n", i % 2 + 3, 3 * matrix_sparse_index[i]);
		for (int j = 0; j < matrix_sparse_index[i]; j++) {
			for (int k = 0; k < 3; k++)
				printf("%d ", matrix_sparse[i][j][k]);
			printf("\n");
		}
		printf("\n");
	}

	//matrix sparse computation
	add_sparse(matrix_sparse[0], matrix_sparse[1], matrix_sparse_index[0], matrix_sparse_index[1]);
	multiply_sparse(matrix_sparse[0], matrix_sparse[1], matrix_sparse_index[0], matrix_sparse_index[1], matrix_space);


	//matrix normal free
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < matrix_space; j++)
			free(matrix_normal[i][j]);
		free(matrix_normal[i]);
	}

	//matrix sparse freee
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < matrix_space * matrix_space; j++)
			free(matrix_sparse[i][j]);
		free(matrix_sparse[i]);
	}

	return 0;
}