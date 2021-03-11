#include <stdio.h>
 
int main() {
 
    int numero_funcionario;
    int horas_trabalhadas;
    double valor_hora;
    double salario;
    scanf("%i",&numero_funcionario);
    scanf("%i",&horas_trabalhadas);
    scanf("%lf",&valor_hora);
    salario=horas_trabalhadas*valor_hora;
    printf("NUMBER = %i\n",numero_funcionario);
    printf("SALARY = U$ %.2lf\n",salario);

 
    return 0;
}
