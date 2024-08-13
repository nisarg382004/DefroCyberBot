import os
import subprocess
import requests
import psutil
import whois
import shodan
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import matplotlib.pyplot as plt
import speech_recognition as sr

# Configuration
SHODAN_API_KEY = 'MDWDeR5X2P4BdwUIRCVaz2hfCmgLHC9J'
WEATHER_API_KEY = 'YOUR_WEATHER_API_KEY'
EMAIL_SENDER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'
COMMAND_ALIASES = {}
context = {}

# Initialize Shodan API
shodan_api = shodan.Shodan(SHODAN_API_KEY)

def process_command(command):
    if command == 'help':
        return get_help()
    elif command.startswith('weather '):
        location = command.split(' ', 1)[1]
        return get_weather(location)
    elif command.startswith('domain '):
        domain = command.split(' ', 1)[1]
        return lookup_domain(domain)
    elif command.startswith('traceroute '):
        target = command.split(' ', 1)[1]
        return run_traceroute(target)
    elif command.startswith('whois '):
        domain = command.split(' ', 1)[1]
        return whois_lookup(domain)
    elif command == 'status':
        return get_system_resources()
    elif command == 'network':
        return monitor_network_traffic()
    elif command == 'cpu_temp':
        return get_cpu_temperature()
    elif command.startswith('disk '):
        directory = command.split(' ', 1)[1]
        return get_disk_usage(directory)
    elif command.startswith('calculate '):
        expression = command.split(' ', 1)[1]
        return calculate_expression(expression)
    elif command.startswith('email '):
        parts = command.split(' ', 3)
        recipient = parts[1]
        subject = parts[2]
        body = parts[3]
        return send_email(recipient, subject, body)
    elif command == 'alerts':
        return check_system_alerts()
    elif command.startswith('set_alert '):
        _, resource_type, threshold = command.split(' ', 2)
        return set_alert_threshold(resource_type, int(threshold))
    elif command == 'check_alerts':
        return check_custom_alerts()
    elif command == 'interactive':
        interactive_mode()
    elif command == 'update':
        return check_for_updates()
    elif command == 'tutorial':
        start_tutorial()
    elif command.startswith('search '):
        query = command.split(' ', 1)[1]
        return advanced_search(query)
    elif command.startswith('download '):
        resource = command.split(' ', 1)[1]
        return download_resource(resource)
    elif command.startswith('plot_cpu '):
        data = command.split(' ', 1)[1]
        return plot_cpu_usage([float(i) for i in data.split(',')])
    elif command == 'real_time':
        return monitor_network_traffic()  # Can be expanded to other real-time metrics
    else:
        return f"Unknown command: {command}. Type 'help' for a list of commands."

def get_help():
    return (
        "Available commands:\n"
        "  help                   - Show this help message\n"
        "  weather [location]     - Get weather information for the specified location\n"
        "  domain [domain]        - Lookup WHOIS information for the specified domain\n"
        "  traceroute [target]    - Perform a traceroute to the specified target\n"
        "  whois [domain]         - Lookup WHOIS information for the specified domain\n"
        "  status                 - Show system resource usage\n"
        "  network                - Monitor network traffic\n"
        "  cpu_temp               - Show CPU temperature\n"
        "  disk [directory]       - Show disk usage for the specified directory\n"
        "  calculate [expression] - Calculate the result of the specified expression\n"
        "  email [recipient] [subject] [body] - Send an email\n"
        "  alerts                 - Check system alerts\n"
        "  set_alert [resource_type] [threshold] - Set alert thresholds\n"
        "  check_alerts           - Check custom alerts\n"
        "  interactive            - Start interactive mode\n"
        "  update                 - Check for updates\n"
        "  tutorial               - Start tutorial\n"
        "  search [query]         - Perform an advanced search\n"
        "  download [resource]    - Download a specified resource\n"
        "  plot_cpu [data]        - Plot CPU usage from comma-separated data\n"
        "  real_time              - Monitor real-time metrics"
    )

def get_weather(location):
    try:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}")
        data = response.json()
        weather = data['current']
        return (f"Weather in {location}:\n"
                f"Temperature: {weather['temp_c']}°C\n"
                f"Condition: {weather['condition']['text']}\n"
                f"Humidity: {weather['humidity']}%\n"
                f"Wind: {weather['wind_kph']} kph")
    except Exception as e:
        return f"Failed to fetch weather data: {e}"

def lookup_domain(domain):
    try:
        info = whois.whois(domain)
        return str(info)
    except Exception as e:
        return f"Failed to lookup domain: {e}"

def get_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return (
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_info.percent}%\n"
        f"Disk Usage: {disk_info.percent}%"
    )

def monitor_network_traffic():
    net_io = psutil.net_io_counters()
    return (f"Bytes Sent: {net_io.bytes_sent}\n"
            f"Bytes Received: {net_io.bytes_recv}\n"
            f"Packets Sent: {net_io.packets_sent}\n"
            f"Packets Received: {net_io.packets_recv}")

