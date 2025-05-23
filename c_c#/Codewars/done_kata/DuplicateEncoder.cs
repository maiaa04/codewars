// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

using System;

public class DuplicateEncoder
{
    public static string DuplicateEncode(string word)
    {
        string final = "";
        List<char> letters = [.. word.ToLower()];
        Dictionary<char, int> letter_count = new Dictionary<char, int>();
        foreach (char l in letters) if (!letter_count.TryAdd(l, 1)) letter_count[l] += 1;
        foreach (char c in letters)
        {
            if (letter_count[c] == 1) final += "(";
            else final += ")";
        }
        return final;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(DuplicateEncode("din"));
        Console.WriteLine(DuplicateEncode("recede"));
    }
}