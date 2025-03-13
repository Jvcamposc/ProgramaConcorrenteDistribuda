#include <stdio.h>


int main(){
    int n1, n2;
   printf("Digite a soma: ");
   scanf("%d + %d", &n1, &n2);

   while (n1 != 0)
   {
    n1 = n1 - 1;
    n2 = n2 + 1;
   }
   printf("Resultado: %d\n", n2);
    return 0;
}