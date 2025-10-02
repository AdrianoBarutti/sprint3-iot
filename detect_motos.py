import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')


cap = cv2.VideoCapture('motos.mp4') 

if not cap.isOpened():
    print("Erro: Não foi possível abrir o vídeo. O arquivo está na pasta e o nome está correto?")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro na leitura.")
        break

    results = model(frame, verbose=False)

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = r.names[class_id]

            if class_name == 'motorcycle':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Detecao de Motos', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()