import yaml

# 读取 YAML 配置文件
def load_config(file_path: str):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)  # 使用 safe_load 读取文件
    return config