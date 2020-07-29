import logging
import logging.config
import os

import simplejson as simplejson

log_init = False


def init_logging(console=False):
    global log_init
    if log_init:
        return
    if console:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s')
    else:
        log_config_path = os.getenv('BREAKTIME_LOG_SETTINGS_PATH', '/etc/Sif/logging-article.json')
        if os.path.exists(log_config_path):
            with open(log_config_path, 'rt') as f:
                config = simplejson.load(f)
                logging.config.dictConfig(config)
        else:
            log_filename = os.getenv('BREAKTIME_LOG_PATH', '/var/log/breaktime/article.log')
            logging.basicConfig(filename=log_filename, level=logging.DEBUG)
    log_init = True
