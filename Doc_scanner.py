import cv2
import numpy as np

# Loading the image to scan the edges
img = cv2.imread('C:\\Users\\Jiya\\OneDrive\\Pictures\\abc card.jpg')

# handelling the error
if img is None:
    print("Error in loading the image, Please check for the file path.")
else:
    # Step 1 : Convertion to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 2 : Gaussian bluring the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    #Step 3 : Canny edge detection in image
    edge = cv2.Canny(blur, 50, 150)

    # Step 4 : Finding contours in image
    contour, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Step 5 : Drawing contours on the image
    cv2.drawContours(img, contour, -1, (0, 255, 0), 2)

    # Step 6 : Display results
    cv2.imshow('Edges in Green', img)

    # Closing
    cv2.waitKey(0)
    cv2.destroyAllWindows()
