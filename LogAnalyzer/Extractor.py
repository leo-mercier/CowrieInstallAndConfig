import json
import wget


class Extractor:
    def __init__(self):
        self.CowrieIPs = []
        self.TannerIPs = []
        self.cowrieSessions = {}
        self.tannerSessions = {}

    def ExtractCowrie(self):
        try:
            with open('logs/cowrie.json', 'r') as f:
                data = f.readlines()
                for l in data:
                    l = json.loads(l)
                    if l['src_ip'] not in self.CowrieIPs:
                        self.CowrieIPs.append(l['src_ip'])
                for ip in self.CowrieIPs:
                    self.cowrieSessions[ip] = {}
                    for l in data:
                        l = json.loads(l)
                        if ip in l['src_ip']:
                            for k, v in l.items():
                                if k not in self.cowrieSessions[ip]:
                                    self.cowrieSessions[ip][k] = []
                                    self.cowrieSessions[ip][k].append(v)
                                else:
                                    if v not in self.cowrieSessions[ip][k]:
                                        self.cowrieSessions[ip][k].append(v)
            return self.cowrieSessions
        except Exception as e:
            msg = "[!] Error while retreiving data from cowrie.json logging file"
            err = "[!] Details : " + e
            print(msg);
            print(err);

    # ============================================================================
    # Code suivant est la possibilite d'ajouter un honeypot web nomme tanner/snare
    # ============================================================================

    # def ExtractTanner(self):
    #     try:
    #         with open('logs/tanner_report.json', 'r') as f:
    #             data = f.readlines()
    #             for l in data:
    #                 l = json.loads(l)
    #                 if l['peer']['ip'] not in self.TannerIPs:
    #                     self.TannerIPs.append(l['peer']['ip'])
    #             for ip in self.TannerIPs:
    #                 self.tannerSessions[ip] = {}
    #                 for l in data:
    #                     l = json.loads(l)
    #                     if ip in l['peer']['ip']:
    #                         for k, v in l.items():
    #                             if k not in self.tannerSessions[ip]:
    #                                 self.tannerSessions[ip][k] = []
    #                                 self.tannerSessions[ip][k].append(v)
    #                             else:
    #                                 if v not in self.tannerSessions[ip][k]:
    #                                     self.tannerSessions[ip][k].append(v)
    #         return self.tannerSessions
    #     except Exception as e:
    #         msg = "[!] Error while retreiving data from tanner.json logging file"
    #         err = "[!] Details : " + e
    #         print(msg);
    #         print(err);
    #
    # def CowrieTannerCorrel(self):
    #     with open('logs/correlation.json', 'w') as C:
    #         for ip in self.TannerIPs:
    #             if ip in self.CowrieIPs:
    #                 C.writelines(" [+] " + str(ip) + " is present in both SSH and Tanner Logs.")