package com.gesturedetection.application.services;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
@ConfigurationProperties(prefix = "gestes.raccourcis")
public class Raccourcis {
        private List<String> mac = new ArrayList<>();

        public List<String> getRaccourcis() {
                return mac;
        }

        public boolean keep(String geste) {
                return mac.contains(geste);
        }
}
