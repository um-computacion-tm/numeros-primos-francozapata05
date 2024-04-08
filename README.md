Programa de numeros primos Python

Creo una funcion is_primo que tiene como parametro la variable value
Creo tres condicionales
1) En caso de que value sea negativo => devuelve False, el numero no es primo.

2)En caso de que value sea mayor que 3, mediante un bucle for con rango, divido a value por todos los numeros enteros entre 1(sin incluirlo) y si mismo, llevando en un contador cuantas veces el resto es 0. Entonces si contador es = 1, significa que solo es divisible por si mismo (ademas del 1), es primo. Si el contador es mayor que uno, devuelve False.

3) Condicional else (value igual a 1,2,3), devuelve True, son primos.

Ing Informatica Franco Zapata
