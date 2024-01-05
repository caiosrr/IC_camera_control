import cv2

webcam = cv2.VideoCapture(1) #int: 0 - webcam pc; 1 - webcam adicional.

if webcam.isOpened():
    validacao, frame = webcam.read()
    # webcam.read() devolve a informação em booleano se a câmera esta conectada, armazenando em validacao, e um array de frames (print) em lista RGB, armazenado em frame
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Vide da Webcam", frame)
        # as imagens estão sendo processadas rapidamente, o que impede a visualização do vídeo. Vamos adicionar uma variável "key", que faz a imagem aguardar (milissegundos) e ainda armazena as teclas pressionadas durante o vídeo.
        key = cv2.waitKey(5)
        if key == 27: #ESC
            break
    cv2.imwrite("Frame.png", frame) #comando iwrite salva um frame, no local que esta sendo usado criará um arquivo png com o último frame registrado no vídeo.                   

webcam.release()
cv2.destroyAllWindows() #comandos para fechar a execução da webcam