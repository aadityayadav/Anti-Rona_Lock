## ABOUT 

**Project Motivation**: 
COVID-19, Anti-maskers, People ignoring distancing regulations in public

**Function**: 
Our project takes pictures of people who wish to enter a building/room through a door. It determines whether masks are being worn and some distance is being maintained between individuals. If either of these conditions are not met, the door remains locked. Only when both conditions are satisfied is the door unlocked automatically.

**Approach**: 
We decided to use an Arduino as the microcontroller which would manipulate our lock, powered by a servo motor. The camera module we decided on had the ability to connect to the internet, which made sending images to our server (a computer) much easier. We decided to code in python, which allowed the use of the OpenCV library for image manipulation. We resolved that TensorFlow could be implemented for mask detection whereas Haar Cascades would suffice for distance detection, which only required detecting faces in an image.

## COLLABORATORS

*Aaditya Yadav* \
*David Xu* \
*Kevin Xu* \
*Kush Kansara* \
*William Xu*

## REFERENCES

Allan SAllan S 1, Dave RayDave Ray 37.9k77 gold badges7979 silver badges8282 bronze badges, KevinKevin 76155 silver badges88 bronze badges, Jmajma 69011 gold badge88 silver badges1717 bronze badges, BjornBjorn, & Micheal MorrowMicheal Morrow 3722 bronze badges. (1958, March 01). How do you run your own code alongside Tkinter's event loop? Retrieved December 02, 2020, from https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop 

Basics For Displaying Image In Tkinter Python. (n.d.). Retrieved December 02, 2020, from https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python 

Deep Learning From Scratch Part 1: Introduction to Neural Networks. (2020, August 04). Retrieved December 02, 2020, from https://www.youtube.com/watch?v=iCPvzMpLl88 

Esp32 face Detection with python part 2 : Getting output from esp32 and face detection with python. (2020, August 10). Retrieved December 02, 2020, from https://www.youtube.com/watch?v=92UBFhPJQJ8 
 
From mind to design in minutes. (n.d.). Retrieved December 03, 2020, from https://www.tinkercad.com/ 

Getting Started with Images. (n.d.). Retrieved December 02, 2020, from https://docs.opencv.org/master/db/deb/tutorial_display_image.html 

Getting Started with Images¶. (n.d.). Retrieved December 02, 2020, from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html 

Getting Started with Videos¶. (n.d.). Retrieved December 02, 2020, from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html 

Haddad, J. (2020, May 24). How I built a Face Mask Detector for COVID-19 using PyTorch Lightning. Retrieved December 02, 2020, from https://towardsdatascience.com/how-i-built-a-face-mask-detector-for-covid-19-using-pytorch-lightning-67eb3752fd61 

Human head. (2020, October 22). Retrieved December 02, 2020, from https://en.wikipedia.org/wiki/Human_head 

Image Module¶. (n.d.). Retrieved December 02, 2020, from https://pillow.readthedocs.io/en/stable/reference/Image.html 

Kazarinoff, P. (2018, December 20). Using Python to control an Arduino. Retrieved December 03, 2020, from https://pythonforundergradengineers.com/python-arduino-LED.html 

Matt GregoryMatt Gregory 5, Aki92aki92 1, Kayteckaytec, DF.dF. 65.1k2727 gold badges123123 silver badges134134 bronze badges, TreeDoNotSplitTreeDoNotSplit 9111 silver badge33 bronze badges, Martin GuilesMartin Guiles 5111 silver badge11 bronze badge, . . . Jose Pablo CastilloJose Pablo Castillo 1411 bronze badge. (1957, November 01). How do I close a tkinter window? Retrieved December 02, 2020, from https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window 

 Ravi, & Wallwin. (2016, August 24). Python + arduino controlling DC Motor. Retrieved December 03, 2020, from https://pythonpedia.com/en/knowledge-base/39107576/python-plus-arduino-controlling-dc-motor 

Real-Time Face Mask Detector with Python, OpenCV, Keras. (2020, August 06). Retrieved December 02, 2020, from https://data-flair.training/blogs/face-mask-detection-with-python/ 

RizwanRizwan 32411 gold badge33 silver badges1616 bronze badges, Michela RupertiMichela Ruperti 5433 bronze badges, Arno_varno_v 9, Eric FournieEric Fournie 1, & IbraIbra 7122 silver badges66 bronze badges. (1968, February 01). Does Any one got "AttributeError: 'str' object has no attribute 'decode' " , while Loading a Keras Saved Model. Retrieved December 02, 2020, from https://stackoverflow.com/questions/53740577/does-any-one-got-attributeerror-str-object-has-no-attribute-decode-whi 

Simplilearn. (2018, December 06). Scikit-Learn Tutorial | Machine Learning With Scikit-Learn | Sklearn | Python Tutorial | Simplilearn. Retrieved December 02, 2020, from https://www.youtube.com/watch?v=0Lt9w-BxKFQ 

Simplilearn. (2018, December 06). Scikit-Learn Tutorial | Machine Learning With Scikit-Learn | Sklearn | Python Tutorial | Simplilearn. Retrieved December 02, 2020, from https://www.youtube.com/watch?v=0Lt9w-BxKFQ 

Tensorflow. (n.d.). H5py==3.0.0 causes issues with keras model loads in tensorflow 2.1.0 · Issue #44467 · tensorflow/tensorflow. Retrieved December 02, 2020, from https://github.com/tensorflow/tensorflow/issues/44467 

Tkinter - Python interface to Tcl/Tk¶. (n.d.). Retrieved December 02, 2020, from https://docs.python.org/3/library/tkinter.html 

Wobbily_colwobbily_col 8, Sudeep JuvekarSudeep Juvekar 4, & ZuluZulu 6. (1963, May 01). Python "from [dot]package import ..." syntax. Retrieved December 02, 2020, from https://stackoverflow.com/questions/22511792/python-from-dotpackage-import-syntax 

X-zhangyang. (n.d.). X-zhangyang/Real-World-Masked-Face-Dataset. Retrieved December 02, 2020, from https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset 