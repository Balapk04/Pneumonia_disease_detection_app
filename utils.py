# utils.py
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models

CLASS_NAMES = ['Bacterial Pneumonia', 'Normal', 'Pneumonia', 'Viral Pneumonia']

def load_model(model_path):
    model = models.densenet121(weights=None)
    num_ftrs = model.classifier.in_features
    model.classifier = nn.Linear(num_ftrs, len(CLASS_NAMES))
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def predict_image(image, model):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485], [0.229])
    ])
    image = transform(image).unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        confidence = torch.nn.functional.softmax(outputs, dim=1)[0][predicted].item()
        return CLASS_NAMES[predicted], confidence
