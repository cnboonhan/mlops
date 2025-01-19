from flask import Flask, request, send_file
from ultralytics import YOLO
import os

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)
model = YOLO("best.pt")


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return "No file part", 400
    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    if file:
        filename = os.path.join("uploads", "image.jpg")
        file.save(filename)
        results = model(
            "uploads/image.jpg",
            save=True,
            show_boxes=True,
            exist_ok=True,
        )
        return send_file(f"{results[0].save_dir}/image.jpg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(port=8000)
results = model(
    "uploads/image.jpg",
    save=True,
    show_boxes=True,
    exist_ok=True,
)
