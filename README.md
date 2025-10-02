LINK VIDEO YOUTUBE:https://youtu.be/YuiJEdLCiOo



Projeto de Detecção de Motos com YOLOv8
Este projeto é um script de visão computacional em Python que utiliza o modelo de inteligência artificial YOLOv8 para detectar e rastrear motos em um stream de vídeo. O sistema processa frames em tempo real, desenhando caixas delimitadoras e exibindo o índice de confiança para cada detecção.

Requisitos
Certifique-se de que você tem o Python 3.8 ou superior instalado em sua máquina.

Instalação
Clone ou baixe este repositório.

Navegue até o diretório do projeto no terminal.

Crie um ambiente virtual (recomendado):

Bash

python -m venv venv
Ative o ambiente virtual:

Windows: .\venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Instale as bibliotecas necessárias:

Bash

pip install opencv-python ultralytics
Como Usar
Para executar o script, você precisa de um arquivo de vídeo. Certifique-se de que o seu vídeo (por exemplo, motos.mp4) está na mesma pasta que o script detect_motos.py.

Execute o seguinte comando no terminal (com o ambiente virtual ativado):

Bash

python detect_motos.py
O script abrirá uma janela exibindo o vídeo com as detecções em tempo real.

Para fechar a janela, pressione a tecla q no teclado.

Estrutura do Projeto
detect_motos.py: O script principal que realiza a detecção de objetos.

motos.mp4: Arquivo de vídeo de entrada para a detecção.

yolov8n.pt: O modelo pré-treinado do YOLOv8, baixado automaticamente na primeira execução.

venv/: Pasta do ambiente virtual.

Tecnologias Utilizadas
Python: Linguagem de programação.

OpenCV: Biblioteca de visão computacional.

Ultralytics YOLOv8: Algoritmo de detecção de objetos.
