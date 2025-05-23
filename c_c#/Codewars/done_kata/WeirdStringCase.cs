// https://www.codewars.com/kata/52b757663a95b11b3d00062d/csharp

using System;

public class WeirdStringCase
{
    public static string ToWeirdCase(string s)
    {
        return string.Concat(s.Split(" ").Select((l) => string.Concat(l.Select((ll, j) => j % 2 == 0 ? char.ToUpper(ll) : char.ToLower(ll))) + " ")).TrimEnd();
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(ToWeirdCase("String") + " -> StRiNg");
        Console.WriteLine(ToWeirdCase("Weird String Case") + " -> WeIrD StRiNg CaSe");
    }
}