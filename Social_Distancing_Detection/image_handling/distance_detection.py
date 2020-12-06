from .facedetector import FaceDetector
from .distance_calculations import get_distance
import imutils
import cv2

# the following class will be able to detect whether faces are social distancing given an input file #

class DistanceDetector:

    image_file = None
    image = None
    gray = None
    distance_tolerance = None
    adj_width = None
    height = None
    all_faces = None
    face_distances = None
    all_breaches = None
    num_faces = 0
    CONST_DISTANCE_TOLERANCE = 1.5 #the minimum distance that people can be relative to each other without breaching regulation in METERS
    image_count = 0


    def __init__(self, image_file = None, image = [], distance_tolerance = CONST_DISTANCE_TOLERANCE, adj_width = 1000, height = 500):
        self.image_file = image_file
        self.distance_tolerance = distance_tolerance
        self.adj_width = adj_width
        self.height = height
        if len(image) > 0:
            self.image = imutils.resize(image, width=self.adj_width, height=self.height)
        else:
            self.image = imutils.resize(cv2.imread(image_file), width=self.adj_width, height=self.height)

        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def detectFaces(self):
        fd = FaceDetector()
        face_rects = fd.detect(self.gray, scaleFactor=1.1,
                              minNeighbors=8, minSize=(30, 30))

        self.all_faces = []
        for (x, y, w, h) in face_rects:
            start_cord = (x, y)
            end_cord = (x + w, y + h)
            cv2.rectangle(self.image, start_cord, end_cord, (0, 255, 0), 2)
            self.num_faces = len(face_rects)
            cv2.putText(self.image, "{} faces in this image".format(self.num_faces),
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
            self.all_faces.append({"startCord": start_cord, "endCord": end_cord})

    def detectDistances(self):
        self.detectFaces()
        self.face_distances = []
        faces_done = []
        for face in self.all_faces:
            for compFace in self.all_faces:
                if face != compFace and not ([compFace, face] in faces_done or [face, compFace] in faces_done):
                    distance = get_distance(face["startCord"][0], face["startCord"][1], face["endCord"][0], face["endCord"][1], compFace["startCord"][0], compFace["startCord"][1], compFace["endCord"][0], compFace["endCord"][1], self.adj_width)
                    self.face_distances.append({"faces": [face, compFace], "dist": distance})
                    faces_done.append([face, compFace])

    def getCloseFaces(self):
        self.detectDistances()
        # going through data structure to find exact people in breach and the location of their faces (to draw red rectangle around them)
        self.all_breaches = []
        for face_combo in self.face_distances:
            print(face_combo["dist"])
            if face_combo["dist"] < self.distance_tolerance:
                self.all_breaches.append(face_combo)
                cv2.putText(self.image, "Faces in this image not following social distancing",
                            (50, self.height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                print("SOCIAL DISTANCING IN BREACH")
                print("Face 1: {faceStart} to {faceEnd}".format(faceStart = face_combo["faces"][0]["startCord"], faceEnd = face_combo["faces"][0]["endCord"]))
                print("Face 2: {faceStart} to {faceEnd}".format(faceStart = face_combo["faces"][1]["startCord"], faceEnd = face_combo["faces"][1]["endCord"]))
                print("Distance: {distance}".format(distance = face_combo["dist"]))
                print("\n")

    def showImage(self):
        cv2.imshow("Faces", self.image)
        cv2.waitKey(0)

    #overwrites the image file with the same image but with green rectangle(s) around faces OR creates new image in specified location
    def writeImage(self, location=None):
        self.image_count += 1
        if location==None:
            cv2.imwrite(self.image_file, self.image)
        else:
            cv2.imwrite(location + "image" + str(self.image_count) + ".jpg", self.image)