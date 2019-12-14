package com.gesturedetection.application.controllers;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.awt.AWTException;
import java.io.IOException;
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
		GesteService PTTFile = new GesteService();
		try {
			PTTFile.startPTT("D:\\Jules\\Documents\\1.pptx");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "home";
	}
	
	@PostMapping("/getAPI")
	public @ResponseBody ResponseEntity<List<Object>> getAPI(GesteService PTTFile) throws AWTException {
		
		PTTFile.DoGeste(PTTFile.getGeste());
		
		return new ResponseEntity<List<Object>>(
				Arrays.asList(
				PTTFile.getGeste(),
				PTTFile.getPosition()),
				HttpStatus.OK);	
	  }

}