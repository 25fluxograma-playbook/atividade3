import cv2
import matplotlib.pyplot as plt
import os

# 1. Lista com os nomes exatos dos seus arquivos de imagem
# Certifique-se de que estão na mesma pasta que este script
nomes_arquivos = ['imagem01.jpeg', 'imagem02.jpeg', 'imagem03.jpeg', 'imagem04.jpeg']

# 2. Loop para processar e gerar uma figura para CADA imagem
for i, nome in enumerate(nomes_arquivos):
    # Verificar se o arquivo existe para não dar erro
    if not os.path.exists(nome):
        print(f"Erro: O arquivo {nome} não foi encontrado.")
        continue

    # A. Carregar e preparar a imagem
    img_bgr = cv2.imread(nome)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # Converter para RGB para o Matplotlib

    # B. Aplicar o Método Próprio/Pré-processamento (Blur/Desfoque)
    # Suaviza a imagem para reduzir o ruído
    img_blur = cv2.GaussianBlur(img_rgb, (15, 15), 0)

    # C. Aplicar o Método da Literatura (Detecção de Linhas/Bordas com Canny)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) # Canny precisa de escala de cinza
    img_edges = cv2.Canny(img_gray, 50, 150) # Ajuste os limiares se necessário

    # 3. Criar a Figura com layout LADO A LADO na HORIZONTAL (1 linha, 3 colunas)
    fig, ax = plt.subplots(1, 3, figsize=(18, 6)) # figsize maior na largura
    
    # Título principal da figura com o número da imagem
    fig.suptitle(f'Processamento da Imagem {i+1} ({nome})', fontsize=16, fontweight='bold')

    # Exibir Original (Coluna 1)
    ax[0].imshow(img_rgb)
    ax[0].set_title('1. Original', fontsize=14)
    ax[0].axis('off') # Remove os eixos (números)

    # Exibir Blur (Coluna 2)
    ax[1].imshow(img_blur)
    ax[1].set_title('2. Pré-processamento: Blur (Suavização)', fontsize=14)
    ax[1].axis('off')

    # Exibir Linhas (Coluna 3)
    ax[2].imshow(img_edges, cmap='gray') # Exibir em tons de cinza
    ax[2].set_title('3. Literatura: Detecção de Linhas (Canny)', fontsize=14)
    ax[2].axis('off')

    # Adicionar a fonte embaixo de toda a figura
    fig.text(0.5, 0.02, 'Fonte: Imagens da Internet', ha='center', fontsize=12, style='italic')

    # Ajustar layout para não cortar os títulos e a fonte
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    
    # Exibir a figura atual e esperar o usuário fechar para mostrar a próxima
    plt.show()

# Mensagem final para o terminal
print("\nProcessamento concluído. Verifique as figuras geradas.")