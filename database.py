import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('tg.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS accounts(a_id TEXT PRIMARY KEY, cart_id TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS items(i_id TEXT PRIMARY KEY, name TEXT, desc TEXT, price TEXT, photo TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS brands(b_id TEXT PRIMARY KEY, name TEXT, b_desc TEXT)")

    db.commit()


async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ?, ?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()


async def edit_profile(state, user_id):
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET photo = '{}', age = '{}', description = '{}', name = '{}' WHERE user_id == '{}'".format(
            data['photo'], data['age'], data['description'], data['name'], user_id))
        db.commit()