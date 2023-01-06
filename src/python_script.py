from datetime import datetime
import os
import logging
current_dir_path = os.getcwd()
f_name = datetime.now().strftime('%Y%m%d-%H%M%S')
os.mkdir(f_name)
f_path = os.path.join(current_dir_path, f_name)
os.chdir(f_path)

with open('logs.txt', 'w') as f:
     f.write('Logging File Results\n')

logging.basicConfig(filename="logs.txt", level=logging.DEBUG)
logging.debug("Debug logging test...")
# logging.info("Program is working as expected")
# logging.warning("Warning, the program may not function properly")
# logging.error("The program encountered an error")
# logging.critical("The program crashed")

