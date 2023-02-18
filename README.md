# Movement Detector

The code is in Python and uses three main libraries: ``OpenCV (cv2)``, ``datetime``, and ``Pygame``. It is designed to open a webcam (or video file) and detect people in the image. When people are detected, a sound is played and a green rectangle is drawn around each detected person.

The code uses a Haar cascade file for person detection with the name "haarcascade_fullbody.xml". The code is executed in an infinite loop until the user presses the ``q`` key.

In addition to person detection, the code displays the current time in real time, as well as a green frame around the screen. It also displays a ``+`` symbol in the centre of the screen and red corners in the four corners of the screen.

The code also uses Pygame functions to load and play a sound file ``sound1.wav``, and to initialise Pygame.

Ultimately, the code displays the video in real time with green rectangles drawn around the detected people, as well as the current time and "+" and corner symbols.

---
# Run the code

To run the code, type the following command in your terminal:
```python

python file-path/index.py

```

---



## Screenshots

![App Screenshot](https://media.discordapp.net/attachments/733366929561092157/1076539504548126861/image.png?width=1616&height=909)
![App Screenshot](https://media.discordapp.net/attachments/733366929561092157/1076550240062152825/image.png?width=1616&height=909)



## Author

- [Hugo T](https://www.github.com/HugoTby)

