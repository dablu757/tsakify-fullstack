import logging
import os

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename='logs/app.log',
    # filemode='a' 
)

LOGGER = logging.getLogger(__name__)