package ControleJava;

import org.springframework.core.io.ClassPathResource;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;
import org.deeplearning4j.nn.modelimport.keras.exceptions.InvalidKerasConfigurationException;
import org.deeplearning4j.nn.modelimport.keras.exceptions.UnsupportedKerasConfigurationException;
import org.nd4j.linalg.api.ndarray.INDArray;
import org.datavec.image.loader.NativeImageLoader;
import java.awt.Image;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;


public class Run {
	
	private static NativeImageLoader imageLoader = new NativeImageLoader(100, 100, 3);
	
	public static INDArray recognise(String name) throws IOException, InvalidKerasConfigurationException, UnsupportedKerasConfigurationException {
		String simpleMlp = new ClassPathResource("src/main/resources/11-27-19-12h41m55s.h5").getFile().getPath();
		MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights(simpleMlp);
		
		Image picture = ImageIO.read(new File(name));
		INDArray image = imageLoader.asMatrix(picture);
		//preProcessor.transform(image);
		INDArray output = model.output(image);
		return output;
	}
	
	public static void main(String[] args) throws IOException, InvalidKerasConfigurationException, UnsupportedKerasConfigurationException {
		
		String fileName = "src/main/resources/78210100_453493245361163_6520881419101667328_n.jpg";
		INDArray output = recognise(fileName);
		System.out.println(output);
	}
}
