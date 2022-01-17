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
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
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
  
  private static final String RANKING_FILE_NAME_TRADITIONAL_TEXT = "compiled/ranking-traditional.txt";
  private static final String RANKING_FILE_NAME_SIMPLIFIED_TEXT = "compiled/ranking-simplified.txt";
  private static final String RANKING_FILE_NAME_TRADITIONAL_SERIAL = "generated/ranking-traditional.ser";
  private static final String RANKING_FILE_NAME_SIMPLIFIED_SERIAL = "generated/ranking-simplified.ser";
  private static final String COMMON_FILE_NAME_TRADITIONAL_SERIAL = "generated/common-traditional.ser";
  private static final String COMMON_FILE_NAME_SIMPLIFIED_SERIAL = "generated/common-simplified.ser";
  private static final int COMMON_CHARACTER_RANK_THRESHOLD = 1400;
  
  private static final String CHARACTERS_FILE_NAME_TRADITIONAL_TEXT = "generated/characters-traditional.txt";
  private static final String CHARACTERS_FILE_NAME_SIMPLIFIED_TEXT = "generated/characters-simplified.txt";
  private static final String CHARACTERS_FILE_NAME_TRADITIONAL_SERIAL = "generated/characters-traditional.ser";
  private static final String CHARACTERS_FILE_NAME_SIMPLIFIED_SERIAL = "generated/characters-simplified.ser";
  
  private static final String SEQUENCE_CHARACTERS_FILE_NAME_TEXT = "generated/sequence-characters.txt";
  private static final String SEQUENCE_CHARACTERS_FILE_NAME_SERIAL = "generated/sequence-characters.ser";
  
  public static void main(String[] args)
  {
    serialisePhrasesData(PHRASES_FILE_NAME_TRADITIONAL_TEXT, PHRASES_FILE_NAME_TRADITIONAL_SERIAL);
    serialisePhrasesData(PHRASES_FILE_NAME_SIMPLIFIED_TEXT, PHRASES_FILE_NAME_SIMPLIFIED_SERIAL);
    
    serialiseRankingData(
      RANKING_FILE_NAME_TRADITIONAL_TEXT,
      RANKING_FILE_NAME_TRADITIONAL_SERIAL,
      COMMON_FILE_NAME_TRADITIONAL_SERIAL
    );
    serialiseRankingData(
      RANKING_FILE_NAME_SIMPLIFIED_TEXT,
      RANKING_FILE_NAME_SIMPLIFIED_SERIAL,
      COMMON_FILE_NAME_SIMPLIFIED_SERIAL
    );
    
    serialiseCharactersData(CHARACTERS_FILE_NAME_TRADITIONAL_TEXT, CHARACTERS_FILE_NAME_TRADITIONAL_SERIAL);
    serialiseCharactersData(CHARACTERS_FILE_NAME_SIMPLIFIED_TEXT, CHARACTERS_FILE_NAME_SIMPLIFIED_SERIAL);
    
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
  
  private static void serialiseRankingData(
    final String rankingFileNameText,
    final String rankingFileNameSerial,
    final String commonFileNameSerial
  )
  {
    final Map<Integer, Integer> sortingRankFromCodePoint = new HashMap<>();
    final Set<Integer> commonCodePointSet = new HashSet<>();
    
    try (final BufferedReader bufferedReader = new BufferedReader(new FileReader(rankingFileNameText)))
    {
      int currentRank = 0;
      String line;
      while ((line = bufferedReader.readLine()) != null)
      {
        if (!isCommentLine(line))
        {
          for (final int codePoint : toCodePointList(line))
          {
            currentRank++;
            if (!sortingRankFromCodePoint.containsKey(codePoint))
            {
              sortingRankFromCodePoint.put(codePoint, currentRank);
            }
            if (currentRank < COMMON_CHARACTER_RANK_THRESHOLD)
            {
              commonCodePointSet.add(codePoint);
            }
          }
        }
      }
      
      {
        final FileOutputStream fileOutputStream = new FileOutputStream(rankingFileNameSerial);
        final ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(sortingRankFromCodePoint);
        objectOutputStream.close();
      }
      
      {
        final FileOutputStream fileOutputStream = new FileOutputStream(commonFileNameSerial);
        final ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
        objectOutputStream.writeObject(commonCodePointSet);
        objectOutputStream.close();
      }
    }
    catch (IOException exception)
    {
      exception.printStackTrace();
    }
  }
  
  private static void serialiseCharactersData(
    final String charactersFileNameText,
    final String charactersFileNameSerial
  )
  {
    final Set<Integer> codePointSet = new HashSet<>();
    
    try (final BufferedReader bufferedReader = new BufferedReader(new FileReader(charactersFileNameText)))
    {
      String line;
      while ((line = bufferedReader.readLine()) != null)
      {
        if (!isCommentLine(line))
        {
          codePointSet.add(getFirstCodePoint(line));
        }
      }
      
      final FileOutputStream fileOutputStream = new FileOutputStream(charactersFileNameSerial);
      final ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
      objectOutputStream.writeObject(codePointSet);
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
  
  private static int getFirstCodePoint(final String string)
  {
    return string.codePointAt(0);
  }
  
  private static List<Integer> toCodePointList(final String string)
  {
    final List<Integer> codePointList = new ArrayList<>();
    
    final int charCount = string.length();
    for (int charIndex = 0; charIndex < charCount;)
    {
      final int codePoint = string.codePointAt(charIndex);
      codePointList.add(codePoint);
      charIndex += Character.charCount(codePoint);
    }
    
    return codePointList;
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
