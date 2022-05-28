# ceaser cipher with arg parse 

from flask import Flask, request
from flask_restful import Api, Resource
from webargs.flaskparser import use_args
from webargs import fields
import ceasercipher


app = Flask(__name__)
api = Api(app)

# cipher_put_args = reqparse.RequestParser()
# cipher_put_args.add_argument("cipher", type=str, help="cipher text required", required=True)
# cipher_put_args.add_argument("rotation", type=int, help="number of rotation required", required=False)

class CCipher(Resource):
    def get(self,cipher,rotation):   
        kk=ceasercipher.ceaser(cipher,rotation)
        return {"cipher": kk,"rotation": rotation}
    
api.add_resource(CCipher,"/c/<string:cipher>/<int:rotation>")


@app.route("/greeting/<name>/")
@use_args({"name": fields.Str(required=True)}, location="view_args")
def greeting(args, **kwargs):
    return "Hello {}".format(args["name"])


if __name__ == "__main__":
    app.run(debug=True)