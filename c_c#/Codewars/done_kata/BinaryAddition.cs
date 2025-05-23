// https://www.codewars.com/kata/551f37452ff852b7bd000139

using System;
using System.Linq;

public static class BinaryAddition
{
    public static string AddBinary(int a, int b)
    {
        double dec = a + b;
        string bin = "";
        while (dec != 0)
        {
            int rem = (int) dec % 2;
            dec = Math.Floor(dec / 2);
            bin = bin.Insert(0, rem.ToString());
        }
        return bin;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(AddBinary(1, 2));
        Console.WriteLine(AddBinary(5, 9));
    }
}