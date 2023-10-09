from scheduler import UnixScheduler

if __name__ == "__main__":
    scheduler = UnixScheduler(10, "MyCronJob", "/bin/python script.py")
    scheduler.setup_task()
