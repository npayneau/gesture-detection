package com.gesturedetection.application.services;

import java.util.List;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.support.PropertySourcesPlaceholderConfigurer;

import java.util.ArrayList;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;

@Configuration
@PropertySource(value="classpath:application.properties")
public class PTTService {
	
	
	@Value("#{'${spring.cache.cache-names}'.split(',')}") 
	private List<String> raccourcis = new ArrayList<String>();
	
	private String chemin;

	
	@Bean
	public static PropertySourcesPlaceholderConfigurer propertyConfigInDev() {
		return new PropertySourcesPlaceholderConfigurer();
	}
	
	public List<String> getRaccourcis() {
		System.out.println(this.raccourcis);
		System.out.println(raccourcis);
		return raccourcis;
	}

	public String getChemin() {
		return chemin;
	}
	public void setChemin(String chemin) {
		this.chemin = chemin;
	}
	public PTTService() {
		this.chemin = "trouver le chemin";
	}
	
	public String getOS() {
	      String OS = System.getProperty("os.name");
	      System.out.println(OS);
	      return OS;
	}
	
	public void DoGeste(String geste) {
		
		
	}
}
