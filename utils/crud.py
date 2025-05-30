from fastapi import HTTPException
from mysql.connector import Error
from database import get_connection

def executar_insert(query, params):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def executar_select(query):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Erro de banco de dados: {str(e)}")
    finally:
        cursor.close()
        conn.close()
