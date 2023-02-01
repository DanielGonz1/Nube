#include<stdio.h>

void convbin(int de);

main(){
	int de;
	printf("Ingrese un numero del 0-15: ");
	scanf("%d", &de);
	convbin(de);
}

void convbin(int de){
	if(de >= 0 && de <=15){
		switch(de){
			case 0: printf("Decimal: %d -- Binario: 0000", de); break;
			case 1: printf("Decimal: %d -- Binario: 0001", de); break;
			case 2: printf("Decimal: %d -- Binario: 0010", de); break;
			case 3: printf("Decimal: %d -- Binario: 0011", de); break;
			case 4: printf("Decimal: %d -- Binario: 0100", de); break;
			case 5: printf("Decimal: %d -- Binario: 0101", de); break;
			case 6: printf("Decimal: %d -- Binario: 0110", de); break;
			case 7: printf("Decimal: %d -- Binario: 0111", de); break;
			case 8: printf("Decimal: %d -- Binario: 1000", de); break;
			case 9: printf("Decimal: %d -- Binario: 1001", de); break;
			case 10: printf("Decimal: %d -- Binario: 1010", de); break;
			case 11: printf("Decimal: %d -- Binario: 1011", de); break;
			case 12: printf("Decimal: %d -- Binario: 1100", de); break;
			case 13: printf("Decimal: %d -- Binario: 1101", de); break;
			case 14: printf("Decimal: %d -- Binario: 1110", de); break;
			case 15: printf("Decimal: %d -- Binario: 1111", de); break;
			default: printf("");
		}
	}
	else
		printf("El numero debe estar entre el 0 al 15");
}
