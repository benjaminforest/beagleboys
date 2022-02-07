#https://pypi.org/project/websocket_client/
import websocket
from shared import shared

FILENAME="sample3.txt"
global BUFFER
BUFFER = []

def on_message(ws, message):
    global BUFFER
    BUFFER += [message+"\n"]
    if len(BUFFER) == 100:
        with open(FILENAME, "a") as fp:
            fp.writelines(BUFFER)
        BUFFER = []

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    for symbol in shared.SYMBOLS:
        ws.send(f'{{"type":"subscribe","symbol":"{symbol}"}}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c7ttg6iad3ifisk2drlg",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()