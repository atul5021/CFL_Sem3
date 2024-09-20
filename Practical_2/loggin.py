import logging

logging.basicConfig(

    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s"

)

log = logging.getLogger(__name__)
log.info("test the custom logger")

