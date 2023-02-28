package com.mgmetehan.filereader.shared.util;

import lombok.experimental.UtilityClass;

import java.util.ArrayList;

@UtilityClass
public class PunctuationUtil {
    public String noPunctuation(String word) {
        ArrayList arr = new ArrayList();
        arr.add(".");
        arr.add(",");
        arr.add(":");
        arr.add(";");
        arr.add("?");
        arr.add("!");
        arr.add("-");
        arr.add("\u201c");
        arr.add("\u201d");
        arr.add("\u2018");
        arr.add("\u2019");
        arr.add("\"");
        arr.add("'");
        arr.add("(");
        arr.add(")");
        arr.add("[");
        arr.add("]");
        arr.add("{");
        /*
        \u201c matches “ (left double quotation mark)
        \u201d matches ” (right double quotation mark)
        \u2018 matches ‘ (left single quotation mark)
        \u2019 matches ’ (right single quotation mark)
         */
        String[] parts = new String[0];
        for (int i = 0; i < arr.size(); i++) {
            if (word.startsWith(arr.get(i).toString()) || word.endsWith(arr.get(i).toString())) {
                word = word.replace((CharSequence) arr.get(i), "");
            }
        }
        return word;
    }
}
