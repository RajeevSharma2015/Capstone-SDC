from styx_msgs.msg import TrafficLight
import tensorflow as tf
import numpy as np

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier

	# Path to frozen detection graph. This is the actual model that is used for the object detection.
	#PATH_TO_CKPT = 'light_classification/Faster-RCNN-10K/frozen_inference_graph.pb' #MODEL_NAME + '/frozen_inference_graph.pb'
	#PATH_TO_CKPT = 'light_classification/sim-40k/frozen1/frozen_inference_graph.pb'
        PATH_TO_CKPT = 'light_classification/SSD-Sim-Train/frozen/frozen_inference_graph.pb'

        # Load a frozen tensorflow into memory
	self.detection_graph = tf.Graph()

	with self.detection_graph.as_default():
	    od_graph_def = tf.GraphDef()
	    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
	        serialized_graph = fid.read()
	        od_graph_def.ParseFromString(serialized_graph)
	        tf.import_graph_def(od_graph_def, name='')
	    
            #Setup session inputs
	    # Definite input and output Tensors for detection_graph
	    self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
	    # Each box represents a part of the image where a particular object was detected.
	    self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
	    # Each score represent how level of confidence for each of the objects.
	    # Score is shown on the result image, together with the class label.
	    self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
	    self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
	    self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

	 # with  as self.sess:
	self.session =  tf.Session(graph=self.detection_graph)

	self.detection_threshold =.20

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
           int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # Actual detection.
        (boxes, scores, classes, num) = self.session.run(
	  [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
	  feed_dict={self.image_tensor: image_np_expanded})

        # The model by default detect upto 10 objects (lightss), we are going to assume that all lights are from the same singlaed intersection.
        # Calssification
	scores = np.squeeze(scores) # get rid of outer dimension
	classes = np.int32(np.squeeze(classes))
	
	#As the results are ordered in the detection probability we are jsut going to pick the highest.
	highest_score = scores[0]
        highest_class = classes[0]
	detected_Light = TrafficLight.UNKNOWN
	if highest_score > self.detection_threshold:
	    if highest_class   == 1:
		detected_Light = TrafficLight.GREEN
	    elif highest_class == 2:
		detected_Light = TrafficLight.RED
	    elif highest_class == 3:
		detected_Light = TrafficLight.YELLOW
      
        return detected_Light 
