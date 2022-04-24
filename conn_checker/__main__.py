import pathlib
import sys
import logging
import asyncio
from conn_checker.checker import site_is_online, site_is_online_async
from conn_checker.cli import display_check_result, read_user_cli_args

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, encoding='utf-8',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S ')


def main():
    """Run Connection Checker."""
    user_args = read_user_cli_args()
    if user_args.log_file:
        fh = logging.FileHandler(user_args.log_file)
        fh.setLevel(logging.INFO)
        log.addHandler(fh)
    logging.info("Run connection checker")
    urls = _get_websites_urls(user_args)
    if not urls:
        logging.error("No URLs to check")
        sys.exit(1)
    if user_args.asynchronous:
        asyncio.run(_asynchronous_check(urls))
    else:
        _synchronous_check(urls)


def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            logging.error(f'Empty input file, {file}')
    else:
        logging.error("Input file not found")
    return []


def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)


async def _asynchronous_check(urls):
    async def _check(url):
        error = ""
        try:
            result = await site_is_online_async(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

    await asyncio.gather(*(_check(url) for url in urls))


if __name__ == "__main__":
    main()
