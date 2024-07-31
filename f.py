import cv2
import numpy as np

# Charger l'image
image = cv2.imread('chemin/vers/votre/image.jpg')

# Charger le modèle pré-entraîné pour la détection d'objets (par exemple, MobileNet SSD)
net = cv2.dnn.readNetFromTensorflow('chemin/vers/le/modele.pb', 'chemin/vers/le/fichier/config.pbtxt')

# Prétraiter l'image pour l'entrée du modèle
blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

# Définir l'entrée du réseau
net.setInput(blob)

# Obtenir les détections
detections = net.forward()

# Parcourir les détections et afficher les résultats
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.5:  # Seuil de confiance
        class_id = int(detections[0, 0, i, 1])
        class_name = 'Nom_de_la_classe'  # Remplacez par le nom de la classe correspondante à l'ID
        box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
        (startX, startY, endX, endY) = box.astype('int')

        # Dessiner la boîte et afficher le nom de la classe et la confiance
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        label = f'{class_name}: {confidence:.2f}'
        cv2.putText(image, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Afficher l'image avec les détections
cv2.imshow('Detection d\'objets', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
