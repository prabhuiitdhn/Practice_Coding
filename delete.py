class MLModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"MLModel(name={self.name}, version={self.version})"

model = MLModel("Random Forest", "2.0")
print(model)  # Output: MLModel(name=Random Forest, version=2.0)
print(repr(model))