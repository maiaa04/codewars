// https://www.codewars.com/kata/515decfd9dcfc23bb6000006

using System;
using System.Text.RegularExpressions;

public static class IPValidation
{
    public static bool IsValidIp(string ipAddress)
    {      
        if (ipAddress.Length > 0)
        {
            string[] array = ipAddress.Split(".");
            if (array.Length != 4 || array.ToArray().Any(s => string.IsNullOrWhiteSpace(s) || Regex.IsMatch(s, "[a-z]") || !int.Parse(s).ToString().Equals(s) || int.Parse(s) < 0 || int.Parse(s) > 255)) return false;
            else return true;
        }
        else return false;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(IsValidIp("")); // false
        Console.WriteLine(IsValidIp("a.b.c.d")); // false
        Console.WriteLine(IsValidIp("1.2.3.4")); // true
        Console.WriteLine(IsValidIp("1.02.3.4")); // false
        Console.WriteLine(IsValidIp("0.2.3.4")); // true
        Console.WriteLine(IsValidIp("0.255.3.4")); // true
        Console.WriteLine(IsValidIp("0.256.3.4")); // false
        Console.WriteLine(IsValidIp("0.253.3")); // false
    }
}