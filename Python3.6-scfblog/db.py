import pymysql.cursors

from index import host, port, user, pas, db


def get_db():
    """
    Connect to the application's configured database.
    The connection is unique for each request and will be reused if this is called again.
    连接到应用程序的已配置数据库。
    连接对于每个请求都是唯一的，如果被调用，将被重用。再一次。
    """
    connect = pymysql.connect(
        host=host,
        user=user,
        password=pas,
        database=db,
        port=port,
        cursorclass=pymysql.cursors.DictCursor
    )

    with connect:
        cur = connect.cursor()
        state_user = cur.execute("show tables like 'user'")
        state_post = cur.execute("show tables like 'post'")

    if state_user == 0:
        with connect:
            cur = connect.cursor()
            cur.execute("""
            CREATE TABLE `user` (
              `id` INT NOT NULL AUTO_INCREMENT,
              `username` TINYTEXT NOT NULL,
              `password` TINYTEXT NOT NULL,
              `sessionUUID4` VARCHAR(36) NULL,
              PRIMARY KEY (`id`)
            )
            """)

    if state_post == 0:
        with connect:
            cur = connect.cursor()
            cur.execute("""
            CREATE TABLE `post` (
              `id` INT NOT NULL AUTO_INCREMENT,
              `author_id` INT NOT NULL,
              `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
              `title` TINYTEXT NOT NULL,
              `body` MEDIUMTEXT NOT NULL,
              PRIMARY KEY (`id`)
            )
            """)

    return connect
