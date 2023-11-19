from flask import Flask, json, request, jsonify
import os
# import urlib.request import urlopen
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from CBIR_texture import compare_and_write_results, dataset_to_json, cbir_dataset
from models import db, Image


app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

db.init_app(app)

with app.app_context():
    db.create_all()

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt,''pdf','png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

ma=Marshmallow(app)

class ImageSchema(ma.Schema):
    class Meta:
        fields = ('id','title')

image_schema =ImageSchema(many=True)

@app.route("/")
def hello_world():
    return "<p> test!</p>"

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({
            "message": 'No file part in the request',
            "status": 'failed'
        })
        resp.status_code = 400
        return resp
    
    files = request.files.getlist('files[]')

    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
            newFile = Image(title=filename)
            db.session.add(newFile)
            db.session.commit()

            success = True
        else:
            resp = jsonify({
                "message": 'Files successfully uploaded',
                "status": 'success'
            })
            return resp
    
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        errors['status'] = 'failed'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'successs'
        })
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

@app.route('/images', methods=['GET'])
def images():
    all_images = Image.query.all()
    results = image_schema.dump(all_images)
    return jsonify(results)

@app.route('/similarImages', methods=['POST'])
def similarImages():
    target_folder_path = "static\\uploads"
    dataset_to_json(cbir_dataset(target_folder_path))
    dataset = "dataset_vektor.json"
    image_path = "static\\uploads\\0.jpg"
    compare_and_write_results(image_path,dataset)

# if __name__ == "__main__":
#     app.run(debug=True)