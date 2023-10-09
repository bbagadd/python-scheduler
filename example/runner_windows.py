from scheduler import WindowsScheduler

if __name__ == "__main__":
    scheduler = WindowsScheduler(10, "MyScheduledTask", "C:\\path\\to\\python.exe C:\\path\\to\\script.py")
    scheduler.setup_task()
