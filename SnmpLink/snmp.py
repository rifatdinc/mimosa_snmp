#!/usr/bin/python3
from routeros_api import Api, CreateSocketError
import aiosnmp
import asyncio
import time
import mysql.connector
import json
import nmap3
from udpPortSnmp import subPro


def sql():
    connection = mysql.connector.connect(host="DATABASE HOST", user="My Database Username", password="My database Password",
                                         database="DATABASE NAME", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute(
        'Select Bname From mimosa')
    gels = cursor.fetchall()
    nasName = []
    for values in gels:
        nasnameStr = values[0].decode()
        nasName.append(nasnameStr)
    return nasName


async def main(ip):
    degerler = []

    async with aiosnmp.Snmp(host=ip, port=161, community="public") as snmp:
        # nmap = nmap3.NmapHostDiscovery()
        # result = nmap.nmap_portscan_only(ip, args="-p 161 ")
        udpPort = subPro(ip)
        # ipPorts = result[ip]['ports']
        # for state in ipPorts:
        if udpPort == 'open':
            for res in await snmp.get(['1.3.6.1.4.1.43356.2.1.2.1.1.0',
                                       '1.3.6.1.4.1.43356.2.1.2.5.8.0',
                                       '1.3.6.1.4.1.43356.2.1.2.6.3.1.3.1',
                                       '1.3.6.1.4.1.43356.2.1.2.6.1.1.6.1',
                                       '1.3.6.1.4.1.43356.2.1.2.7.1.0',
                                       '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.1',
                                       '1.3.6.1.4.1.43356.2.1.2.6.2.1.5.2',
                                       '1.3.6.1.4.1.43356.2.1.2.7.2.0',
                                       '1.3.6.1.4.1.43356.2.1.2.1.8.0',
                                       '1.3.6.1.4.1.43356.2.1.2.3.3.0',
                                       '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.1',
                                       '1.3.6.1.4.1.43356.2.1.2.6.1.1.3.2',
                                       '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.1',
                                       '1.3.6.1.4.1.43356.2.1.2.6.2.1.2.2']):
                degerler.append(res.value)
        else:
            print('Port Kapali', ip)
    return degerler


def fenasin(iplers):
    try:
        mimosaName = asyncio.run(main(iplers))
        NamesMimosa = mimosaName[0].decode()
        MimosaIp = str(mimosaName[1])
        MimosaMhz = mimosaName[2]
        MimosaFrequency = mimosaName[3]
        MimosaTxValue = mimosaName[4] / 100000
        MimosaRxPhy0 = mimosaName[5]
        MimosaRxPhy1 = mimosaName[6]
        MimosaRxValue = mimosaName[7] / 100000
        MimosaTotalRxPhy = MimosaRxPhy0 + MimosaRxPhy1
        rxValuess = str(MimosaRxValue)
        rxValues = rxValuess[0:5]
        txValuess = str(MimosaTxValue)
        txValues = txValuess[0:5]
        MimosaCpuTempS = str(mimosaName[8])
        MimosaCpuTemp = MimosaCpuTempS[0:2]
        WirelesStatus = mimosaName[9]
        RxDbms = str(mimosaName[10])
        RxDbms1 = str(mimosaName[11])
        MimosaTxPhy0 = mimosaName[12]
        MimosaTxPhy1 = mimosaName[13]
        MimosaTotalTxPhy = MimosaTxPhy0 + MimosaTxPhy1
        RxDbm = RxDbms[0:3]
        RxDbm1 = RxDbms1[0:3]
        return json.dumps({
            'NamesMimosa': NamesMimosa,
            'MimosaIp': MimosaIp,
            'MimosaMhz': MimosaMhz,
            'MimosaFrequency': MimosaFrequency,
            'MimosaTotalRxPhy': MimosaTotalRxPhy,
            'MimosaTotalTxPhy': MimosaTotalTxPhy,
            'MimosaTxValue': rxValues,
            'MimosaRxValue': txValues,
            'MimosaCpuTemp': MimosaCpuTemp,
            'WirelesStatus': WirelesStatus,
            'RxDbm': RxDbm,
            'RxDbm1': RxDbm1, })
    except Exception as err:
        print(err)


def saymaMakinesi():
    connection = mysql.connector.connect(host="DATABASE HOST", user="My Database Username", password="My database Password",
                                         database="DATABASE NAME", auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute(
         'Select device,nas,ip From tblLink WHERE device="mimosa"  ORDER BY ip')
    gels = cursor.fetchall()
      MimosaInformation = []
       for values in gels:
            NasIpp = values[2].decode()
            ass = fenasin(NasIpp)
            MimosaInformation.append(ass)
        return MimosaInformation


'''
1.3.6.1.4.1.43356.2.1.2.4.1.0 - Station Wireless Mode - 2
1.3.6.1.4.1.43356.2.1.2.1.1.0 - Cihazin Ismi
1.3.6.1.4.1.43356.2.1.2.4.1.0 -  Hangi Ulke koduna Sahip
1.3.6.1.4.1.43356.2.1.2.5.8.0 - Cihazin Ip Adresi
1.3.6.1.4.1.43356.2.1.2.5.10.0 - Cihazin Gatewayi
1.3.6.1.4.1.43356.2.1.2.6.1 - Cihazin Chain Degerleri
1.3.6.1.4.1.43356.2.1.2.6.1.1.6.1 	- Cihazin Frekansi
1.3.6.1.4.1.43356.2.1.2.6.3.1.3.1 - Cihazin Kac Mhz'de Mhz'si
1.3.6.1.4.1.43356.2.1.2.6.3.1.4.1 - Cihaz Kac dBm'de Calisiyor.
1.3.6.1.4.1.43356.2.1.2.6.3.1.5.1 - Cihaz Kac Frekasnta Calisiyor.
1.3.6.1.4.1.43356.2.1.2.7.1.0 - Cihaz Kac mbps trafik geciyor Tx Degeri
1.3.6.1.4.1.43356.2.1.2.7.2.0 - Cihazin anlik gecirdigi Rx Degeri.

1.3.6.1.4.1.43356.2.1.2.3.3.0	mimosaWanStatus.0	INTEGER: connected(1)	Overview > Dashboard > Wireless Status
1.3.6.1.4.1.43356.2.1.2.3.4.0	mimosaWanUpTime.0	Timeticks: (18571300) 2 days, 3:35:13.00	Overview > Dashboard > Link Uptime
1.3.6.1.4.1.43356.2.1.2.1.8.0	mimosaInternalTemp.0	INTEGER: 382 C1	Overview > Dashboard > Device Details > Internal Temp or CPU Temp (Local)
'''
