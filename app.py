from flask import Flask, render_template, request, redirect, url_for
import io
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
import torch

app = Flask(__name__)

# تحميل نموذج مدرب على ImageNet
model = models.mobilenet_v2(pretrained=True)
model.eval()

# فئات ImageNet التي تمثل الكلاب والقطط (نطاقات)
DOG_INDICES = list(range(151, 269))   # 151..268
CAT_INDICES = list(range(281, 286))   # 281..285

# التحويلات للصورة
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def predict_image(img_pil):
    input_tensor = preprocess(img_pil).unsqueeze(0)  # batch dimension
    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)
        top_prob, top_idx = torch.max(probs, dim=0)
        idx = int(top_idx.item())
        prob = float(top_prob.item())
        if idx in DOG_INDICES:
            label = "Dog"
        elif idx in CAT_INDICES:
            label = "Cat"
        else:
            label = "Other"
        return label, idx, prob

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        if 'file' not in request.files:
            result = ("Error", -1, 0.0)
        else:
            file = request.files['file']
            if file.filename == "":
                result = ("Error", -1, 0.0)
            else:
                img = Image.open(io.BytesIO(file.read())).convert("RGB")
                label, idx, prob = predict_image(img)
                result = (label, idx, prob)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
