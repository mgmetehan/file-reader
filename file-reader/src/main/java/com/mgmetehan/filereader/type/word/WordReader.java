package com.mgmetehan.filereader.type.word;

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

    public static void main(String[] args) {
        WordReader wordReader = new WordReader();
        var path = "/Users/mgmetehan/Desktop/chomar/deneme.docx";
        wordReader.readWordFirst2Byte(path);
    }
}
