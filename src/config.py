class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'my-secret-pw'
    MYSQL_DB = 'auravant-challange'


config = {
    'development': DevelopmentConfig
}