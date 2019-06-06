from com.mcneelat.pyutils.anomali import Anomali
from com.mcneelat.pyutils.confutils import load_conf

conf_file = 'C:\\Users\\tmcne003\\Documents\\PyCharmProjects\\pyutils\\conf\\bvprofile.json'
conf_data = load_conf(conf_file)
anomali_conf = conf_data['ANOMALI_INFO']
anomali = Anomali(anomali_conf['API_USER'], anomali_conf['API_KEY'], 98)
iocs = anomali.get_iocs("domain")
for r in iocs:
    print(r)
isthreat = anomali.is_threat("govnohost.ddns.net")
print(isthreat)
