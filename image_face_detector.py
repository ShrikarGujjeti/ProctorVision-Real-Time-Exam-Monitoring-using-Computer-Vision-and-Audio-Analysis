#image face detector
import cv2
import numpy as np


def get_face_detector(modelFile=None, configFile=None, quantized=False):

    try:
        if quantized:
            if modelFile is None:
                modelFile = "models/opencv_face_detector_uint8.pb"
            if configFile is None:
                configFile = "models/opencv_face_detector.pbtxt"
            model = cv2.dnn.readNetFromTensorflow(modelFile, configFile)
        else:
            if modelFile is None:
                modelFile = "models/res10_300x300_ssd_iter_140000.caffemodel"
            if configFile is None:
                configFile = "models/deploy.prototxt"
            model = cv2.dnn.readNetFromCaffe(configFile, modelFile)

        print("Model loaded successfully!")
        return model

    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def find_faces(img, model):
    """
    Find the faces in an image.
    """
    try:
        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))
        model.setInput(blob)
        res = model.forward()
        faces = []
        for i in range(res.shape[2]):
            confidence = res[0, 0, i, 2]
            if confidence > 0.5:
                box = res[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x1, y1) = box.astype("int")
                faces.append([x, y, x1, y1])
        return faces

    except Exception as e:
        print(f"Error finding faces: {e}")
        return []


def draw_faces(img, faces):
    """
    Draw faces on image.
    """
    for x, y, x1, y1 in faces:
        cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 3)


# Example usage with a local image
face_model = get_face_detector()
if face_model:
    img = cv2.imread('C:\MINI PROJECT\MOTION DETECTION\Proctoring-AI\models\img_3.png')  # Replace with your local image path
    if img is not None:
        faces = find_faces(img, face_model)
        draw_faces(img, faces)
        cv2.imshow('Faces', img)
        cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        cv2.destroyAllWindows()
    else:
        print("Error: Image not found.")
