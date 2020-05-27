from .mysql_client import get_connection
import os

def handler(event, context):
  db_status = 'successful'
  try:
    db_client = get_connection()
    db_client.close()
  except Exception:
    db_status = 'failure'
    
  return {
      "db_status": db_status
  }