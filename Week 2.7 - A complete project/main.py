from RunApplication import RunApplication

if __name__ == "__main__":
    app_runner = RunApplication()
    app_runner.run(filename = "sensor.csv", config = "application.json")