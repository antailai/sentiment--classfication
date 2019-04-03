class knn:
    def __init__(self, train_data, k):
        if train_data is not None:
            self.data = train_data
        return

    def set_k(self, k):
        self.k = k

    def __normalize(self):
        max(self.data)
