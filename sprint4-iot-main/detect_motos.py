import cv2
from ultralytics import YOLO

# 1. Inicialização do Modelo YOLO com capacidade de Rastreamento
model = YOLO('yolov8n.pt')

# --- Variáveis de Rastreamento e Inatividade ---
pos_history = {} 
INACTIVITY_THRESHOLD = 30  # Frames para considerar a moto como parada (ex: 1 segundo em 30 FPS)
MOVEMENT_THRESHOLD = 5     # Distância máxima em pixels para considerar a moto parada

# --- Configuração de Entrada ---
INPUT_PATH = 'motos.mp4'  # Defina o caminho para o seu arquivo de vídeo
# -------------------------------

# Inicia a captura de vídeo
cap = cv2.VideoCapture(INPUT_PATH) 

if not cap.isOpened():
    print(f"Erro: Não foi possível abrir o vídeo em: {INPUT_PATH}")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro na leitura.")
        break

    # 2. Rastreamento de Objetos (necessário para ID persistente e detecção de inatividade)
    results = model.track(frame, persist=True, tracker="botsort.yaml", verbose=False)
    
    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            class_name = r.names[class_id]
            
            # Processa apenas motocicletas e verifica se há um ID de rastreamento
            if class_name == 'motorcycle' and box.id is not None:
                track_id = int(box.id[0])
                confidence = float(box.conf[0])
                
                # Coordenadas da caixa delimitadora
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # Ponto de referência para a análise de movimento (centro inferior)
                x_center = (x1 + x2) / 2
                y_base = y2
                current_pos = (x_center, y_base)
                
                
                # --- Lógica de Análise de Inatividade (PARADA vs MOVENDO) ---
                if track_id not in pos_history:
                    pos_history[track_id] = {'positions': [current_pos], 'stopped_count': 0}
                else:
                    pos_history[track_id]['positions'].append(current_pos)
                    # Mantém o histórico com o número de frames definido
                    if len(pos_history[track_id]['positions']) > INACTIVITY_THRESHOLD:
                        pos_history[track_id]['positions'].pop(0)

                is_stopped = False
                
                if len(pos_history[track_id]['positions']) == INACTIVITY_THRESHOLD:
                    initial_pos = pos_history[track_id]['positions'][0]
                    # Calcula a distância euclidiana percorrida
                    distance_moved = ((current_pos[0] - initial_pos[0])**2 + (current_pos[1] - initial_pos[1])**2)**0.5
                    
                    if distance_moved < MOVEMENT_THRESHOLD:
                        is_stopped = True
                        pos_history[track_id]['stopped_count'] += 1
                    else:
                        pos_history[track_id]['stopped_count'] = 0 
                
                # 3. Definir cor e rótulo com base no estado de inatividade
                color = (0, 255, 0) # Verde: Movendo
                status_text = "MOVENDO"
                
                if pos_history[track_id]['stopped_count'] >= INACTIVITY_THRESHOLD:
                    color = (0, 0, 255) # Vermelho: Parada
                    status_text = "PARADA"
                
                label = f"ID {track_id}: {status_text} ({confidence:.2f})"
                
                # Desenhar a caixa e o rótulo no frame original
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Exibe SOMENTE a janela da câmera
    cv2.imshow('Detecao de Motos (Camera)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()