import logging
from utils import my_lib


def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logging.info("Started")
    my_lib.do_something()
    logging.info("Finished")


if __name__ == "__main__":
    main()
