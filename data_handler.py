import pandas as pd
import json


class DataLoader:
    def __init__(self, path):
        with open(path, 'r') as file:
            self.lines = file.readlines()

        json_line = []

        for line in self.lines:
            json_line.append(json.loads(line))

        self.data = pd.DataFrame(json_line)

    def get_column(self, column):
        return self.data[column].tolist()

