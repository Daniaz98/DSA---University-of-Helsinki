//Estudo DSA em C#, parte I - Introdução
// int[] numeros = new int[] {1, 3, 4, 5, 9, 8};

// int maxNum = numeros[0];

// foreach (int num in numeros) 
// {
//   if (num > maxNum ) 
//   {
//     maxNum = num;
//   }
// }

// Console.WriteLine(maxNum);

//Complexidade O(n), pois percorre todos os elementos uma única vez

////---------------Números pares-----------------
int[] numbers = new int[] {1, 3, 5, 6, 9, 7, 12, 14, 18, 22, 23};

int result = 0;

foreach (int y in numbers ) 
{
  if (y % 2 == 0) 
  {
    Console.WriteLine(y);
  }
}

//Console.WriteLine(result);