def get_cpu_temperature():
    try:
        sensors = psutil.sensors_temperatures()
        if 'coretemp' in sensors:
            return f"CPU Temperature: {sensors['coretemp'][0].current}°C"
        else:
            return "CPU temperature information not available."
    except Exception as e:
        return f"Failed to fetch CPU temperature: {e}"

def get_disk_usage(directory):
    try:
        disk_info = psutil.disk_usage(directory)
        return (
            f"Disk Usage for {directory}:\n"
            f"Total: {disk_info.total / (1024**3):.2f} GB\n"
            f"Used: {disk_info.used / (1024**3):.2f} GB\n"
            f"Free: {disk_info.free / (1024**3):.2f} GB\n"
            f"Percent Used: {disk_info.percent}%"
        )
    except Exception as e:
        return f"Failed to fetch disk usage: {e}"

def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Failed to calculate expression: {e}"

def send_email(recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, recipient, msg.as_string())
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {e}"

def run_traceroute(target):
    try:
        result = subprocess.check_output(["traceroute", target], stderr=subprocess.STDOUT, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Failed to run traceroute: {e.output}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        return str(info)
    except Exception as e:
        return f"Failed to lookup domain: {e}"

def check_system_alerts():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    
    alerts = []
    if cpu_usage > 80:
        alerts.append(f"High CPU usage detected: {cpu_usage}%")
    if memory_info.percent > 80:
        alerts.append(f"High memory usage detected: {memory_info.percent}%")
    
    if alerts:
        return "\n".join(alerts)
    else:
        return "No system alerts."

def set_alert_threshold(resource_type, threshold):
    context['alert_thresholds'] = context.get('alert_thresholds', {})
    context['alert_thresholds'][resource_type] = threshold
    return f"Alert threshold for {resource_type} set to {threshold}."

def check_custom_alerts():
    alerts = []
    thresholds = context.get('alert_thresholds', {})
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    if 'cpu' in thresholds and cpu_usage > thresholds['cpu']:
        alerts.append(f"CPU usage exceeded threshold: {cpu_usage}%")
    if 'memory' in thresholds and memory_info.percent > thresholds['memory']:
        alerts.append(f"Memory usage exceeded threshold: {memory_info.percent}%")

    if alerts:
        return "\n".join(alerts)
    else:
        return "No custom alerts."

def start_tutorial():
    return (
        "Tutorial:\n"
        "1. Type 'help' to see the list of available commands.\n"
        "2. Use 'weather [location]' to get weather information.\n"
        "3. Use 'domain [domain]' for WHOIS lookup.\n"
        "4. Use 'traceroute [target]' to perform traceroute.\n"
        "5. Use 'status' to check system resources.\n"
        "6. Use 'network' to monitor network traffic.\n"
        "7. Use 'cpu_temp' to get CPU temperature.\n"
        "8. Use 'disk [directory]' to check disk usage.\n"
        "9. Use 'calculate [expression]' to evaluate mathematical expressions.\n"
        "10. Use 'email [recipient] [subject] [body]' to send emails.\n"
        "11. Use 'alerts' to check system alerts.\n"
        "12. Use 'set_alert [resource_type] [threshold]' to set alert thresholds.\n"
        "13. Use 'check_alerts' to check custom alerts.\n"
        "14. Use 'interactive' to enter interactive mode.\n"
        "15. Use 'update' to check for updates.\n"
        "16. Use 'tutorial' to get a brief tutorial.\n"
        "17. Use 'search [query]' for advanced search functionality.\n"
        "18. Use 'download [resource]' to download resources.\n"
        "19. Use 'plot_cpu [data]' to plot CPU usage from data.\n"
        "20. Use 'real_time' to monitor real-time metrics."
    )

def check_for_updates():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "defroc-bot"])
        return "Bot and dependencies updated successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to update: {e}"

def plot_cpu_usage(cpu_usage_list):
    plt.plot(cpu_usage_list)
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.savefig('cpu_usage_plot.png')
    return "CPU usage plot saved as 'cpu_usage_plot.png'."

def interactive_mode():
    while True:
        try:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                print("Exiting interactive mode.")
                break
            response = process_command(command)
            print(response)
            log_command(command, response)
        except Exception as e:
            print(f"Error: {e}")

def advanced_search(query):
    # Implement advanced search functionality here
    return "Advanced search functionality not yet implemented."

def download_resource(resource):
    # Implement resource download functionality here
    return "Resource download functionality not yet implemented."

def log_command(command, response):
    # Log command and response for auditing or debugging
    with open('command_log.txt', 'a') as log_file:
        log_file.write(f"Command: {command}\nResponse: {response}\n\n")

def interactive_mode():
    while True:
        try:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                print("Exiting interactive mode.")
                break
            response = process_command(command)
            print(response)
            log_command(command, response)
        except Exception as e:
            print(f"Error: {e}")

# Schedule email notifications for system alerts
schedule.every().hour.do(lambda: send_email('recipient@example.com', 'System Alert', check_system_alerts()))

# Start the interactive terminal
interactive_mode()
