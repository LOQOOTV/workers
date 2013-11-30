import sys, json
import urlparse
import cgi

class WorkerArgs:
    payload = None
    config = None

    def __init__(self, payload=None, config=None, webhook=False, multipart=False):
        self.payload = payload
        self.config = config
        if self.payload is None or self.config is None:
            for i in range(len(sys.argv)):
                if self.payload is None and sys.argv[i] == "-payload" and (i + 1) < len(sys.argv):
                    payload_file = sys.argv[i+1]
                    with open(payload_file, 'r') as f:
                        data = f.read()
                        if multipart:
                            boundary = data.strip().split("\n")[0][2:].strip()
                            f.seek(0)
                            self.payload = cgi.parse_multipart(f, {"boundary": boundary})
                        else:
                            if webhook:
                                data = urlparse.parse_qs(data)
                                data = data["payload"][0]
                            self.payload = json.loads(data)
                elif self.config is None and sys.argv[i] == "-config" and (i + 1) < len(sys.argv):
                    config_file = sys.argv[i+1]
                    with open(config_file, 'r') as f:
                        self.config = json.loads(f.read())
                if self.config is not None and self.payload is not None:
                    break
