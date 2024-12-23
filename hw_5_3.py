import argparse
import re

def parse_log_line(line):
  """Парсить рядок логу і повертає словник з інформацією."""
  pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
  match = re.match(pattern, line)
  if match:
    return {
      "timestamp": match.group(1),
      "level": match.group(2),
      "message": match.group(3)
    }
  return None

def load_logs(file_path: str) -> list:
  """Завантажує логи з файлу."""
  with open(file_path, 'r') as f:
    logs = []
    for line in f:
      parsed_log = parse_log_line(line.strip())
      if parsed_log:
        logs.append(parsed_log)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
  """Фільтрує логи за рівнем."""
  return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
  """Підраховує кількість записів за рівнем."""
  counts = {}
  for log in logs:
    counts[log['level']] = counts.get(log['level'], 0) + 1
  return counts

def display_log_counts(counts: dict):
  """Виводить статистику за рівнями логування."""
  print("Рівень логування | Кількість")
  print("-----------------|----------")
  for level, count in counts.items():
    print(f"{level:15} | {count}")

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("log_file", help="Path to the log file")
  parser.add_argument("-l", "--level", help="Filter logs by level")
  args = parser.parse_args()

  logs = load_logs(args.log_file)

  if args.level:
    filtered_logs = filter_logs_by_level(logs, args.level)
    print("Деталі логів для рівня '{}':".format(args.level))
    for log in filtered_logs:
      print(f"{log['timestamp']} - {log['message']}")
  else:
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
  main()