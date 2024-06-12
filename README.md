<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Tolerance Adjustment using HSV</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            font-size: 28px;
            color: #333;
            border-bottom: 2px solid #ccc;
            padding-bottom: 5px;
        }
        h2 {
            font-size: 24px;
            color: #555;
            margin-top: 20px;
        }
        p {
            font-size: 16px;
            color: #666;
        }
        code {
            font-family: Consolas, monospace;
            font-size: 14px;
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Image Tolerance Adjustment using HSV</h1>
    
    <p style="text-align: center;"><strong>Deus é fiel.</strong></p>

    <h2>Clone the Repository:</h2>
    <code>git clone https://github.com/mateus1010mateus/meus-projetos-python.git</code>

    <h2>Explicação do Código em Português</h2>
    <p>Este código em Python utiliza a biblioteca OpenCV para permitir ajustes interativos nos valores de HSV (Matiz, Saturação, Valor) e na tolerância de uma imagem. Através de barras deslizantes (trackbars), você pode ajustar esses parâmetros e visualizar os efeitos na imagem em tempo real.</p>

    <h3>Funcionamento do Código:</h3>
    <ol>
        <li><strong>Carregamento da Imagem:</strong> A imagem é carregada utilizando o OpenCV.</li>
        <li><strong>Conversão para HSV:</strong> A imagem é convertida do espaço de cores RGB para HSV, facilitando o processamento baseado em cores.</li>
        <li><strong>Criação da Janela:</strong> Uma janela é criada para exibir a imagem original e a imagem resultante após aplicar a máscara com base nos valores de HSV e tolerância.</li>
        <li><strong>Ajuste Interativo:</strong> São criadas trackbars para ajustar os valores de H, S, V (HSV) e tolerância (variação permitida nos valores de HSV).</li>
        <li><strong>Atualização da Imagem:</strong> A função <code>atualizar_imagem()</code> é chamada sempre que os valores são ajustados nas trackbars, recalculando a máscara e exibindo a imagem resultante.</li>
        <li><strong>Finalização:</strong> O loop continua até que a tecla 's' seja pressionada, encerrando o ajuste interativo.</li>
        <li><strong>Cálculo da Tolerância Média:</strong> Após a interação, a função <code>calcular_tolerancia_media()</code> é utilizada para determinar a média da tolerância ajustada.</li>
        <li><strong>Exibição dos Resultados:</strong> Os valores finais de HSV e a tolerância média são exibidos.</li>
    </ol>

    <h2>Code Explanation in English</h2>
    <p>This Python code utilizes the OpenCV library to allow interactive adjustments of HSV (Hue, Saturation, Value) values and tolerance for an image. Using trackbars, you can adjust these parameters and visualize their effects on the image in real-time.</p>

    <h3>How the Code Works:</h3>
    <ol>
        <li><strong>Image Loading:</strong> The image is loaded using OpenCV.</li>
        <li><strong>Conversion to HSV:</strong> The image is converted from RGB color space to HSV, making color-based processing easier.</li>
        <li><strong>Window Creation:</strong> A window is created to display the original image and the resulting image after applying the mask based on HSV values and tolerance.</li>
        <li><strong>Interactive Adjustment:</strong> Trackbars are created to adjust the H, S, V (HSV) values and tolerance (allowed variation in HSV values).</li>
        <li><strong>Image Update:</strong> The <code>update_image()</code> function is called whenever values are adjusted on the trackbars, recalculating the mask and displaying the resulting image.</li>
        <li><strong>Completion:</strong> The loop continues until the 's' key is pressed, ending the interactive adjustment.</li>
        <li><strong>Calculation of Average Tolerance:</strong> After interaction, the <code>calculate_average_tolerance()</code> function is used to determine the average of the adjusted tolerance.</li>
        <li><strong>Display of Results:</strong> The final HSV values and the average tolerance are displayed.</li>
    </ol>
</body>
</html>
