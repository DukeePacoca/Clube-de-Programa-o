#include <stdio.h>
#include <stdlib.h>

int soma (){
    
    int numero1, numero2;
    
    numero1 = 10;
    numero2 = 20;
    
    int resultado = numero1 + numero2;
    printf("A soma é %d",resultado );
    
    
}

int contador(){
    int indice = 0;
    
    while (indice <=10){
        printf("%d \n", indice);
        indice += 1;
        
        
    } // fecha o while
    
    
    
} // fecha o contador




int main(){
    contador();
   //chamamos a soma para aparecer 
    
    
  
    
    return 0; 
}

/*
%d = inteiros (1,2,3,4,5...) + importante
%f = reais (Exemplo: 3,1415...) + importante
%c = letra 
%s = texto
return 0 = parar
\n = coloca na linha de baixo
sempre começar com: #include <stdio.h> e #include <stdlib.h>
int = o que retorna para iniciar 
float = vai retornar um número decimal
char = retorna com letra
void = não precisa de return para parar
*/
