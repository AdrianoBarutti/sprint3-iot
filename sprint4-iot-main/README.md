## 🚀 Projeto de Detecção e Análise de Motocicletas com YOLOv8

Este projeto é um conjunto de scripts de visão computacional em Python que utiliza o modelo de inteligência artificial **YOLOv8** para detectar, rastrear e analisar o estado de motocicletas em diferentes tipos de entrada (vídeo ou foto estática).

O sistema principal processa o conteúdo, desenhando caixas delimitadoras que mudam de cor e exibindo informações cruciais como ID de rastreamento e status.

***

## ✨ Funcionalidades e Scripts do Projeto

O projeto está dividido logicamente em dois modos de operação para lidar com diferentes tipos de entrada.

### 1. Modo VÍDEO (`detect_motos.py`)

* **Finalidade:** Análise em tempo real de vídeos ou *streams* de câmera.
* **Funcionalidades:**
    * **Rastreamento Persistente:** Utiliza o `BoT-SORT` para atribuir um **ID único** a cada moto.
    * **Detecção de Inatividade:** Analisa o histórico de posições da moto para determinar seu status: **"MOVENDO"** (Cor Verde) ou **"PARADA"** (Cor Vermelha).

### 2. Modo IMAGEM (`detect_motos_paradas.py`)

* **Finalidade:** Análise estática de fotos (`.jpg`, `.png`, etc.).
* **Funcionalidades:**
    * **Detecção Estática:** Realiza uma única detecção e atribui um ID sequencial simulado.
    * **Status Fixo (Simulado):** Todas as motocicletas detectadas recebem o status **"ESTACIONADA"** (Cor Vermelha), ideal para visualização de pátios.

***

## 🛠️ Requisitos

Certifique-se de que você tem o **Python 3.8 ou superior** instalado em sua máquina.

***

## 📦 Instalação

1.  **Clone ou baixe** este repositório.
2.  **Navegue** até o diretório do projeto no terminal.

3.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

4.  **Ative o ambiente virtual:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

5.  **Instale as bibliotecas necessárias:** (O NumPy é necessário para cálculos de distância na lógica de inatividade).
    ```bash
    pip install opencv-python ultralytics numpy
    ```

***

## ▶️ Como Usar

Para executar o projeto, você deve configurar o arquivo de entrada (`INPUT_PATH`) no script desejado e executá-lo.

### Opção 1: Análise de Vídeo (Modo Rastreamento)

1.  **Abra o arquivo `detect_motos.py`** e defina o nome do seu vídeo:
    ```python
    INPUT_PATH = 'motos.mp4' 
    ```

2.  **Execute:**
    ```bash
    python detect_motos.py
    ```
    *Para fechar, pressione **`q`**.*

### Opção 2: Análise de Imagem (Modo Estático)

1.  **Abra o arquivo `detect_motos_paradas.py`** e defina o nome da sua foto:
    ```python
    INPUT_PATH = 'minha_foto.jpg' 
    ```

2.  **Execute:**
    ```bash
    python detect_motos_paradas.py
    ```
    *Para fechar, pressione **qualquer tecla**.*

***

## 💻 Tecnologias Utilizadas

* **Python**: Linguagem de programação.
* **OpenCV**: Biblioteca de visão computacional.
* **Ultralytics YOLOv8**: Algoritmo de detecção de objetos e framework de rastreamento (BoT-SORT).
* **NumPy**: Necessário para cálculos matemáticos.