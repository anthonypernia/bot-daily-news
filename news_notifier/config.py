""" config file for news_notifier """
import configparser

configparser.DEFAULTSECT = "DEFAULT"

config = configparser.ConfigParser()
config.read("config.ini")

default_settings = config["DEFAULT"]
