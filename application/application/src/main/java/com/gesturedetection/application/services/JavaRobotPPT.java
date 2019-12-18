package com.gesturedetection.application.services;

import java.awt.AWTException;
import java.awt.Robot;

/**
 * A Java Robot example class.
 *
 * @author Alvin Alexander, http://devdaily.com
 *
 */


//*************************************************************************//
//			Classe effectuant l'action pour un fichier PowerPoint          //
//*************************************************************************//

public class JavaRobotPPT {
	
  Robot robot = new Robot();
  
  public JavaRobotPPT() throws AWTException{}  	// Contructeur
  
  //--------------------------------------------------------//
  //        Effcetue l'action passé en paramètre          	//
  //														//
  // Parametre :											//
  // 		String s : Commande robot permettant à la 		//
  //				   librairie Robot d'effectuer une		//
  //				   action sur le système 				//
  //														//
  //--------------------------------------------------------//
  
  public void type(String s)
  {
    byte[] bytes = s.getBytes();
    for (byte b : bytes)
    {
      int code = b;
      // keycode ne supposte que des [A-Z] (qui est en décimal ASCII [65-90])
      if (code > 96 && code < 123) code = code - 32;
      robot.delay(40);
      robot.keyPress(code);
      robot.keyRelease(code);
    }
  }
  
  public void type(int i)						// Même objectif que la classe précédente pour un int en paramètre au lieu d'un String 
  {
    robot.delay(40);
    robot.keyPress(i);
    robot.keyRelease(i);
  }
}