import cv2
import pytesseract
from fastapi import UploadFile
import numpy as np


async def check_passport(file: UploadFile):
    # Read image with opencv

    img = cv2.imdecode(np.fromstring(await file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    dimensions = img.shape
    h = dimensions[0]
    w = dimensions[1]

    if w > h:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    resized = cv2.resize(img, (1024, 2048), interpolation=cv2.INTER_AREA)
    # Convert to gray
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)
    # Apply threshold to get image with only black and white
    gray = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", gray)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(gray, lang="rus")
    return result
    # gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.bitwise_not(gray)

    # # write the grayscale image to disk as a temporary file so we can
    # filename = "{}.png".format("temp")
    # cv2.imwrite(filename, gray)
    # result = pytesseract.image_to_string(gray, lang="eng+rus")
    # print(result)
    # return result
