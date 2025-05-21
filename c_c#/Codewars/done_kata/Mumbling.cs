using System;

public class Mumbling
{
    public static string Accum(string s)
    {
        string final = "";
        for (int i = 0; i < s.Length; i++)
        {
            string subs = s.Substring(i, 1).ToLower();
            string temp = String.Concat(subs.ToUpper(),String.Concat(Enumerable.Repeat(subs, i)),"-");
            final += temp;
        }
        return final[..(final.Length-1)];
    }
    
    static void Main_(string[] args)
    {
        Console.WriteLine(Accum("ZpglnRxqenU"));
    }
}