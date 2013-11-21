import yadtbroadcastclient

def create(name):
    return yadtbroadcastclient.WampBroadcaster('ybc', 8081, name)
