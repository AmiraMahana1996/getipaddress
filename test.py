import uuid
import socket



from fastapi import FastAPI, Request

app = FastAPI()

hostname = socket.gethostname()
ipv4_address = socket.gethostbyname(hostname)



def get_mac_address():
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac_address[i:i+2] for i in range(0, len(mac_address), 2)])

# phyId=get_mac_address()
@app.get("/getPhusicalId")
async def home(request: Request):
    ip_address = request.client
    return f'Your IP address is: {ipv4_address}'
