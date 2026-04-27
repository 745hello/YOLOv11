yolo task=detect mode=train model=/home/dl/xg/yolov11/ultralytics/cfg/models/11/yolo11s.yaml data=/home/dl/xg/yolov11/myCoco.yaml epochs=300 device=0,1,2,3,4,5,6,7 batch=64 patience=300 save_json=True workers=16

