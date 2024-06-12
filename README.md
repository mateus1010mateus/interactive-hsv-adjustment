# Deus é fiel

## Clone o Repositório

```bash
git clone https://github.com/mateus1010mateus/meus-projetos-python.git

Explicação do Código em Português
Este código em Python utiliza a biblioteca OpenCV para permitir ajustes interativos nos valores de HSV (Matiz, Saturação, Valor) e na tolerância de uma imagem. Através de barras deslizantes (trackbars), você pode ajustar esses parâmetros e visualizar os efeitos na imagem em tempo real.

Funcionamento do Código
Carregamento da Imagem: A imagem é carregada utilizando o OpenCV.
Conversão para HSV: A imagem é convertida do espaço de cores RGB para HSV, facilitando o processamento baseado em cores.
Criação da Janela: Uma janela é criada para exibir a imagem original e a imagem resultante após aplicar a máscara com base nos valores de HSV e tolerância.
Ajuste Interativo: São criadas trackbars para ajustar os valores de H, S, V (HSV) e tolerância (variação permitida nos valores de HSV).
Atualização da Imagem: A função atualizar_imagem() é chamada sempre que os valores são ajustados nas trackbars, recalculando a máscara e exibindo a imagem resultante.
Finalização: O loop continua até que a tecla 's' seja pressionada, encerrando o ajuste interativo.
Cálculo da Tolerância Média: Após a interação, a função calcular_tolerancia_media() é utilizada para determinar a média da tolerância ajustada.
Exibição dos Resultados: Os valores finais de HSV e a tolerância média são exibidos.
Code Explanation in English
This Python code utilizes the OpenCV library to allow interactive adjustments of HSV (Hue, Saturation, Value) values and tolerance for an image. Using trackbars, you can adjust these parameters and visualize their effects on the image in real-time.

How the Code Works
Image Loading: The image is loaded using OpenCV.
Conversion to HSV: The image is converted from RGB color space to HSV, making color-based processing easier.
Window Creation: A window is created to display the original image and the resulting image after applying the mask based on HSV values and tolerance.
Interactive Adjustment: Trackbars are created to adjust the H, S, V (HSV) values and tolerance (allowed variation in HSV values).
Image Update: The update_image() function is called whenever values are adjusted on the trackbars, recalculating the mask and displaying the resulting image.
Completion: The loop continues until the 's' key is pressed, ending the interactive adjustment.
Calculation of Average Tolerance: After interaction, the calculate_average_tolerance() function is used to determine the average of the adjusted tolerance.
Display of Results: The final HSV values and the average tolerance are displayed
