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
    cv2.putText(frame, current_time, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, 'CAMAERA 1', (frame.shape[1]-160, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv2.LINE_AA)

    # Dessin d'un cadre autour de l'écran
    frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 255, 0), 2)

    # Dessin du symbole "+"
    center_x, center_y = int(frame.shape[1]/2), int(frame.shape[0]/2)
    cv2.line(frame, (center_x-20, center_y), (center_x+20, center_y), (0, 0, 255), 2)
    cv2.line(frame, (center_x, center_y-20), (center_x, center_y+20), (0, 0, 255), 2)

    # Ajout des angles
    angle_size = 20
    angle_color = (0, 0, 255)
    frame_height, frame_width = frame.shape[:2]
    cv2.line(frame, (angle_size, angle_size), (angle_size, angle_size + 50), angle_color, 2)
    cv2.line(frame, (angle_size, angle_size), (angle_size + 50, angle_size), angle_color, 2)
    cv2.line(frame, (frame_width - angle_size, angle_size), (frame_width - angle_size, angle_size + 50), angle_color, 2)
    cv2.line(frame, (frame_width - angle_size, angle_size), (frame_width - angle_size - 50, angle_size), angle_color, 2)
    cv2.line(frame, (angle_size, frame_height - angle_size), (angle_size, frame_height - angle_size - 50), angle_color, 2)
    cv2.line(frame, (angle_size, frame_height - angle_size), (angle_size + 50, frame_height - angle_size), angle_color, 2)
    cv2.line(frame, (frame_width - angle_size, frame_height - angle_size), (frame_width - angle_size, frame_height - angle_size - 50), angle_color, 2)
    cv2.line(frame, (frame_width - angle_size, frame_height - angle_size), (frame_width - angle_size - 50, frame_height - angle_size), angle_color, 2)



    
    # Affichage de l'image
    cv2.imshow('Video', frame)
    # cv2.imshow('Video', gray)
    
    # Arrêt de la boucle si la touche 'q' est appuyée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fermeture du flux vidéo et des fenêtres d'affichage
video_capture.release()
cv2.destroyAllWindows()
