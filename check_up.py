import sys
import psutil

mem_usage = psutil.virtual_memory()
each_core = psutil.cpu_percent(interval=1, percpu=True)
core_count = 1
for per_cpu in each_core:
    if per_cpu > 80 and mem_usage.percent > 80:
        print(f'core{core_count}: {per_cpu}%')
        print(f'memory usage: {mem_usage.percent}%')
        print("resource usage is high, close the unnecessary applications")
        sys.exit()
    core_count += 1
print("system in normal condition")
