import json
from datetime import date
from pymisp import MISPEvent, PyMISP
import yaml


class MispOuput():

    def sendToMisp(self=None):
        with open('config.yml') as config:
            config = yaml.safe_load(config)
            misp = PyMISP(config['misp_base_url'], config['misp_publisher_api_key'], False)
            with open('resultsCowrie.json', 'r') as f:
                data = json.load(f)
                if data:
                    for k in data:
                        event = MISPEvent()
                        d = date.today()
                        event.set_date(d)
                        event.info = f'This is IOCs for: {k} from Cowrie Honeypot'
                        if 'src_ip' in data[k].keys():
                            event.add_attribute('ip-src', k)
                        if 'dst_port' in data[k].keys():
                            event.add_attribute('port', data[k]['dst_port'])
                        if 'url' in data[k].keys():
                            event.add_attribute('url', data[k]['url'])
                        if 'input' in data[k].keys():
                            event.add_attribute('text', data[k]['input'], disable_correlation=True, comment='Command input by the entity')
                        if 'version' in data[k].keys():
                            event.add_attribute('text', data[k]['version'], comment='Version of the SSH client')
                        if 'protocol' in data[k].keys():
                            event.add_attribute('text', data[k]['protocol'])
                        if 'username' in data[k].keys():
                            event.add_attribute('text', data[k]['username'], disable_correlation=True, comment='Usernames used to connect to the honeypot')
                        if 'password' in data[k].keys():
                            event.add_attribute('text', data[k]['password'], disable_correlation=True, comment='Paswords used to connect to the honeypot')
                        if 'hassh' in data[k].keys():
                            event.add_attribute('hassh-md5', data[k]['hassh'], comment='"HASSH" is a network fingerprinting standard which can be used to identify specific Client and Server SSH implementations.')
                        if 'sensor' in data[k].keys():
                            event.add_attribute('text', data[k]['sensor'], comment="The origin sensor name")
                        misp.add_event(event)


