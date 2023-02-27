package com.mgmetehan.filereader.shared.util;

import lombok.experimental.UtilityClass;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

@UtilityClass
public class FinderAll {
    //var path = "/Users/mgmetehan/Desktop/chomar";

    public List<String> listAllTypesInFolder(String path) {
        List<String> results = new ArrayList<String>();

        File[] files = new File(path).listFiles();

        for (File file : files) {
            if (file.isFile()) {
                results.add(file.getName());
                System.out.println(file.getName());
            }
        }
        return results;
    }

    public List<String> listSpecificTypesInFolder(String path, String type) {
        // type = ".pdf"
        List<String> results = new ArrayList<String>();

        File[] files = new File(path).listFiles((dir, name) -> name.endsWith(type));

        for (File file : files) {
            if (file.isFile()) {
                results.add(file.getName());
                System.out.println(file.getName());
            }
        }
        return results;
    }
}
