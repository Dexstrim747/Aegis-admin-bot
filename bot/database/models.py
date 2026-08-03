CREATE_TABLES = [

    # Пользователи
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    # Группы
    """
    CREATE TABLE IF NOT EXISTS chats (
        chat_id INTEGER PRIMARY KEY,
        title TEXT,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    # Предупреждения
    """
    CREATE TABLE IF NOT EXISTS warns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        admin_id INTEGER NOT NULL,
        reason TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,

    # Муты
    """
    CREATE TABLE IF NOT EXISTS mutes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        admin_id INTEGER NOT NULL,
        until_date INTEGER,
        reason TEXT
    );
    """,

    # Настройки групп
    """
    CREATE TABLE IF NOT EXISTS settings (
        chat_id INTEGER PRIMARY KEY,
        antispam INTEGER DEFAULT 1,
        antiflood INTEGER DEFAULT 1,
        captcha INTEGER DEFAULT 0,
        logs INTEGER DEFAULT 1
    );
    """
]