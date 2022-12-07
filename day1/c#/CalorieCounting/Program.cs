static int CalorieCount(int top)
{
    string inputPath = Path.Combine(Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName, "input.txt");

    string text = File.ReadAllText(inputPath);
    string[] splittedText = text.Split("\r\n\r\n");
    IEnumerable<string[]> splittedArrays = splittedText.Select(s => s.Split("\r\n"));
    IEnumerable<int> summedArrays = splittedArrays.Select((d) => d.Select(int.Parse).Sum());
    IEnumerable<int> orderedArrays = summedArrays.OrderByDescending(num => num);

    return orderedArrays.Take(top).Sum();
}

Console.WriteLine(CalorieCount(3));