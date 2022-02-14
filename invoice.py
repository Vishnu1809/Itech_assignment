from PIL import Image
import pytesseract
import os


data = {"image_details":[]}
folder_dir = "/home/vishnu/Desktop/itech/rvl-cd/invoices"
for image_path in os.listdir(folder_dir):
    if (image_path.endswith(".tif")):
        img = Image.open(f'{folder_dir}/{image_path}')
        text = pytesseract.image_to_string(img)
        data["image_details"].append({'image_path':image_path})
        data["image_details"].append({'text':text})


with open("final.txt", 'w')as final:
    final.write(str(data))

