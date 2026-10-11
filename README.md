# vision-playground

Real-time face detection from a webcam: the program reads the video stream, finds faces in every frame and draws a box around each one.

## What it does

- Opens the webcam and shows a mirrored live preview
- Detects faces in every frame with the YuNet neural network
- Draws a green bounding box around each face
- Quits when you press `q`

## Built with

- Python 3.12
- [OpenCV](https://opencv.org/) 5 for camera access, drawing and running the model
- [YuNet](https://github.com/opencv/opencv_zoo/tree/main/models/face_detection_yunet) face detection model
- [uv](https://docs.astral.sh/uv/) for dependencies and the virtual environment

## How to run

You need a webcam and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

```
git clone https://github.com/CatherineSalenko/vision-playground.git
cd vision-playground
uv sync
uv run python src/vision_playground/camera.py
```

Run the last command from the project root, because the path to the model is relative to it.

On macOS the first run asks for camera access for your terminal. Allow it and start the program again.

Tested on macOS with Apple Silicon only.

## How it works

Each frame from the camera is a grid of pixels, 1280 by 720. The program flips it horizontally, so the preview behaves like a mirror, and passes it to the detector. For every face the detector returns a row of 15 numbers: the box (x, y, width, height), five landmark points (eyes, nose, mouth corners) and a confidence score. The first four numbers are used to draw the box.

The whole program is one file: [src/vision_playground/camera.py](src/vision_playground/camera.py).

## Roadmap

- [x] Live video from the webcam
- [x] Face detection with bounding boxes
- [ ] Object detection (people, cups, phones and other everyday things)
- [ ] Face recognition: telling whose face it is, using only my own face as a sample

## Credits

The face detection model `models/face_detection_yunet_2023mar.onnx` comes from the [OpenCV Zoo](https://github.com/opencv/opencv_zoo) and is distributed under the MIT license.

## License

[MIT](LICENSE)
