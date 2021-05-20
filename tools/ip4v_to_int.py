# -*- coding: utf-8 -*-
import json
import sys
import pathlib
import argparse
import logging
from datetime import datetime
import re
from logging import getLogger
import ipaddress

import settings

logger = getLogger(__name__)

EPOC_START_DATETIME_STR = '2000-01-01 00:00:00'
EPOC_END_DATETIME_STR = '2030-12-31 23:59:59'
JSON_DB_FILENAME_API = 'test/ipv4_statistics.json'

BASE_DIR = settings.BASE_DIR
logger.info('BASE_DIR: ' + BASE_DIR)
"""
ip = ipaddress.ip_address("8.8.8.8")
print(int(ip))
ip = ipaddress.ip_address("254.8.8.8")
print(int(ip))
"""


def main(ipv4file, dt_from, dt_to, out_json):
    p_file = pathlib.Path(ipv4file)

    if not p_file.exists():
        logger.info("[E] {} not found".format(p_file))
        sys.exit(1)

    logger.info("logfile being statistically processed.")

    f_file_text = p_file.read_text()
    # f_logfile_text = p_logfile.read_text(encoding='CP932', errors='backslashreplace')
    msg_json = get_statistics(f_file_text, dt_from, dt_to)
    # db.jsonに書き込む
    msg_json['count'] = len(msg_json['results'])
    logger.info("write info. to {}".format(out_json))
    fw = open(out_json, "w")
    json.dump(msg_json, fw, indent=4)
    logger.info("done[{}]".format(len(msg_json['results'])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', description='get statistics on log.', usage='%(prog)s [options]')
    parser.add_argument('ipv4', help='the target log.')
    parser.add_argument('--dt_from', help='datetime when log started.', default=EPOC_START_DATETIME_STR)
    parser.add_argument('--dt_to', help='datetime when log ended', default=EPOC_END_DATETIME_STR)
    parser.add_argument('--out_json', help='json fomrat file', default=JSON_DB_FILENAME_API)
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args()
    # print(vars(args))
    # print(args.days)
    # print(args.verbose)
    logger.info('the target log: {}'.format(args.logfile))
    logger.info('datetime started: {}'.format(args.dt_from))
    logger.info('datetime ended: {}'.format(args.dt_to))
    logger.info('out json: {}'.format(args.out_json))
    if args.verbose:
        logger.info('verbose mode: True')
        q_verbose = True
    else:
        logger.info('verbose mode: False')
        q_verbose = False

    # Loggingレベルを変更してログを出なくする
    if not q_verbose:
        # from logging import FATAL
        # disable(FATAL)
        from logging import disable
        from logging import DEBUG

        disable(DEBUG)

    main(BASE_DIR + args.logfile, args.dt_from, args.dt_to, BASE_DIR + args.out_json)

    # 変更したLoggingレベルを戻す（リセットする）
    # from logging import NOTSET
    # disable(NOTSET)
