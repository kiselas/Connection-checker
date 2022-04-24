import argparse
import logging
logging.getLogger()


def read_user_cli_args():
    """Handle the CLI args and options."""
    parser = argparse.ArgumentParser(
        prog='conn_checker', description='check the availability of websites'
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    parser.add_argument(
        "-lf",
        "--log-file",
        metavar="logfile",
        type=str,
        default="",
        help="path to log file",
    )
    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    if result:
        logging.info(f'{url} is online! 👍')
    else:
        logging.info(f'{url} is offline: {error}')
