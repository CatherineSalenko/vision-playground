import cv2


cap = cv2.VideoCapture(0)
detector = cv2.FaceDetectorYN.create(
    "models/face_detection_yunet_2023mar.onnx",
    "",
    (1280, 720),
)
while True:
    ok, frame = cap.read()
    if frame is None:
        break

    frame = cv2.flip(frame, 1)
    _, faces = detector.detect(frame)
    if faces is not None:
        for face in faces:
            x, y, w, h = face[:4].astype(int)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()





