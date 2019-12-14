package com.gesturedetection.application.controllers;

import org.springframework.http.HttpStatus;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;
import java.awt.AWTException;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;


import com.gesturedetection.application.services.GesteService;

@Service
@RestController
public class ApplicationController {
	
	@Value("#{file.to.open}")
	private String path;
	

	@GetMapping("/actions")
	public String firstPage() {
		return "welcom";
	}
	
	@GetMapping("/")
	public String HomePage() {
		return "home";
	}
	
	@GetMapping("/getAPI")
	public @ResponseBody ResponseEntity<List<Object>> getAPI(GesteService PTTFile) throws AWTException {
		try {
			PTTFile.startPTT(path);
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		//PTTService PTT = new PTTService();
		
		PTTFile.DoGeste(PTTFile.getGeste());
		
		return new ResponseEntity<List<Object>>(
				Arrays.asList(
				PTTFile.getGeste(),
				PTTFile.getPosition()),
				HttpStatus.OK);
		
		
		
	  }

}