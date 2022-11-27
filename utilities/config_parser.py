import configparser

config = configparser.RawConfigParser()
config.read("/Users/oleksiifedorchuk/PycharmProjects/AQA/Automation_tests/configurations/configuration.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("app_info", "base_url")

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
