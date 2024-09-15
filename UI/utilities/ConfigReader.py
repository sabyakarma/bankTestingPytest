from configparser import ConfigParser


class ConfigReader:

    def __init__(self):

        self.config = ConfigParser()
        self.configFile = r"UI/configuration/config.ini"
        self.config.read(self.configFile)

    def get_base_url(self):
        return self.config['env'].get('url','http://localhost')

    def get_user_name(self):
        return self.config['login'].get('userName')

    def get_user_password(self):
        return self.config['login'].get('password')




