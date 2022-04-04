import  cv2.cv2 as cv2

class Model:
    def __init__(self,path):
        self.path = path

    def Load_model(self):
        self.model = cv2.ml.ANN_MLP_load(self.path)

    def predict(self, X):
        resp = None
        try:
            ret, resp = self.model.predict(X)
        except Exception as e:
            print(e)
        return resp.argmax(-1)