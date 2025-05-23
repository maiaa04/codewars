//  https://www.codewars.com/kata/541c8630095125aba6000c00/csharp

using System;

public static class SumOfDigitsDigitalRoot
{
    public static int DigitalRoot(long n)
    {
        while (n.ToString().Length != 1)
        {
            int[] array = [.. n.ToString().Select(i => int.Parse(i.ToString()))];
            n = 0;
            foreach (int i in array) n += i;
        }
        return (int)n;
    }
    
    static void Main_(string[] args)
    {
        Console.WriteLine(DigitalRoot(16));
        Console.WriteLine(DigitalRoot(942));
        Console.WriteLine(DigitalRoot(132189));
        Console.WriteLine(DigitalRoot(493193));
    }
}