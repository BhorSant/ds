import os 
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        # split the data
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False, header=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False, header=False)

        logger.info(f"Data splitted in {self.config.root_dir}")
        logger.info(f"Train: {os.path.join(self.config.root_dir, 'train.csv')}")
        logger.info(f"Test: {os.path.join(self.config.root_dir, 'test.csv')}")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)