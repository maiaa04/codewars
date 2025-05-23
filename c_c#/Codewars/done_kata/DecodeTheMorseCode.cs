// https://www.codewars.com/kata/54b724efac3d5402db00065e

using System;
using System.Globalization;

public class DecodeTheMorseCode
{
    public static char MorseCode(string morse)
    {
        Dictionary<char, String> morse_dict = new Dictionary<char, String>()
            {
                {'A' , ".-"},
                {'B' , "-..."},
                {'C' , "-.-."},
                {'D' , "-.."},
                {'E' , "."},
                {'F' , "..-."},
                {'G' , "--."},
                {'H' , "...."},
                {'I' , ".."},
                {'J' , ".---"},
                {'K' , "-.-"},
                {'L' , ".-.."},
                {'M' , "--"},
                {'N' , "-."},
                {'O' , "---"},
                {'P' , ".--."},
                {'Q' , "--.-"},
                {'R' , ".-."},
                {'S' , "..."},
                {'T' , "-"},
                {'U' , "..-"},
                {'V' , "...-"},
                {'W' , ".--"},
                {'X' , "-..-"},
                {'Y' , "-.--"},
                {'Z' , "--.."},
                {'0' , "-----"},
                {'1' , ".----"},
                {'2' , "..---"},
                {'3' , "...--"},
                {'4' , "....-"},
                {'5' , "....."},
                {'6' , "-...."},
                {'7' , "--..."},
                {'8' , "---.."},
                {'9' , "----."},
            };
        return morse_dict.FirstOrDefault(x => x.Value == morse).Key;
    }
    public static string Decode(string morseCode)
    {
        string result = "";
        string[] morse_words = morseCode.Split("   ");
        string[][] morse_letters = new string[morse_words.Length][];
        for (int i = 0; i < morse_words.Length; i++)
        {
            morse_letters[i] = morse_words[i].Split(" ");
            foreach (string j in morse_letters[i])
            {
                result += MorseCode(j).ToString();
            }
            result += " ";
        }
        return result.TrimEnd();
    }
    
    static void Main_(string[] args)
    {
        Console.WriteLine(Decode(".... . -.--   .--- ..- -.. ."));
    }
}