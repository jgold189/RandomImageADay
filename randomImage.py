from PIL import Image
import numpy as np
from datetime import datetime
import webbrowser

#Width and height for the image
w, h = 512, 512
data = np.random.randint(256, size=(h, w, 3), dtype=np.uint8)
img = Image.fromarray(data, "RGB")
todayFile = "images/" + str(datetime.today().strftime("%m-%d-%Y")) + ".png"
img.save(todayFile)
#webbrowser.open(todayFile)