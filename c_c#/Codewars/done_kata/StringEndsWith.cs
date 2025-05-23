// https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d

using System;
using System.Text.RegularExpressions;

public class StringEdndsWith
{
    public static bool Solution(string str, string ending)
    {
        // string pattern = $".?{ending}$";
        // Regex rg = new Regex(pattern);
        // if (rg.IsMatch(str)) return true;
        // else return false;

        if (str.Length >= ending.Length && str.Substring(str.Length - ending.Length) == ending) return true;
        else return false;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(Solution("samurai", "ai"));
        Console.WriteLine(Solution("abc", "abcd"));
        Console.WriteLine(Solution(":-)", ":-("));
    }
}