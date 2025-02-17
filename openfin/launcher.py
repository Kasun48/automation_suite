# openfin/launcher.py
import subprocess
from utils.config import OPENFIN_PATH
from utils.logger import logger

def launch_openfin():
    logger.info("Launching OpenFin application...")
    subprocess.Popen(OPENFIN_PATH)