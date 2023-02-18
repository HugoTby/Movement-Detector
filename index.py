import cv2
import datetime
import pygame

# Initialisation de Pygame
pygame.init()


# Chargement du son
sound = pygame.mixer.Sound('PYTHON/sound1.wav')

# Chargement du fichier cascade Haar pour la détection de personnes
person_cascade = cv2.CascadeClassifier('PYTHON/haarcascade_fullbody.xml')

# Ouverture du flux vidéo
video_capture = cv2.VideoCapture(0) # 0 indique la webcam par défaut, sinon indiquer le chemin vers le fichier vidéo

# cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Video', 1920, 1080)
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while True:
    # Lecture d'une image depuis le flux vidéo
    ret, frame = video_capture.read()
    
    # Conversion de l'image en niveau de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Détection des personnes dans l'image
    people = person_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))
    
    # Dessin des rectangles autour des personnes détectées
    for (x, y, w, h) in people:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sound.play()  # Joue le son lorsque la détection est effectuée

    # Affichage de l'heure en temps réel
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, 'CAMAERA 1', (frame.shape[1]-140, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)

    
    # Affichage de l'image
    cv2.imshow('Video', frame)
    # cv2.imshow('Video', gray)
    
    # Arrêt de la boucle si la touche 'q' est appuyée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fermeture du flux vidéo et des fenêtres d'affichage
video_capture.release()
cv2.destroyAllWindows()
