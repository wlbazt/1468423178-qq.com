import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(f"当前路径:{BASE_DIR}")
# /Users/xxxx/python_code/FastAdmin/backend

sys.path.insert(0, BASE_DIR)

from app.api.db.base import Base  # noqa

target_metadata = Base.metadata
