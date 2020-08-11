#encoding=gbk
import os
import logging
import ctypes
from logging.handlers import RotatingFileHandler
from concurrent_log_handler import ConcurrentRotatingFileHandler


FOREGROUP_WHITH = 0x0007
FOREGROUP_BLUE = 0x01
FOREGROUP_GREEN = 0x02
FOREGROUP_RED = 0x04
FOREGROUP_YELLOW = FOREGROUP_RED | FOREGROUP_GREEN

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def make_dir(dir_path):
    path = dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


class Logger:
    def __init__(self, path, name):
    # def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(level=logging.INFO)
        # 设置文件日志
        fh = logging.FileHandler(filename=path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(level=logging.WARNING)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warring(self, message, color=FOREGROUP_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUP_WHITH)

    def error(self, message, color=FOREGROUP_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUP_WHITH)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger('./yyx.log','zt')
    logyyx.debug('一个debug')
    logyyx.info('一个info')
    logyyx.warring('一个war')
    try:
        1/0
    except Exception as e:
        logyyx.error(f"异常是{e}")

