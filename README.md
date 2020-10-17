# Mobile parking system

## Mobile Application
Mobile application you can find in `app` branch - [see here](https://github.com/andxeg/parking_system/tree/app)


<p float="left">
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app_screenshot_01.jpg?raw=true" width="200" height="330" />
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app_screenshot_02.jpg?raw=true" width="200" height="330" />
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app_screenshot_03.jpg?raw=true" width="200" height="330" />
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app_screenshot_04.jpg?raw=true" width="200" height="330" />
</p>

## Mobile Application. Animation

<img src="https://github.com/andxeg/parking_system/blob/master/screenshots/mobile_app.gif" width="340" height="660" />


## Mobile Application. Try it now!

1.  Install Expo application on Androind or iPhone [link](https://expo.io/)
2.  Scan QR code [here](https://expo.io/@danielbitesdog/projects/rostelekom-parkings) or see it below

![QRCode](/screenshots/qr_code_expo.png?raw=true "QR code expo")


## Model
Based on YOLOv5 [see here](https://github.com/ultralytics/yolov5).

Model weights you can find [here](https://github.com/andxeg/parking_system/tree/master/src/core/models)


<p float="left">
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/recognition_example_01.jpg?raw=true" width="400" height="350" />
    <img src="https://github.com/andxeg/parking_system/blob/master/screenshots/recognition_example_02.jpg?raw=true" width="400" height="350" />
</p>

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

