import pandas as pd
import matplotlib.pyplot as plt
from DataTrainer import TrainModel

class DataPlotter():
    """Plots and saves the sensor anomolies of the provided df and sensors"""
    def plot_sensor_anomolies(self,df,sensor):
        anomoly_rows = df[df["Isolation Forest"] == -1]
        broken_rows = df[df['machine_status']=='BROKEN']
        recovery_rows = df[df['machine_status']=='RECOVERING']

        plt.figure(figsize=(25,3))
        plt.plot(df[sensor], color='grey')
        plt.plot(recovery_rows[sensor], linestyle='none', marker='o', color='yellow', markersize=5, label='recovering',alpha = 0.5)
        plt.plot(broken_rows[sensor], linestyle='none', marker='X', color='red', markersize=20, label='broken')
        plt.plot(anomoly_rows[sensor], linestyle='none', marker='X', color='blue', markersize=4, label='anomoly predicted', alpha = 0.1)
        plt.title(sensor)
        plt.legend()
        
        return plt            