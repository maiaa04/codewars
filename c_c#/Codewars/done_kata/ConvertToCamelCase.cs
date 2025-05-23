using System;
using System.Collections.Generic;

public class ConvertToCamelCase
{
    public static string ToCamelCase(string str)
    {
        string[] array = str.Split(['-', '_']);
        string output = array[0];
        for (int i = 1; i < array.Length; i++) output += char.ToUpper(array[i][0]) + array[i][1..];
        return output;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(ToCamelCase("the-stealth-warrior"));
        Console.WriteLine(ToCamelCase("The-stealth-warrior"));
        Console.WriteLine(ToCamelCase("The_stealth-warrior"));
    }
}