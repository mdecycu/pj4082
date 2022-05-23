import pySTL
from numpy import array

def leoprint(x):
    try:
        print(x)
    except:
        g.es(x)

#Load a model from a file.
#打開stl檔案路徑
model = pySTL.STLmodel('F:\\pystl\\link2_binary.stl') 
#印出體積數值
leoprint(model.get_volume())

#print model properties
#印出Volume +體積數值
leoprint("Volume  " + str(model.get_volume()))
c = model.get_centroid()
leoprint("Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2]))

#Translate the model so that the centroid is at the origin.
#將形心移動到原點
model.translate(-c)
#生成檔案
model.write_text_stl("link2_ascii.stl")

#Rotate the model 90 degrees about the Y-axis
#物體以Y軸調整角度，所以轉-90度
#必須使用弧度
R2 = pySTL.rotationAboutY(-3.14159/2)

model.rotate(R2)

#得到link2_ascii.stl形心
c = model.get_centroid()

leoprint("Centroid " +  "X: " + str(c[0]) + " Y:" + str(c[1]) + "  Z:" + str(c[2]))
#生成檔案
model.write_text_stl('link2_ascii_-90deg_Y-axis.stl')

#Scale the model down by 100%
#調整比例，所小檔案0.1%
scale = 0.001
model.scale(scale)

#生成檔案
model.write_text_stl('link2_ascii_scale_down_0.001.stl')
