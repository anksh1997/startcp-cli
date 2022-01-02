import datetime

class Logger:

    def info(self, log_msg):
        os.makedirs(constants.startcp_default_folder, exist_ok=True)
        with open(str(constants.startcp_log_file), "w+") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + log_msg)
