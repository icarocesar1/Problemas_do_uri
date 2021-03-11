#include <stdio.h>
 
int main() {
 
    char nome_do_vendedor;
    double salario_fixo;
    double comissao;
    double bonus;
    double total;
    scanf("%s",&nome_do_vendedor);
    scanf("%lf",&salario_fixo);
    scanf("%lf",&comissao);
    bonus=comissao*0.15;
    total=salario_fixo+bonus;
    printf("TOTAL = R$ %.2lf\n",total);
    return 0;
   
}
