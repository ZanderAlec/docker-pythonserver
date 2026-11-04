import os
import sys

import mysql.connector
from mysql.connector import Error

QUERY = "SELECT User, Host FROM mysql.user;"

def conectar():
    try:
        return mysql.connector.connect(
            host=os.environ["DB_HOST"],
            port=int(os.environ.get("DB_PORT", "3306")),
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
        )
    except Error as erro:
        sys.exit(f"erro: {erro}")


def main():
    conn = conectar()
    try:
        cur = conn.cursor()
        cur.execute(QUERY)
        linhas = cur.fetchall()
        cur.close()
    finally:
        conn.close()

    print(f"Resultado de: {QUERY}")
    print(f"{'User':<20} Host")
    print("-" * 40)
    for user, host in linhas:
        print(f"{user:<20} {host}")
    print(f"\n{len(linhas)} linha(s)")


if __name__ == "__main__":
    main()
