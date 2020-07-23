# This program reads text from lincense document in image format
# from specific coordinates and saves them into a file
#
# Authour: Joseph Afriyie Attakorah
# Supervisor: Hadi Saleh

import cv2
import pytesseract

# Thee installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image from which text needs to be extracted
image = cv2.imread('files/test03.jpg', 0)
# OTSU threshold
thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

labels_coordinates = \
    [
        ('DCCINo', [1170, 480, 210, 50])
        , ('LegalType_EN', [1190, 545, 180, 40])
        , ('LegalType_AR', [470, 830, 750, 55])
        , ('TradeName_EN', [1700, 830, 340, 55])
        , ('TradeName_AR', [470, 975, 750, 55])
        , ('EstablishmentDate', [1650, 910, 379, 55])
        , ('IssueDate', [470, 1050, 950, 55])
        , ('ExpiryDate', [470, 1120, 950, 55])
        , ('Role_EN', [470, 1195, 950, 55])
        , ('Role_AR', [65, 1760, 350, 55])
        , ('Nationality_EN', [65, 1700, 350, 55])
        , ('Nationality_AR', [480, 1760, 350, 55])
        , ('FullName_EN', [480, 1700, 350, 55])
        , ('FullName_AR', [875, 1760, 1300, 55])
        , ('NoAD', [875, 1700, 1300, 55])
        , ('LicenseActivities_EN', [2100, 1700, 1900, 55])
        , ('LicenseActivities_AR', [30, 1895, 1700, 55])
        , ('Address', [1750, 1895, 710, 55])
    ]

for label_coordinate in labels_coordinates:
    x, y, w, h = label_coordinate[1]
    # Get the bounding box
    ROI = thresh[y:y + h, x:x + w]
    # Read from the bounding box
    data = pytesseract.image_to_string(ROI, lang='eng+ara', config='--psm 6')
    # print(label_coordinate[0] + ': ' + data)
    # save to file
    f = open("doc.txt", "a", encoding='utf-8')
    f.write(label_coordinate[0] + ': ' + data + '\n')
    f.close()

# x, y, w, h = 1750, 1895, 710, 55
# ROI = thresh[y:y + h, x:x + w]
# data = pytesseract.image_to_string(ROI, lang='eng+ara', config='--psm 6')
# print(data)
# cv2.imshow('ROI', ROI)
# cv2.waitKey()

# coordinates = \
#     [
#         [1170, 480, 210, 50]
#         , [1190, 545, 180, 40]
#         , [470, 830, 750, 55]
#         , [1700, 830, 340, 55]
#         , [470, 975, 750, 55]
#         , [1650, 910, 379, 55]
#         , [470, 1050, 950, 55]
#         , [470, 1120, 950, 55]
#         , [470, 1195, 950, 55]
#         , [65, 1760, 350, 55]
#         , [65, 1700, 350, 55]
#         , [480, 1760, 350, 55]
#         , [480, 1700, 350, 55]
#         , [875, 1760, 1300, 55]
#         , [875, 1700, 1300, 55]
#         , [2100, 1700, 1900, 55]
#         , [30, 1895, 1700, 55]
#         , [1750, 1895, 710, 55]
#         , [500, 2290, 2600, 55]
#     ]
#
# labels = \
#     [
# 'DCCINo'
#         , 'LegalType_EN'
#         , 'LegalType_AR'
#         , 'TradeName_EN'
#         , 'TradeName_AR'
#         , 'EstablishmentDate'
#         , 'IssueDate'
#         , 'ExpiryDate'
#         , 'Role_EN'
#         , 'Role_AR'
#         , 'Nationality_EN'
#         , 'Nationality_AR'
#         , 'FullName_EN'
#         , 'FullName_AR'
#         , 'NoAD'
#         , 'LicenseActivities_EN'
#         , 'LicenseActivities_AR'
#         , 'Address'
#     ]