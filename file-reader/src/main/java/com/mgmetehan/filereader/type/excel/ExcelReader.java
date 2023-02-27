package com.mgmetehan.filereader.type.excel;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;

public class ExcelReader {
    public void readExcelFirst2Byte(String path) {
        String value = null;

        try {
            FileInputStream file = new FileInputStream(new File(path));
            XSSFWorkbook workbook = new XSSFWorkbook(file);
            XSSFSheet sheet = workbook.getSheetAt(0);
            Iterator<Row> rowIterator = sheet.iterator();
            Row row = rowIterator.next();
            Iterator<Cell> cellIterator = row.cellIterator();

            Cell cell = cellIterator.next();
            if (cell.getCellType() == CellType.STRING) {
                value = cell.getStringCellValue();
            } else if (cell.getCellType() == CellType.NUMERIC) {
                value = String.valueOf(cell.getNumericCellValue());
            }
            for (int i = 0; i < 2; i++) {
                System.out.println(value.charAt(i));
            }
            file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        ExcelReader excelReader = new ExcelReader();
        var path = "/Users/mgmetehan/Desktop/chomar/deneme.xlsx";
        excelReader.readExcelFirst2Byte(path);
    }
}
