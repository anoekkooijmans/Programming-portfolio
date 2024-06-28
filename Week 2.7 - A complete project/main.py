from DataLoader import DataLoader

if __name__ == "__main__":
    # Replace 'your_data.csv' with the actual path to your CSV file
    data_loader = DataLoader('sensor.csv')
    print("Training data shape:", data_loader.train_data.shape)
    print("Testing data shape:", data_loader.test_data.shape)