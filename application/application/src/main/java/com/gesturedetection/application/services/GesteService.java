package com.gesturedetection.application.services;

import java.io.File;
import java.io.IOException;
import java.awt.AWTException;
import java.awt.Desktop;
import java.awt.event.KeyEvent;


//****************************************************************//
//    Classe créant l'object geste passé au controleur Java       //
//****************************************************************//


public class GesteService {

  private String geste;
  private String position;

  public GesteService(String geste, String position) {
    this.geste = geste;
    this.position = position;
  }

  public GesteService() {}  			// Constructeur
  
  //--------------------------------------------//
  //        Modifie le geste de l'objet        	//
  //--------------------------------------------//
  public void setGeste(String geste) {
	  this.geste = geste;
  }
  
  //--------------------------------------------//
  //        Renvoie le geste de l'objet        	//
  //--------------------------------------------//
  public String getGeste() {
	  return geste;
  }
  //------------------------------------------------//
  //        Modifie la position de l'objet        	//
  //------------------------------------------------//
  public void setPosition(String position) {
	  this.position = position;
  }
  
  //------------------------------------------------//
  //        Renvoie la position de l'objet        	//
  //------------------------------------------------//
  public String getPosition() {
	  return position;
  }
  
  //------------------------------------------------//
  //        Lance le fichier PowerPoint          	//
  //------------------------------------------------//
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
  
  // Propriété indispensable au bon fonctionnement de la classe Robot
  static {
      System.setProperty("java.awt.headless", "false");
  }
  
  //------------------------------------------------------------//
  //        Choix de l'action en fonction du geste          	//
  //------------------------------------------------------------//
  public void DoGeste(String geste) throws AWTException {
      System.out.println(geste);
	  JavaRobotPPT Robot = new JavaRobotPPT();
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
