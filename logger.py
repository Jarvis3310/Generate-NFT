import logging
from logging import handlers
class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }
    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#設置格式
        self.logger.setLevel(self.level_relations.get(level))#設置級別
        sh = logging.StreamHandler()
        sh.setFormatter(format_str) #設置顯示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')
        #記錄
        th.setFormatter(format_str)#設置紀錄的格式
        self.logger.addHandler(sh) #加到logger裡
        self.logger.addHandler(th)
