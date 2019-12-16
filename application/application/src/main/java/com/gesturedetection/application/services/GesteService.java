package com.gesturedetection.application.services;

import java.io.File;
import java.io.IOException;
import java.awt.AWTException;
import java.awt.Desktop;
import java.awt.event.KeyEvent;

import com.gesturedetection.application.JavaRobotExample;

public class GesteService {

  private String geste;
  private String position;

  public GesteService(String geste, String position) {
    this.geste = geste;
    this.position = position;
  }

  public GesteService() {}
  
  
  public void setGeste(String geste) {
	  this.geste = geste;
  }
  
  public String getGeste() {
	  return geste;
  }
  
  public void setPosition(String position) {
	  this.position = position;
  }
  
  public String getPosition() {
	  return position;
  }
  
  
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
      System.out.println(geste);
	  JavaRobotExample Robot = new JavaRobotExample();
	  switch(geste) {
	  case "Poing":
	    //Robot.type(KeyEvent.VK_ESCAPE);
	    break;
	  case "Doigt 1":
		  //Robot.type(KeyEvent.VK_F5);
		  Robot.type(KeyEvent.VK_N);
	    break;
	  case "Main Ouverte":
		  Robot.type(KeyEvent.VK_F5);
		break;
	  case "2 Doigts":
		  //Robot.type(KeyEvent.VK_F5);
		  Robot.type(KeyEvent.VK_B);
		break;
	  case "Pouce Haut":
		  //Robot.type(KeyEvent.VK_F5);
		  Robot.type(KeyEvent.VK_P);
		break;
	  case "Rien":
	  	  //Robot.type(KeyEvent.VK_F5);
		  //Robot.type(KeyEvent.VK_ESCAPE);
		break;
	  default:
	    // code block
	}
  }
}
