// Read CSV dataset  
package src;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class ReadCSV {
  // Parse CSV file into BufferedReader constructor
  static String filepath = "data/arabica_data_cleaned.csv";

  public static ArrayList<String> extractData(String filepath) {
    ArrayList<String> csv_lines = new ArrayList<>();
    String line = "";
    String splitBy = ",";

    try {
      // Open file reader  
      BufferedReader br = new BufferedReader(new FileReader(filepath));

      // While lines are valid
      while ((line = br.readLine()) != null) {
 
        // split line by char and convert to readable format
        String row = Arrays.deepToString(line.split(splitBy));
 
        // Add to list
        csv_lines.add(row); }
      
      // Close the open reader
      br.close(); 
      return csv_lines; }

    catch(IOException e) {
      e.printStackTrace();
      return csv_lines; }

  }

  public static void main() {
    ArrayList<String> dataset = extractData(ReadCSV.filepath);

    // print size 
    System.out.println(String.format("The lenght of the array is %s", dataset.size()));

  }

}