def parse_config(config_str):
    """Parse the configuration string and return a dictionary of key-value pairs."""
    if not config_str:
        return {}

    configs = config_str.split(";")
    parsed_config = {}

    for config in configs:
        key, value = config.split("=")
        parsed_config[key.strip()] = value.strip()

    return parsed_config
