#include <stdio.h>
int getSum(int a, int b){
	//Environment: goormIDE
	//You must maske (a & b) part with `& 0xffffffff` in other environment.
	//Shifting (1 << 31) << 1 is undefined behavier. You may get runtime error in some compilor. 
	return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
}
int main(){
	printf("%d", getSum(1, -1));
}
