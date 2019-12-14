package com.gesturedetection.application;

import java.awt.AWTException;
import java.awt.Robot;

/**
 * A Java Robot example class.
 *
 * @author Alvin Alexander, http://devdaily.com
 *
 */
public class JavaRobotExample {
	
  Robot robot = new Robot();
  
  public JavaRobotExample() throws AWTException{}
  
  public void type(int i)
  {
    robot.delay(4000);
    robot.keyPress(i);
    robot.keyRelease(i);
  }

  public void type(String s)
  {
    byte[] bytes = s.getBytes();
    for (byte b : bytes)
    {
      int code = b;
      // keycode only handles [A-Z] (which is ASCII decimal [65-90])
      if (code > 96 && code < 123) code = code - 32;
      robot.delay(4000);
      robot.keyPress(code);
      robot.keyRelease(code);
    }
  }
}