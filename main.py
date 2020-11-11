from time import sleep
from PIL import Image, ImageTk
#I installed PIL (pillow) using "pip3 install pillow"
import tkinter
from Social_Distancing_Detection.image_handling.distance_detection import DistanceDetector
import os

#below are dummy functions

def arduino_start():
    print("Arduino started.")
    return

def arduino_get_image():
    print("Retrieved image successfully.")
    return 0

def arduino_range_sensor():
    #will tell us if there is an object in front of the door
    print("There is someone at the door.")
    return True

def arduino_unlock_door():
    print("Door unlocked successfully.")
    return

def arduino_lock_door():
    print("Door locked successfully.")
    return

def arduino_stop():
    print("Arduino stopped.")
    return

def mask_detection(image):
    print("Masks are not being worn.")
    return False

def distance_detection(image):
    print("Distance is being maintained.")
    # detector = DistanceDetector(image)
    # detector.getCloseFaces()
    # allBreaches = detector.all_breaches
    # if len(allBreaches > 0):
    #     return False #do not open door, they are not following rules
    return True #open door

# def main():
#     arduino_start()
#     locked = True
#     wait_time = 1
#     while locked:
#         if arduino_range_sensor():
#             image = arduino_get_image()
#             masks = mask_detection(image)
#             distancing = distance_detection(image)
#             if (masks and distancing):
#                 arduino_unlock_door()
#                 locked = False
#             else:
#                 print("Violation detected. Waiting " + str(wait_time) + " seconds before getting new image.")
#                 sleep(wait_time)
            
#     sleep(5)
#     arduino_lock_door()
#     arduino_stop()
#     print("Program Finished.")


if __name__ == "__main__":
    
    # main()

    image_list = []

    root = tkinter.Tk()
    root.title("Main")

    CONST_CANVAS_WIDTH = 1000
    CONST_CANVAS_HEIGHT = 1000
    CONST_CANVAS_MAX_IMAGE_HEIGHT = 800
    canvas = tkinter.Canvas(root, width=CONST_CANVAS_WIDTH, height=CONST_CANVAS_HEIGHT) 
    canvas.pack()     
    
    def new_size(size, desired_width=CONST_CANVAS_WIDTH):
        width = size[0]
        height = size[1]
        new_width = desired_width
        new_height = (int) ((desired_width/width)*height)
        if new_height > CONST_CANVAS_MAX_IMAGE_HEIGHT:
            new_height = CONST_CANVAS_MAX_IMAGE_HEIGHT
            new_width = (int) ((CONST_CANVAS_MAX_IMAGE_HEIGHT/new_height)*new_width)
        return (new_width, new_height)

    def image(filename, location):
        abs_path = location + filename
        img_size = Image.open(abs_path).size
        # print(img_size)
        # print("new size: " + str(new_size(img_size)))
        resized_img = Image.open(abs_path).resize(new_size(img_size))
        img = ImageTk.PhotoImage(resized_img)
        # alternative method: img = tkinter.PhotoImage(file="filename")
        return img

    images_abs_path = os.path.dirname(os.path.abspath(__file__)) + "\\images\\"

    img1 = image("cat1.png", images_abs_path)
    img2 = image("cat2.jpg", images_abs_path)
    img3 = image("cat3.jpg", images_abs_path)

    image_list.append(img1)
    image_list.append(img2)    
    image_list.append(img3)

    i = 0
    canvas.create_image(0,0, anchor=tkinter.constants.NW, image=image_list[i])   

    def next_image():
        canvas.delete("all")
        global i
        i += 1
        if i >= len(image_list):
            i = 0
        canvas.create_image(0,0, anchor=tkinter.constants.NW, image=image_list[i])

    def prev_image():
        canvas.delete("all")
        global i
        i -= 1
        if i < 0:
            i = len(image_list)-1
        canvas.create_image(0,0, anchor=tkinter.constants.NW, image=image_list[i])
        

    button = tkinter.Button(root, text="Next Image", command=next_image)
    button.place(x=500,y=900)
    button = tkinter.Button(root, text="Previous Image", command=prev_image)
    button.place(x=400,y=900)

    #this code replaces main()
    arduino_start()
    CONST_WAIT_TIME = 3
    def while_loop():
        if arduino_range_sensor():
            image = arduino_get_image()
            # image_list.append(image)
            next_image()
            masks = mask_detection(image)
            distancing = distance_detection(image)
            if (masks and distancing):
                arduino_unlock_door()
                sleep(5)
                arduino_lock_door()
                arduino_stop()
                print("Program Finished.")
            else:
                print("Violation detected. Waiting " + str(CONST_WAIT_TIME) + " seconds before trying again.")
                root.after(CONST_WAIT_TIME*1000, while_loop)
        
    root.after(CONST_WAIT_TIME*1000, while_loop)
    
    root.mainloop()  