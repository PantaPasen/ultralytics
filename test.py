import ultralytics_bower

if True:
    model = ultralytics_bower.YOLO("yolov8-multihead.yaml")
    model.train(
        data='/workspaces/ultralytics/crowdsourced-yolo-data-mh/data.yaml', 
        epochs=5,
        #cache=True,
        resume=True,
        workers=1,
        verbose=True,
        #pretrained='yolov8n.pt',
        )
else:
    model = ultralytics_bower.YOLO("runs/detect/train3/weights/best.pt")
    model.val()