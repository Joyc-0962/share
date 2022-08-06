from datetime import datetime, time
from logging.handlers import TimedRotatingFileHandler
import logging
import time
# 基本logging======
# 沒有設定檔名就只會出現在console上
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# 顯現ERROR、CRITICAL======
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')

# 輸出到檔案======
# logging.basicConfig(level=logging.INFO, filename='log.txt', filemode='w',
#                     format='[%(asctime)s %(levelname)s] %(message)s',
#                     datefmt='%Y%m%d %H:%M:%S'
#                     )

# if __name__ == "__main__":
#     logging.debug('debug')
#     logging.info('info')
#     logging.warning('warning')
#     logging.error('error')
#     logging.critical('critical')

# 輸出到檔案和console======
# import logging
# import datetime

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
#     datefmt='%Y%m%d %H:%M:%S')

# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# ch.setFormatter(formatter)

# log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
# fh = logging.FileHandler(log_filename)
# fh.setLevel(logging.DEBUG)
# fh.setFormatter(formatter)

# logger.addHandler(ch)
# logger.addHandler(fh)

# if __name__ == "__main__":
#     logging.debug('debug')
#     logging.info('info')
#     logging.warning('warning')
#     logging.error('error')
#     logging.critical('critical')

# 定期輸出到新檔案======

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
rotating_handler = TimedRotatingFileHandler(filename="./TimedRotatingFileHandler/log.txt",
                                            when='S')
rotating_handler.suffix = '%Y-%m-%d_%H-%M-%S'
formatter = logging.Formatter(
    '%(asctime)s %(name)s:%(levelname)s - %(message)s')
rotating_handler.setLevel(logging.INFO)
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)

time_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in time_list:
    time.sleep(i)
    logger.info("hello")
