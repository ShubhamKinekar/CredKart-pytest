import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')
#config.read(r'D:\Batch Notes\PythonAutomation\CT20\Credkart_Pytest_Dec\Configurations\config.ini')


class ReadConfigClass:
    @staticmethod
    def geta_data_for_email():
        email = config.get('Login data', 'email')
        return email

    @staticmethod
    def geta_data_for_password():
        password = config.get('Login data', 'password')
        return password

    @staticmethod
    def get_homepage_url():
        homepageurl = config.get('Application url', 'homepage')
        return homepageurl

    @staticmethod
    def get_login_url():
        loginurl = config.get('Application url', 'login_page')
        return loginurl


    @staticmethod
    def get_register_url():
        registerurl = config.get('Application url', 'register_page')
        return registerurl



    @staticmethod
    def section1_data():
        section2_data = config.get('section 1', 'key1')
        return section2_data