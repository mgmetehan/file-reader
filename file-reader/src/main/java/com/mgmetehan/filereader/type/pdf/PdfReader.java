package com.mgmetehan.filereader.type.pdf;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;

public class PdfReader {

    public void readPdfFirst2Byte(String path) {
        try {
            PDDocument document = PDDocument.load(new File(path));
            if (!document.isEncrypted()) {
                PDFTextStripper stripper = new PDFTextStripper();
                String text = stripper.getText(document);
                for (int i = 0; i < 2; i++){
                    System.out.println(text.charAt(i));
                }
            }
            document.close();
        }catch (Exception e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        PdfReader pdfReader = new PdfReader();
        var path = "/Users/mgmetehan/Desktop/chomar/C-ProtStajyerproje.pdf";
        pdfReader.readPdfFirst2Byte(path);
    }
}

