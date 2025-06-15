import psutil

def check_cpu_usage():
    try:
        usage = psutil.cpu_percent()
        print("Monitoring CPU usage...")
        while True:
            if usage > 80:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")
    except Exception as e:
        print(f"Somthing Went wrong: {e}")

def main():
    check_cpu_usage()

if __name__ == "__main__":
    main()