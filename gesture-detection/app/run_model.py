from modules.CnnModel import CnnModel
from modules.Video import Video

# %% Parameters
camera = 0
resize = False
model_name = "model"
size = (100, 100, 3)

model = CnnModel(model_name=model_name, size=size)
video = Video(cnnmodel=model, camera=camera, resize=resize)
video.view(post=True)

