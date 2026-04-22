from config_loader import ConfigLoader

config = ConfigLoader()

print("Safe config:", config.get_safe_config())
print("DB Host:", config.get("DB_HOST"))