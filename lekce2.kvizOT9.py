#Jak bude vypadat slovník pozice?
#Bude obsahovat pouze dvojici "Petra": "vývojářka"
#Ke klíči "nova_kolegyně" se uloží hodnota "Petra". Lenka a Lucka zůstanou
#Petra nahradí ve slovníku Lucku, je vždy přepsána poslední hodnota.
#Petra nahradí ve slovníku Lenku, je vždy přepsána první hodnota.
#Ke klíči "Petra" se uloží hodnota "vývojářka". Lenka a Lucka zůstanou
#Program skončí chybou KeyError

pozice = {"Lenka":"testerka", "Lucka": "analytička"}
nova_kolegyne = "Petra"
pozice[nova_kolegyne] = "vývojářka"