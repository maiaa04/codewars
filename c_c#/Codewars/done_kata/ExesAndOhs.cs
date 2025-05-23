// https://www.codewars.com/kata/55908aad6620c066bc00002a

using System;

public class ExesAndOhs
{
    public static bool XO(string input)
    {
        if (input.ToLower().Count(x => x == 'x') == input.ToLower().Count(x => x == 'o')) return true;
        else return false;
    }
  
  static void Main_(string[] args)
  {
        Console.WriteLine(XO("xoxo"));
        Console.WriteLine(XO("xoxoo"));
        Console.WriteLine(XO("xoXo"));
  }
}