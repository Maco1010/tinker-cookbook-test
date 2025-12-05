import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Config:
    
    def __init__(self):
        self.TINKER_API_KEY = os.getenv('TINKER_API_KEY')
    
    # 可选：添加配置验证
    def validate(self):
        required_vars = ['TINKER_API_KEY']
        for var in required_vars:
            if not getattr(self, var):
                raise ValueError(f"Missing required configuration: {var}")

# 创建配置实例
config = Config()

# 验证配置
config.validate()