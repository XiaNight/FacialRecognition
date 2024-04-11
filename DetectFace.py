import dlib
import PIL
import matplotlib

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Returns true if detects any face in the PIL image


def DetectFace(image):
    # Convert PIL image to numpy array
    img = np.array(image)
    # Detect faces in the image
    faces = detector(img)
    # If no faces detected, return false
    if len(faces) == 0:
        return False
    # Get the first face
    face = faces[0]
    # Get the landmarks of the face
    landmarks = predictor(img, face)
    # Return true if face detected
    return True
