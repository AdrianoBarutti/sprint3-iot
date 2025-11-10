import cv2
from ultralytics import YOLO

# 1. Inicialização do Modelo YOLO
model = YOLO('yolov8n.pt')

# --- Configuração de Entrada ---
IMAGE_PATH = 'motosparada.jpg' 
# -------------------------------

# 1. Carrega a imagem
frame = cv2.imread(IMAGE_PATH) 

if frame is None:
    print(f"Erro: Não foi possível carregar a imagem em: {IMAGE_PATH}. Verifique o caminho e o nome.")
    exit()

# 2. Detecção de Objetos (Modo 'predict' para imagens estáticas)
results = model(frame, verbose=False)

# 3. Processar e Desenhar as Detecções
simulated_id = 1 # ID sequencial simulado para motos

for r in results:
    for box in r.boxes:
        class_id = int(box.cls[0])
        class_name = r.names[class_id]
        
        # --- FILTRO: Foca APENAS na Motocicleta ---
        if class_name == 'motorcycle':
            confidence = float(box.conf[0])
            
            # Coordenadas da caixa delimitadora
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # --- Status e Rótulo (SIMULANDO "PARADA" para FOTO) ---
            status_text = "ESTACIONADA" 
            color = (0, 0, 255) # Vermelho
            
            
            # Cria o rótulo com o ID simulado
            label = f"MOTO ID {simulated_id}: {status_text} ({confidence:.2f})"
            simulated_id += 1 
            
            # Desenhar a caixa e o rótulo no frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)


# 4. Exibir a imagem resultante
cv2.imshow('Detecao de Motos Estacionadas', frame)
print(f"Análise de imagem concluída: {IMAGE_PATH}. Pressione qualquer tecla para fechar.")

# Espera indefinidamente até uma tecla ser pressionada
cv2.waitKey(0) 
cv2.destroyAllWindows()