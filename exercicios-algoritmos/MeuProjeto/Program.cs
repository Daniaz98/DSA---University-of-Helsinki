// See https://aka.ms/new-console-template for more information

class Program
{
  static int SumArr(int[] array, int size) 
  {
    if (size == 0)
      return 0;
    return array[size - 1] + SumArr(array, size - 1);
  }


  static int CountArr(int[] array, int index) 
{
  if (index == array.Length)
    return 0;
  return 1 + CountArr(array, index + 1);
}

static int FindMax(int[] array, int index) 
{
  if (index == array.Length - 1)
    return array[index];

  var findRest = FindMax(array, index + 1);

  return Math.Max(array[index], findRest);

}

static int BinarySearch(int[] array, int low, int high, int target) 
{
  if (low > high)
    return -1;

  int mid = low + (high - low) / 2;

  if (array[mid] == target)
      return mid;

  if (array[mid] > target)
    return BinarySearch(array, low, mid - 1, target);

  return BinarySearch(array, low, mid + 1, target);
}

  static void Main(string[] args) 
  {
      int[] nums = {2, 4, 6, 12, 98, 20, 15};
      //int result = SumArr(nums, nums.length);
      //int countResult = CountArr(nums, 0);
      //int maxVal = FindMax(nums, 0);
      int target = 12;
      var resultBS = BinarySearch(nums, 0, nums.Length - 1, target);
      Console.WriteLine(resultBS);

  }
}
