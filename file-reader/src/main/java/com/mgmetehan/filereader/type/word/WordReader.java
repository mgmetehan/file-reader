package com.mgmetehan.filereader.type.word;

import com.mgmetehan.filereader.shared.util.PunctuationUtil;
import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.apache.poi.xwpf.usermodel.XWPFParagraph;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class WordReader {
    public void readWordFirst2Byte(String path) {
        String result = "";

        try {
            XWPFDocument doc = new XWPFDocument(Files.newInputStream(Paths.get(path)));
            List<XWPFParagraph> list = doc.getParagraphs();
            var x = list.get(0).getParagraphText();
            for (int i = 0; i < 2; i++) {
                System.out.println(x.charAt(i));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void readWordFindWord(String path, String findWord) {
        String result = "";
        String[] splitWords;
        Boolean check;
        String splitWordNoPunctuation;
        int offset = 0;
        try {
            for (int j = 0; j < 200; j++) {
                XWPFDocument doc = new XWPFDocument(Files.newInputStream(Paths.get(path)));
                List<XWPFParagraph> list = doc.getParagraphs();
                for (XWPFParagraph paragraph : list) {
                    result = paragraph.getText();
                    splitWords = result.split("\\s+");
                    for (int i = 0; i < splitWords.length; i++) {
                        if (splitWords[i] == null) {
                            continue;
                        }
                        splitWordNoPunctuation = PunctuationUtil.noPunctuation(splitWords[i]);
                        offset += splitWordNoPunctuation.length();
                        check = splitWordNoPunctuation.equals(findWord);
                        if (check) {
                            System.out.println(findWord + " " + offset);
                        }
                    }
                }
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public static void main(String[] args) {
        WordReader wordReader = new WordReader();
        var path = "/Users/mgmetehan/Desktop/chomar/deneme.docx";
        //wordReader.readWordFirst2Byte(path);
        wordReader.readWordFindWord(path, "deneme");
    }
}
