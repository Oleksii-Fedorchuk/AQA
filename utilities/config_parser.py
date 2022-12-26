import configparser

config = configparser.RawConfigParser()
config.read("../configurations/configuration.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("app_info", "base_url")

    @staticmethod
    def get_dashboard_url():
        return config.get("app_info", "dashboard_url")

    @staticmethod
    def get_standard_user_name():
        return config.get("user_info", "standard_user_name")

    @staticmethod
    def get_locked_user_name():
        return config.get("user_info", "locked_user_name")

    @staticmethod
    def get_problem_user_name():
        return config.get("user_info", "problem_user_name")

    @staticmethod
    def get_performance_glitch_user_name():
        return config.get("user_info", "performance_glitch_user_name")

    @staticmethod
    def get_password():
        return config.get("user_info", "password")

    @staticmethod
    def get_driver_id():
        return config.get("browser", "browser_id")

    @staticmethod
    def get_client_first_name():
        return config.get("client_info", "client_name")

    @staticmethod
    def get_client_last_name():
        return config.get("client_info", "client_last_name")

    @staticmethod
    def get_client_postal_code():
        return config.get("client_info", "client_postal_code")
