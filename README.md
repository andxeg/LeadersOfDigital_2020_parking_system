# Mobile parking system

## Mobile Application
Mobile application you can find in `app` branch - [see here](https://github.com/andxeg/parking_system/tree/app)

![Screenshot02](/screenshots/mobile_app_screenshot.png?raw=true "Mobile app")

<!-- ![Animation](/screenshots/mobile_app.gif?raw=true) -->

## Mobile Application. Animation

<img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app.gif" width="340" height="660" />


## Mobile Application. Try it now!

1.	Install Expo application on Androind or iPhone [link](https://expo.io/)
2.	Scan QR code [here](https://expo.io/@danielbitesdog/projects/rostelekom-parkings) or see it below

![QRCode](/screenshots/qr_code_expo.png?raw=true "QR code expo")


## Model
Based on YOLOv5 [see here](https://github.com/ultralytics/yolov5).

Model weights you can find [here](https://github.com/andxeg/parking_system/tree/master/src/core/models)

![Screenshot02](/screenshots/recognition_example_01.jpg?raw=true "Recognition Example 1")

![Screenshot03](/screenshots/recognition_example_02.jpg?raw=true "Recognition Example 2")

## Backend
Backend you can find in `master` branch - [see here](https://github.com/andxeg/parking_system).

Backend contains 3 docker containers:
1. Web (Flask)
2. Worker for model (YOLOv5)
3. MySQL

Start and initilize database:
```bash
# start_test.sh
# init.sh
```

## Api description
You can find API description [here](http://167.99.136.99/api/rospark/ui/)

