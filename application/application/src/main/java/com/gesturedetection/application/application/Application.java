package com.gesturedetection.application.application;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

//*************************************************************//
//       Classe de lancement du serveur Spring Boot            //
//*************************************************************//

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

}