import cv2
import pytesseract
from fastapi import UploadFile
import numpy as np


async def check_passport(file: UploadFile):
    # Распознать ПТС
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO)[1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, img)
    text = pytesseract.image_to_string(img, lang="rus+eng")
    return text
