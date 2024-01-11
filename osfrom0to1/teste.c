#include <stdint.h>

struct bit_field {
	int data1:8;
	/* int data2:8; */
	/* int data3:8; */
	/* int data4:8; */
}; //__attribute__((packed));

struct bit_field2 {
	int data1:8;
	/* int data2:8; */
	/* int data3:8; */
	/* int data4:8; */
	/* char data5:4; */
	int data5:32;
};

struct normal_struct {
	int data1;
	int data2;
	int data3;
	int data4;
};

struct normal_struct ns = {
	.data1 = 0x12345678,
	.data2 = 0x9abcdef0,
	.data3 = 0x12345678,
	.data4 = 0x9abcdef0,
};

int i = 0x12345678;
struct bit_field bf = {
	.data1 = 0x1234,
	/* .data2 = 0x34, */
	/* .data3 = 0x56, */
	/* .data4 = 0x78 */
};
struct bit_field2 bf2 = {
	.data1 = 0x1234,
	/* .data2 = 0x34, */
	/* .data3 = 0x56, */
	/* .data4 = 0x78, */
	.data5 = 0x12345678
};

int main(int argc, char *argv[]) {
	char a = bf2.data1;
	int b = bf2.data5;

	int c = i;
	return 0;

}

