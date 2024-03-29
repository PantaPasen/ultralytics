import ultralytics_bower

model = ultralytics_bower.YOLO("yolov8-multihead.yaml")
model.train(
    data='/workspaces/ultralytics/crowdsourced-yolo-data-mh/data.yaml', 
    epochs=2,
    #cache=True,
    resume=True,
    workers=1,
    verbose=True,
    #pretrained='yolov8n.pt',
    )