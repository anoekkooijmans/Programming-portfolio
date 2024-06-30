from DataPlotter import DataPlotter

if __name__ == "__main__":
    data_plotter = DataPlotter("Data/sensor.csv")
    plt = data_plotter.plot_sensor_anomolies(sensor="sensor_04")
    
