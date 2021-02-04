import pya3rt


class ClGetReply:
    Pya3rt_API = "DZZBA92i9EhCouadQ29CXrw1hMOKORxl"

    def __init__(self, message):
        self.message = message

    def getReply(self):
        client = pya3rt.TalkClient(self.Pya3rt_API)
        res = client.talk(self.message)
        rep = res['results'][0]['reply']
        print("Takeru 「%s」" % rep)
        return rep
