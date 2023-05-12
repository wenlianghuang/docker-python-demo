import os
import sys
import time
import logging
from datetime import datetime
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="the name to be logged")
    args = parser.parse_args()
    
    # 获取当前时间
    time_date_total = datetime.today()
    time_date = str(time_date_total).split(' ')[0]
    time_date_time = str(time_date_total).split(' ')[1].split('.')[0].split(':')
    time_date_millisecond = str(time_date_total).split(' ')[1].split('.')[1]
    time_date_millisecond = int(time_date_millisecond[:3])

    # 配置日志记录器
    logger = logging.getLogger("Test")
    logger.setLevel(logging.DEBUG)

    ch = logging.FileHandler("/app/logs/Test_Logs_{}_{}_{}_{}_{}_{}.log".format(time_date, time_date, time_date_time[0], time_date_time[1], time_date_time[2], time_date_millisecond))
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s  %(levelname)s  %(message)s]')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # 记录日志
    logger.info("Test %s" % myname)