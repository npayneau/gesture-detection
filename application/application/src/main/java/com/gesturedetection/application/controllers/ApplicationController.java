package com.gesturedetection.application.controllers;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.awt.AWTException;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;


import com.gesturedetection.application.services.GesteService;

//*********************************************//
//        Controleur de l'application          //
//*********************************************//

@RestController
public class ApplicationController {
	
	private String prev_geste;  // Stockage du précédent 
	
	//------------------------------------------------------//
    //           Chemin de lancement du PPT                 //
    //------------------------------------------------------//
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
	
	//------------------------------------------------------//
    //           Chemin de reception du geste               //
	//														//
	// Parametre :											//
	// 		Object GesteService : object contenant le nom 	//
	//				du geste à effectué et diverses 		//
	//				autres composants						//
	//														//
    //------------------------------------------------------//
	@PostMapping("/getAPI")
	public @ResponseBody ResponseEntity<List<Object>> getAPI(GesteService PTTFile) throws AWTException {
		
		String new_geste = PTTFile.getGeste();     	// Extraction du nom du geste dans une variable
		
		PTTFile.DoGeste(new_geste);					// Effectue le geste dans le module 
		this.prev_geste = new_geste;
		
		return new ResponseEntity<List<Object>>(	// Affiche quelques composantes du l'Object receptionné sur une page web
				Arrays.asList(
				PTTFile.getGeste(),
				PTTFile.getPosition()),
				HttpStatus.OK);	
	  }

}