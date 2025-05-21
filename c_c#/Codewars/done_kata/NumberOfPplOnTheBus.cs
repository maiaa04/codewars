using System;
using System.Collections.Generic;

public class NumberOfPplOnTheBus
{
    public static int Number(List<int[]> peopleListInOut)
    {
        int people = 0;
        for (int i = 0; i < peopleListInOut.Count; i++)
        {
            people += peopleListInOut[i][0] - peopleListInOut[i][1];
        }
        return people;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(Number(new List<int[]>() { new[] { 10, 0 }, new[] { 3, 5 }, new[] { 5, 8 } }));
    }
}