package springbootopenCV;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.videoio.VideoCapture;
import org.springframework.boot.SpringApplication;
 
public class SpringBootOpenCV {
    public static void main(String[] args) {
        // Load Native Library
        //System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    	nu.pattern.OpenCV.loadLocally();
        // image container object
        Mat imageArray = new Mat();
        // Video device acces
        VideoCapture videoDevice = new VideoCapture();
        // 0:Start default video device 1,2 etc video device id
        videoDevice.open(0);
        // is contected
        if (videoDevice.isOpened()) {
        // Get frame from camera
            videoDevice.read(imageArray);
            // image array
            System.out.println(imageArray.toString());
            // Release video device
            videoDevice.release();
        } else {
            System.out.println("Error.");
        }
        SpringApplication.run(SpringBootOpenCV.class, args);
    }
}