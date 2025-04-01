import subprocess
from collections import defaultdict
import datetime
import re


def parse_processes():
    # Запускаем команду ps aux и получаем её вывод
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    # Пропускаем заголовок
    processes = lines[1:]

    # Инициализируем структуры для сбора данных
    users = set()
    user_process_count = defaultdict(int)
    total_memory = 0.0
    total_cpu = 0.0
    max_memory_process = ('', 0.0)
    max_cpu_process = ('', 0.0)

    # Регулярное выражение для разделения строки (учитывает множественные пробелы)
    pattern = re.compile(r'\s+')

    for line in processes:
        parts = pattern.split(line)
        if len(parts) < 11:
            continue

        user = parts[0]
        cpu = float(parts[2])
        memory = float(parts[3])
        command = ' '.join(parts[10:])

        # Обновляем данные
        users.add(user)
        user_process_count[user] += 1
        total_memory += memory
        total_cpu += cpu

        # Проверяем на максимальное использование памяти
        if memory > max_memory_process[1]:
            max_memory_process = (command[:20], memory)

        # Проверяем на максимальное использование CPU
        if cpu > max_cpu_process[1]:
            max_cpu_process = (command[:20], cpu)

    # Формируем отчет
    report = []
    report.append("Отчёт о состоянии системы:")
    report.append(f"Пользователи системы: {', '.join(sorted(users))}")
    report.append(f"Процессов запущено: {len(processes)}")
    report.append("\nПользовательских процессов:")
    for user, count in sorted(user_process_count.items()):
        report.append(f"{user}: {count}")

    report.append(f"\nВсего памяти используется: {total_memory:.1f}%")
    report.append(f"Всего CPU используется: {total_cpu:.1f}%")
    report.append(f"Больше всего памяти использует: {max_memory_process[0]} ({max_memory_process[1]:.1f}%)")
    report.append(f"Больше всего CPU использует: {max_cpu_process[0]} ({max_cpu_process[1]:.1f}%)")

    # Выводим отчет в консоль
    print('\n'.join(report))

    # Сохраняем отчет в файл
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M")
    filename = f"{timestamp}-scan.txt"
    with open(filename, 'w') as f:
        f.write('\n'.join(report))

    print(f"\nОтчёт сохранён в файл: {filename}")


if __name__ == "__main__":
    parse_processes()