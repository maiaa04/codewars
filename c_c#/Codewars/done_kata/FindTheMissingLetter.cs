// https://www.codewars.com/kata/5839edaa6754d6fec10000a2

using System;
using System.Runtime.CompilerServices;

public class FindTheMissingLetter
{
    public static char FindMissingLetter(char[] array)
    {
        char[] alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
        if (Char.IsUpper(array[0])) for (int i = 0; i < alphabet.Length; i++) alphabet[i] = Char.ToUpper(alphabet[i]);
        char[] subArray = new char[array.Length+1];
        Array.Copy(alphabet, Array.IndexOf(alphabet, array[0]), subArray, 0, array.Length+1);
        char res = ' ';
        foreach (char c in subArray) if (!Array.Exists(array, element => element.Equals(c))) res = c;
        return res;
    }

    static void Main_(string[] args)
    {
        Console.WriteLine(FindMissingLetter(['a', 'b', 'c', 'd', 'f']));
    }
  
}