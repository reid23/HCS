import matplotlib.pyplot as plt
from graphics import *
from math import *
import numpy as np
import io
import cv2

win=GraphWin('AutoDep', 800, 600)

valueInput=Entry(Point(250, 70), 10)
yearInput=Entry(Point(550, 70), 10)
valueText=Text(Point(250, 50), 'Initial Value')
yearText=Text(Point(550, 50), 'Time Since Purchase (Y)')

valueInput.draw(win)
yearInput.draw(win)
valueText.draw(win)
yearText.draw(win)

calcButton=Rectangle(Point(350, 170), Point(450, 200))
calcButton.setFill('blue')
calcText=Text(Point(400, 185), 'Calculate')
calcButton.draw(win)
calcText.draw(win)

while True:
    p=win.getMouse()
    if p.getX()>350 and p.getX()<450 and p.getY()<200 and p.getY()>170:
        break

initialVal=float(valueInput.getText())
years=int(yearInput.getText())

values=np.zeros(years)
values[0]=initialVal

for i in range(years):
    if i==0:
        continue
    values[i]=values[i-1]*0.85


print(values)
fig=plt.figure()
plt.bar(range(years), values, width=1, align='edge')
plt.xlim(0, years)

plt.show()

plt.close(fig)

def get_img_from_fig(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

img=get_img_from_fig(fig)

img=Image(Point(400, 250), img)
win.draw(img)



