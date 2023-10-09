import time
import subprocess
from abc import ABC


class BaseScheduler:
    def __init__(self, interval_minutes):
        self.interval_minutes = interval_minutes

    def task(self):
        """
        Определите свою задачу здесь. Переопределите этот метод в подклассах.
        """
        raise NotImplementedError("Please implement the 'task' method in the subclass.")

    def run(self):
        while True:
            self.task()
            time.sleep(self.interval_minutes * 60)


class WindowsScheduler(BaseScheduler):
    def __init__(self, interval_minutes, task_name, executable_path):
        super().__init__(interval_minutes)
        self.task_name = task_name
        self.executable_path = executable_path

    def _run_command(self, cmd):
        try:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")
            return None

    def task_exists(self):
        cmd = f'schtasks /Query /TN {self.task_name}'
        output = self._run_command(cmd)
        return self.task_name in output if output else False

    def setup_task(self):
        if not self.task_exists():
            cmd = f'schtasks /Create /SC MINUTE /MO {self.interval_minutes} /TN {self.task_name} /TR {self.executable_path}'
            self._run_command(cmd)
            print(f"Task '{self.task_name}' created successfully.")
        else:
            print(f"Task '{self.task_name}' already exists.")

    def delete_task(self):
        if self.task_exists():
            cmd = f'schtasks /Delete /TN {self.task_name} /F'
            self._run_command(cmd)
            print(f"Task '{self.task_name}' deleted successfully.")
        else:
            print(f"Task '{self.task_name}' doesn't exist.")


class UnixScheduler(BaseScheduler):
    def __init__(self, interval_minutes, task_name, executable_path):
        super().__init__(interval_minutes)
        self.task_name = task_name
        self.executable_path = executable_path
        self.cron_line = f"*/{self.interval_minutes} * * * * {self.executable_path} # {self.task_name}\n"

    def _run_command(self, cmd):
        try:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")
            return None

    def task_exists(self):
        cmd = f'crontab -l | grep "{self.task_name}"'
        output = self._run_command(cmd)
        return self.task_name in output if output else False

    def setup_task(self):
        if not self.task_exists():
            cmd = f'(crontab -l 2>/dev/null; echo "{self.cron_line}") | crontab -'
            self._run_command(cmd)
            print(f"Task '{self.task_name}' added to cron.")
        else:
            print(f"Task '{self.task_name}' already exists in cron.")

    def delete_task(self):
        if self.task_exists():
            cmd = f'crontab -l | grep -v "{self.task_name}" | crontab -'
            self._run_command(cmd)
            print(f"Task '{self.task_name}' removed from cron.")
        else:
            print(f"Task '{self.task_name}' doesn't exist in cron.")

