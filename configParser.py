def parse_config_file(filename):
    config = {}
    section = None
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('[') and line.endswith(']'):
                    section = line[1:-1]
                    config[section] = {}
                elif '=' in line and section:
                    key, value = line.split('=', 1)
                    config[section][key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None