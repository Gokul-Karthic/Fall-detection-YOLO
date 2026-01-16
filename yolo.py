import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture(0)

CONFIRM_FRAMES = 4
fall_counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4)
    fall_detected = False

    for r in results:
        if r.keypoints is None:
            continue

        kps = r.keypoints.xy.cpu().numpy()

        for kp in kps:
            if len(kp) < 17:
                continue

            head = kp[0]
            left_hip = kp[11]
            right_hip = kp[12]

            # Skip if keypoints missing
            if np.any(head == 0) or np.any(left_hip == 0) or np.any(right_hip == 0):
                continue

            hip_center = (left_hip + right_hip) / 2

            dx = abs(head[0] - hip_center[0])
            dy = abs(head[1] - hip_center[1])

            # Horizontal body check
            horizontal_body = dx > dy

            if horizontal_body:
                fall_counter += 1
            else:
                fall_counter = max(0, fall_counter - 1)

            if fall_counter >= CONFIRM_FRAMES:
                fall_detected = True

            # Draw skeleton
            for p in kp:
                cv2.circle(frame, tuple(p.astype(int)), 3, (0, 255, 0), -1)

            cv2.circle(frame, tuple(hip_center.astype(int)), 6, (255, 0, 0), -1)
            cv2.circle(frame, tuple(head.astype(int)), 6, (0, 0, 255), -1)

            if fall_detected:
                cv2.putText(frame, "FALL DETECTED!", (40, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow("YOLOv8 Pose Fall Detection (FIXED)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
