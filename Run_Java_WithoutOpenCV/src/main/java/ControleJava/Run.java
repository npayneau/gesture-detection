package ControleJava;

import org.springframework.core.io.ClassPathResource;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.modelimport.keras.KerasModelImport;


public class Run {
	
	String simpleMlp = new ClassPathResource("simple_mlp.h5").getFile().getPath();
	MultiLayerNetwork model = KerasModelImport.importKerasSequentialModelAndWeights(simpleMlp);

	// ...

	INDArray output = model.output(input);

}
