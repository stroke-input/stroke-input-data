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
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class MakeSer
{
  private static final String PHRASES_FILE_NAME_TRADITIONAL_TEXT = "compiled/phrases-traditional.txt";
  private static final String PHRASES_FILE_NAME_SIMPLIFIED_TEXT = "compiled/phrases-simplified.txt";
  private static final String PHRASES_FILE_NAME_TRADITIONAL_SERIAL = "generated/phrases-traditional.ser";
  private static final String PHRASES_FILE_NAME_SIMPLIFIED_SERIAL = "generated/phrases-simplified.ser";
  
  private static final String SEQUENCE_CHARACTERS_FILE_NAME_TEXT = "generated/sequence-characters.txt";
  private static final String SEQUENCE_CHARACTERS_FILE_NAME_SERIAL = "generated/sequence-characters.ser";
  
  public static void main(String[] args)
  {
    serialisePhrasesData(PHRASES_FILE_NAME_TRADITIONAL_TEXT, PHRASES_FILE_NAME_TRADITIONAL_SERIAL);
    serialisePhrasesData(PHRASES_FILE_NAME_SIMPLIFIED_TEXT, PHRASES_FILE_NAME_SIMPLIFIED_SERIAL);
    serialiseSequenceCharactersData(SEQUENCE_CHARACTERS_FILE_NAME_TEXT, SEQUENCE_CHARACTERS_FILE_NAME_SERIAL);
  }
  
  private static void serialisePhrasesData(final String phrasesFileNameText, final String phrasesFileNameSerial)
  {
    final Set<String> phraseSet = new TreeSet<>();
    
    try (final BufferedReader bufferedReader = new BufferedReader(new FileReader(phrasesFileNameText)))
    {
      String line;
      while ((line = bufferedReader.readLine()) != null)
      {
        if (!isCommentLine(line))
        {
          phraseSet.add(line);
        }
      }
      
      final FileOutputStream fileOutputStream = new FileOutputStream(phrasesFileNameSerial);
      final ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
      objectOutputStream.writeObject(phraseSet);
      objectOutputStream.close();
    }
    catch (IOException exception)
    {
      exception.printStackTrace();
    }
  }
  
  private static void serialiseSequenceCharactersData(
    final String sequenceCharactersFileNameText,
    final String sequenceCharactersFileNameSerial
  )
  {
    final Map<String, String> charactersFromStrokeDigitSequence = new TreeMap<>();
    
    try (final BufferedReader bufferedReader = new BufferedReader(new FileReader(sequenceCharactersFileNameText)))
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
      
      final FileOutputStream fileOutputStream = new FileOutputStream(sequenceCharactersFileNameSerial);
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
