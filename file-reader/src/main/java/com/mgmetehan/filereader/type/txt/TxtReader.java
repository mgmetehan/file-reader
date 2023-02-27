package com.mgmetehan.filereader.type.txt;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class TxtReader {

    public void readTxtword(String path) {
        BufferedReader bufferedReader = null;
        try {
            bufferedReader = new BufferedReader(new FileReader(path));
            StringBuilder stringBuilder = new StringBuilder();
            String line = bufferedReader.readLine();
            String[] splited;

            while (line != null) {
                stringBuilder.append(line);
                stringBuilder.append(System.lineSeparator());
                line = bufferedReader.readLine();
            }
            String everything = stringBuilder.toString();
            splited = everything.split("\\s+");
            for (String word : splited) {
                System.out.println(word);
            }
            //System.out.println(everything);
            bufferedReader.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void readTxtFirst2Byte(String path) {
        BufferedReader bufferedReader = null;
        try {
            bufferedReader = new BufferedReader(new FileReader(path));
            StringBuilder stringBuilder = new StringBuilder();
            String line = bufferedReader.readLine();
            String[] splited;

            while (line != null) {
                stringBuilder.append(line);
                stringBuilder.append(System.lineSeparator());
                line = bufferedReader.readLine();
            }
            String everything = stringBuilder.toString();

            for (int i = 0; i < 2; i++) {
                System.out.println(everything.charAt(i));
            }

            bufferedReader.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        var path = "/Users/mgmetehan/Desktop/chomar/c-port.txt";
        TxtReader txtReader = new TxtReader();
        txtReader.readTxtFirst2Byte(path);
    }
}
