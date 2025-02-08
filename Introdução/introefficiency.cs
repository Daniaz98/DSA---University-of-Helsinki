
int n = 1000;
Console.WriteLine("n: " + n);

Random random = new Random(1337);
int[] numbers = new int[n];

for (int i = 0; i < n; i++)
{
    numbers[i] = random.Next(1, 1000000);  // Gera números aleatórios entre 1 e 10^6
}

var startTime = DateTime.Now;

int result = MaxDiff(numbers);

var endTime = DateTime.Now;

Console.WriteLine("result: " + result);
Console.WriteLine("time: " + (endTime - startTime).TotalSeconds + "s");


static int MaxDiff(int[] numbers)
{
  return numbers.Max() - numbers.Min();
}