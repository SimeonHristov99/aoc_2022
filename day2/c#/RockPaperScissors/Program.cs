string inputPath = Path.Combine(Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName, "input.txt");

var text = File.ReadAllLines(inputPath);

var outcomes1 = new Dictionary<string, int>()
{
    { "A X", 4},
    { "A Y", 8},
    { "A Z", 3},
    { "B X", 1},
    { "B Y", 5},
    { "B Z", 9},
    { "C X", 7},
    { "C Y", 2},
    { "C Z", 6}
};

var outcomes2 = new Dictionary<string, int>()
{
    { "A X", 3},
    { "A Y", 4},
    { "A Z", 8},
    { "B X", 1},
    { "B Y", 5},
    { "B Z", 9},
    { "C X", 2},
    { "C Y", 6},
    { "C Z", 7}
};

int RockPaperScissors(Dictionary<string, int> outcomes)
{

    return text.Select(line => outcomes[line]).Sum();
}

Console.WriteLine(RockPaperScissors(outcomes1));
Console.WriteLine(RockPaperScissors(outcomes2));
