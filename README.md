
# Python Scheduler Classes

Данный набор классов позволяет упростить процесс планирования и запуска скриптов на различных платформах.

## Основной класс: `BaseScheduler`

Этот класс предоставляет базовую структуру для создания планировщиков. Он не предназначен для прямого использования, но может быть расширен для создания специфических планировщиков для различных систем.

## Класс для Windows: `WindowsScheduler`

Данный класс предназначен для создания и удаления запланированных задач в системе Windows с использованием утилиты `schtasks`.

Пример использования:

```python
scheduler = WindowsScheduler(10, "MyScheduledTask", "C:\path\to\your\script.bat")
scheduler.setup_task()  # Создать задачу
scheduler.delete_task()  # Удалить задачу
```

## Класс для Unix: `UnixScheduler`

Этот класс позволяет добавлять и удалять задачи из `cron` в Unix-подобных системах.

Пример использования:

```python
scheduler = UnixScheduler(10, "MyCronJob", "/path/to/your/script.sh")
scheduler.setup_task()  # Добавить задачу в cron
scheduler.delete_task()  # Удалить задачу из cron
```

## Установка и требования

1. Убедитесь, что у вас установлен Python 3.x.
2. Для использования `WindowsScheduler` требуется утилита `schtasks`, включенная в состав Windows.
3. Для использования `UnixScheduler` у вас должны быть права на добавление задач в `cron`.
