package com.gesturedetection.application.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.servlet.ModelAndView;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.*;

import java.awt.AWTException;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.List;


import com.gesturedetection.application.services.GesteService;


@RestController
public class ApplicationController {
	

	@GetMapping("/actions")
	public String firstPage() {
		return "welcom";
	}
	
	@GetMapping("/")
	public String HomePage() {
		return "home";
	}
	
	@RequestMapping("/getAPI")
	public List<Object> getAPI(GesteService PTTFile) throws AWTException {
		try {
			PTTFile.startPTT("/Users/Theo/Downloads/Séance-3-2019.pptx");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//PTTService PTT = new PTTService();
		
		PTTFile.DoGeste(PTTFile.getGeste());
		
		return Arrays.asList(
				PTTFile.getGeste(),
				PTTFile.getPosition());
		
		
		
	  }

}