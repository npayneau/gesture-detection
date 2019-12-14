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
	
	private String prev_geste;
	

	@GetMapping("/actions")
	public String firstPage() {
		return "welcom";
	}
	
	@GetMapping("/")
	public String HomePage() {
		GesteService PTTFile = new GesteService();
		try {
			PTTFile.startPTT("D:\\Jules\\Documents\\GitHub\\gesture-detection\\gesture-detection\\app\\data\\PEE.pptx");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "home";
	}
	
	@PostMapping("/getAPI")
	public @ResponseBody ResponseEntity<List<Object>> getAPI(GesteService PTTFile) throws AWTException {
		String new_geste = PTTFile.getGeste();
		
		if(!(new_geste.equals(this.prev_geste))) {
			PTTFile.DoGeste(new_geste);
			this.prev_geste = new_geste;
		}
		
		return new ResponseEntity<List<Object>>(
				Arrays.asList(
				PTTFile.getGeste(),
				PTTFile.getPosition()),
				HttpStatus.OK);	
	  }

}