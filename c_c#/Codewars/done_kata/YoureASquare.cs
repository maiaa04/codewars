// https://www.codewars.com/kata/54c27a33fb7da0db0100040e

using System;

public class YoureASquare
{
  public static bool IsSquare(int n)
  {
    double root = Math.Sqrt(n);
    if (root == (int)root)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  
  static void Main_(string[] args)
  {
    Console.WriteLine(IsSquare(4));
    Console.WriteLine(IsSquare(3));
  }
}