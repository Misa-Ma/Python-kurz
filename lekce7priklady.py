from datetime import datetime, timedelta
apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%m/%d/%Y"))

SatelitSolarOrbiter_start = datetime(2020, 2, 10, 5, 3)
den_v_tydnu = SatelitSolarOrbiter_start.strftime("%A")
print(f"Satelit Solar Orbiter started: {den_v_tydnu}")

SSO_start = datetime(day=10, month=2, year=2020, hour=5, minute=3)
od_startu = (datetime.now() - SSO_start)
print (f"SSO startoval {SSO_start.weekday()}. den v týdnu")


Datum_objednavky = datetime (2020, 11, 13, 19, 47)
prevzeti_objednavky = timedelta (minutes=8, seconds= 35)
priprava_jidla = timedelta (minutes =30)
doprava = timedelta (minutes=25, seconds=30)
celkovy_cas_doruceni = prevzeti_objednavky + priprava_jidla + doprava
cas_doruceni = Datum_objednavky + celkovy_cas_doruceni
print (f"Objednávka už míří k Vám, očekávaný čas doručení je {cas_doruceni.strftime('%d. %m %Y, ve %H:%M:%S')} hodin")
