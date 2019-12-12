package com.gesturedetection.application.services;

import java.io.File;

import java.util.List;
import java.io.IOException;
import java.awt.AWTException;
import java.awt.Desktop;
import java.awt.event.KeyEvent;

/*
import org.apache.poi.sl.usermodel.AutoNumberingScheme;
import org.apache.poi.sl.usermodel.PictureData;
import org.apache.poi.sl.usermodel.TableCell;
import org.apache.poi.sl.usermodel.TextParagraph;
import org.apache.poi.util.IOUtils;
*/
import org.apache.poi.xslf.usermodel.*;

import com.gesturedetection.application.JavaRobotExample;

import java.io.FileInputStream;
/*
import java.awt.*;
import java.io.FileOutputStream;
import java.util.List;
*/


public class GesteService {

  private String geste;
  private String position;
  // Formats output date when this DTO is passed through JSON
  //@JsonFormat(pattern = "dd/MM/yyyy")
  // Allows dd/MM/yyyy date to be passed into GET request in JSON
  //@DateTimeFormat(pattern = "dd/MM/yyyy")

  public GesteService(String geste, String position) {
    this.geste = geste;
    this.position = position;
  }

  public GesteService() {}
  
  
  public void setGeste(String geste) {
	  this.geste = geste;
  }
  
  public String getGeste() {
	  System.out.println(geste);
	  return geste;
  }
  
  public void setPosition(String position) {
	  this.position = position;
  }
  
  public String getPosition() {
	  return position;
  }
  
  /*
  public XMLSlideShow readingExistingSlideShow(String fileLocation) throws IOException {
      return new XMLSlideShow(new FileInputStream(fileLocation));
  }
  */
  
  
  public void startPTT(String nameFile) throws IOException {
	  
	  File file = new File(nameFile);
  
	  if(!Desktop.isDesktopSupported()){
          System.out.println("Desktop is not supported");
          return;
      }
      
      Desktop desktop = Desktop.getDesktop();
      if(file.exists()){desktop.open(file);
      
      }
  }
  static {

      System.setProperty("java.awt.headless", "false");
  }
  
  public void DoGeste(String geste) throws AWTException {
	  JavaRobotExample Robot = new JavaRobotExample();
	  switch(geste) {
	  case "Poing":
	    Robot.type(KeyEvent.VK_ESCAPE);
	    break;
	  case "Doigt 1":
		  Robot.type(KeyEvent.VK_KP_LEFT);
	    break;
	  case "Main Ouverte":
		  Robot.type(KeyEvent.VK_F5);
		break;
	  case "2 Doigts":
		  Robot.type(KeyEvent.VK_KP_RIGHT);
		break;
	  case "Rien":
		  Robot.type(KeyEvent.VK_ESCAPE);
		break;
	  default:
	    // code block
	}
  }

}
