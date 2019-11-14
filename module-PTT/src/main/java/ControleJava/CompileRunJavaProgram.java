package ControleJava;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;


public class CompileRunJavaProgram {
	private static void printLines(String name, InputStream ins) throws Exception {
		String line = null;
	    BufferedReader in = new BufferedReader(
	        new InputStreamReader(ins));
	    while ((line = in.readLine()) != null) {
	        System.out.println(name + " " + line);
	    }
	}

	private static void runProcess(String command) throws Exception {
		Process pro = Runtime.getRuntime().exec(command);
		printLines(command + " stdout:", pro.getInputStream());
		printLines(command + " stderr:", pro.getErrorStream());
		pro.waitFor();
		System.out.println(command + " exitValue() " + pro.exitValue());
	}

	public static void main(String[] args) {
		String fileName = "/Users/Theo/Downloads/Séance-3-2019.pptx";
		String fileExtention = "ppt";
		String classToOpen = "";
		switch(fileExtention)
        {
            case "ppt":
                classToOpen = "JavaOpenPPT";
            break;
            case "iot":
            	classToOpen = "JavaOpenIOT";
            break;
            default:
            	System.out.println("Error : No match to this extention");
            break;
        }
		try {
			runProcess("javac src/main/java/Modules/"+classToOpen+".java");
			runProcess("java src/main/java/Modules/"+classToOpen+".java " + fileName);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
