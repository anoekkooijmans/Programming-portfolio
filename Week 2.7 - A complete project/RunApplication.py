
from DataLoader import DataLoader
from DataPreprocessor import DataPreprocessor
from DataTrainer import TrainModel
from DataListener import DataListener

class RunApplication:
    """
    Loads provided .csv file and extracts the training data, which is pre-processed and then used to train the machine learning model.
    Once model is trained, the application listens for new data, and processes and fits this once it is found. 
    """
    def run(self,filename,config):
        print("Splitting data into training and testing set")
        loader = DataLoader(filename,config) # Load data
        train_data = loader.train_data # Get training data
    
        print("Pre-processing data")
        ppr = DataPreprocessor()
        X = ppr.process_data(train_data) # Preprocess data
        
        print("Training model")
        trainer = TrainModel(config)
        
        df = trainer.predict(train_data, X) # Train model
        
        print("Listening for new data")
        listener = DataListener(config) # Listen for new data
        listener.listen()   