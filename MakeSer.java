/*
  # MakeSer.java
  
  Parse the files
  
  - `compiled/phrases-traditional.txt`
    `compiled/phrases-simplified.txt`
  
  - `compiled/ranking-traditional.txt`
    `compiled/ranking-simplified.txt`
  
  - `generated/characters-traditional.txt`
    `generated/characters-simplified.txt`
  
  - `generated/sequence-characters.txt`
  
  generating the serial files in `generated/`.
  (Assumes `make_txt.py` has already been run.)
  
  Licensed under "MIT No Attribution" (MIT-0),
  see <https://spdx.org/licenses/MIT-0>.
*/

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.Map;
import java.util.TreeMap;

public class MakeSer
{
  private static final String TEXT_FILE_EXTENSION = ".txt";
  private static final String SERIAL_FILE_EXTENSION = ".ser";
  private static final String SEQUENCE_CHARACTERS_BASE_NAME = "generated/sequence-characters";
  
  public static void main(String[] args)
  {
    serialiseSequenceCharactersData(SEQUENCE_CHARACTERS_BASE_NAME);
  }
  
  private static void serialiseSequenceCharactersData(final String sequenceCharactersBaseName)
  {
    final Map<String, String> charactersFromStrokeDigitSequence = new TreeMap<>();
    
    try (BufferedReader bufferedReader = new BufferedReader(new FileReader(sequenceCharactersBaseName + TEXT_FILE_EXTENSION)))
    {
      String line;
      while ((line = bufferedReader.readLine()) != null)
      {
        if (!isCommentLine(line))
        {
          final String[] sunderedLineArray = sunder(line, "\t");
          final String strokeDigitSequence = sunderedLineArray[0];
          final String characters = sunderedLineArray[1];
          charactersFromStrokeDigitSequence.put(strokeDigitSequence, characters);
        }
      }
      
      final FileOutputStream fileOutputStream =
              new FileOutputStream(sequenceCharactersBaseName + SERIAL_FILE_EXTENSION);
      final ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
      objectOutputStream.writeObject(charactersFromStrokeDigitSequence);
      objectOutputStream.close();
    }
    catch (IOException exception)
    {
      exception.printStackTrace();
    }
  }
  
  private static boolean isCommentLine(final String line)
  {
    return line.startsWith("#") || line.length() == 0;
  }
  
  private static String[] sunder(final String string, final String delimiter)
  {
    final int delimiterIndex = string.indexOf(delimiter);
    final int delimiterLength = delimiter.length();
    
    final String substringBeforeDelimiter;
    final String substringAfterDelimiter;
    
    if (delimiterIndex < 0)
    {
      substringBeforeDelimiter = string;
      substringAfterDelimiter = "";
    }
    else
    {
      substringBeforeDelimiter = string.substring(0, delimiterIndex);
      substringAfterDelimiter = string.substring(delimiterIndex + delimiterLength);
    }
    
    return new String[]{substringBeforeDelimiter, substringAfterDelimiter};
  }
}
