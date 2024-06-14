import cv2
import serial as serial


webcam = cv2.VideoCapture(1) #int: 0 - webcam pc; 1 - webcam adicional.

if webcam.isOpened():
    validacao, frame = webcam.read() #devolve em booleano se a câmera está conectada
    #webcam.read() devolve a informação em booleano se a informação está sendo lida, armazenando em validacao, e um array de frames (print) em lista RGB, armazenado em frame
    img_counter = 0  # Inicialize o contador
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        key = cv2.waitKey(5)  # as imagens estão sendo processadas rapidamente, o que impede a visualização do vídeo. Vamos adicionar uma variável "key", que faz a imagem aguardar (milissegundos) e ainda armazena as teclas pressionadas durante o vídeo.
        if key == 112:  # p minúsculo
            img_name = "Frame_{}.png".format(img_counter)  # Crie um nome de arquivo único
            cv2.imwrite(img_name, frame)  # Salve o frame com o novo nome de arquivo
            img_counter += 1  # Incremente o contador
        if key == 27:  # ESC
            break

webcam.release()
cv2.destroyAllWindows()