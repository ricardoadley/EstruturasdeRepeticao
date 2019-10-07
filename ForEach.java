public class ForEach {

    public static void main(String[] args){
        int[] numeros = {1,4,6,8,9,1,3,6,7,4,53,6,7};
        int soma = 0;
        for (int numero : numeros) {
            soma += numero;
        }
        System.out.println(soma);
    }
}
