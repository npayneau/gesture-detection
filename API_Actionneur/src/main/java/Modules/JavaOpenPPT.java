package Modules;

import java.awt.Desktop;
import java.io.File;
import java.io.IOException;

public class JavaOpenPPT {

    public static void main(String[] args) throws IOException {
    	
    	String fileName;
    	
    	// Catch the bame of the file
    	if (args.length > 0) {
			fileName = args[0];
		} else {
			System.out.println("No file name specified.");
			return;
		}
    	
        // PTT FIle
        File file = new File(fileName);
        
        //first check if Desktop is supported by Platform or not
        if(!Desktop.isDesktopSupported()){
            System.out.println("Desktop is not supported");
            return;
        }
        
        Desktop desktop = Desktop.getDesktop();
        if(file.exists()) desktop.open(file);
        
    }

}