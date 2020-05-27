import os
import requests
from dotenv import load_dotenv
from time import sleep
load_dotenv()

def wait_for_local_stack_services(host, port, services):
  status = get_local_stack_status(host, port)
  while not are_services_ready(services.split(','), status):
    print('Local stack services are not ready, retrying in 3 seconds...')
    sleep(3)
    status = get_local_stack_status(host, port)

  print('Local stack services are now ready!')

def are_services_ready(services, status):
  try:
    if not status:
      return False
    services_status = status['services']
  except KeyError:
    return False

  try:
    for service in services:
      if services_status[service] != 'running':
        return False
    return True
  except KeyError as _ke:
    raise Exception('Service not found', _ke)

def get_local_stack_status(host, port):
  try:
    response = requests.get(f'http://{host}:{port}/health?reload')
    return response.json()
  except Exception as _ex:
    print('Local stack not ready, retrying in 3 seconds...')
    sleep(3)
    get_local_stack_status(host, port)

if __name__ == "__main__":
  try:
    host = os.environ['LOCAL_STACK_HOST']
    port = os.environ['LOCAL_STACK_PORT']
    services = os.environ['LOCAL_STACK_SERVICES']
    wait_for_local_stack_services(host, port, services)
  except KeyError as _ke:
    print('Missing environemnt variable', _ke)
    raise _ke
  except Exception:
    raise