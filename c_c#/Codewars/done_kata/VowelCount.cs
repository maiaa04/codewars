// https://www.codewars.com/kata/54ff3102c1bad923760001f3

using System;
using System.Text.RegularExpressions;

public class VowelCount
{
    public static int GetVowelCount(string str)
    {
        string pattern = "[aeiou]";
        int vowelCount = 0;
        Regex rg = new Regex(pattern);

        for (int i = 0; i < str.Length; i++)
        {
            if (rg.IsMatch(str.Substring(i,1)))
            {
                vowelCount++;
            }
        }

        return vowelCount;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(GetVowelCount("aeiou"));
    }
}