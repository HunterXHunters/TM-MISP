# Beyond Endpoint Detection and Response using TM Vision One and MISP Feeds

This script can help your Threat Hunting team to run auto sweep for IoC using MISP STIX version 2 intelligence source.

1. Download the any Threat Feed (Stix_v2) which you want to search in your network for indicators extracted from the source.

2. Give File name as input to the script which is downloaded from MISP from step 1. 
(You can give direct filename if script is in same folder ex: misp.event.list.json
or 
can give complete path with filename as input ex: C:\Users\Downloads\misp.event.list.json)

3. Script takes file as input extact all objects for IoCs for sweeping which are listed from threat Feed. 
(MISP Threat Feed is now loaded in Custom Intelligence Report module in TM-XDR)

4. Script initates Auto-Sweep to search for extracted IoC in your network and if any matchs, you can see them in matched indicators and assosicated assets. 

![image](https://github.com/HunterXHunters/TM-MISP/assets/2347778/3a69de3c-8953-4d84-9f4e-88493974929a)
