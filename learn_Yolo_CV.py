from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

results = model("https://ultralytics.com/images/bus.jpg")

detected_image = results[0].plot()

cv2.imshow("Hasil deteksi YOLO: ", detected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Hasil deteksi.jpg", detected_image)
