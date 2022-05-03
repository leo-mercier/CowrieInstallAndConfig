import json
import logging
import os
import Extractor
import Expeditor
import time
import wget
import yaml


def OpenConfigFileAndDownloadLogs():
        with open('config.yml') as config:
                config = yaml.safe_load(config)
                if os.path.exists('logs/cowrie.json'):
                        os.remove('logs/cowrie.json')
                        print("cowrie.json already exist, i deleted it")
                # download logs file from the honeypot
                wget.download(config['logs_url'], 'logs/cowrie.json')


def ExtactAndWriteNewFormat():
        try:
                print(" [+] Extracting cowrie HoneyPot data")
                data = an.ExtractCowrie()
                print(" [+] Writing results to cowrie result file (resultsCowrie.json)")
                with open('resultsCowrie.json', 'w') as res:
                        json_formated = json.dumps(data, indent=4)
                        res.writelines(json_formated)
        except Exception as e:
                msg = "[!] Error while extracting cowrie.json file data or writing results to resultsCowrie.json"
                err = "[!] Details : " + e
                logging.ERROR(msg)
                logging.ERROR(err)
                print(msg)
                print(err)


if __name__ == '__main__':
        #Set a timer
        ProcessTimer = time.time()
        # Initiate the logging file
        logging.basicConfig(filename='LogAnalyzer.log',
                            level=logging.ERROR)
        # Initiate extracteur class to extract logs from the honeypot
        an = Extractor.Extractor()

        OpenConfigFileAndDownloadLogs()
        ExtactAndWriteNewFormat()

        # Call sendToMisp function in Expeditor class to send event into MISP instance
        Expeditor.MispOuput.sendToMisp();

        # calculate the process time
        executionTime = (time.time() - ProcessTimer)
        print('Execution time in seconds: ' + str(executionTime))






















        # ============================================================================
        # Code suivant est la possibilite d'ajouter un honeypot web nomme tanner/snare
        # ============================================================================

        # try:
        #         print(" [+] Extracting tanner HoneyPot data")
        #         data = an.ExtractTanner()
        #         print(" [+] Writing results to tanner result file (resultsTanner.json)")
        #         with open('resultsTanner.json', 'w') as res:
        #                 json_formated = json.dumps(data, indent=4)
        #                 res.writelines(json_formated)
        # except Exception as e:
        #         msg = "[!] Error while extracting tanner_report.json file data or writing results to resultsTanner.json"
        #         err = "[!] Details : " + e
        #         logging.ERROR(msg)
        #         logging.ERROR(err)
        #         print(msg)
        #         print(err)
        #
        # try:
        #         an.CowrieTannerCorrel()
        # except Exception as e:
        #         msg = "[!] Error while searching corelation in both logs"
        #         err = "[!] Details : " + e
        #         logging.ERROR(msg)
        #         logging.ERROR(err)
        #         print(msg)
        #         print(err)

