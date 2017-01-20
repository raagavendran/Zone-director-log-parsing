import re
import MySQLdb

db = MySQLdb.connect("localhost","root","asm123","ap" )
file = open('/home/asm/Downloads/aamac.txt','rb').read()


#MACAddress
pmac = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
foundmac = re.findall(pmac, file)
cursor = db.cursor()
print '*********************MACAddress*********************'
for mac in foundmac:

    print mac


#IPV4 ADDRESS
pip = re.compile(r'/\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s/')
foundip = re.findall(pip, file)
cursor = db.cursor()
print '*********************IPV4Address*********************'
for ip in foundip:
    ip = ip[1:-1]
    print ip


#IPv6Address
pips = re.compile(r'([\da-fA-F]{4}::[\d])')
foundips = re.findall(pips, file)
print '*********************IPv6Address*********************'
for ips in foundips:
    print ips


#NAME
print '*********************NAME*********************'
pna = re.compile(r'\s*Name\s*:\s*(.*)')
foundna = re.findall(pna, file)
for na in foundna:
    print na

#State
pst = re.compile(r'\s*State\s*:\s*(.*)')
foundst = re.findall(pst, file)
print '*********************State*********************'
for st in foundst:
    print st

#Tunnel
ptu = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/')
foundtu = re.findall(ptu, file)
print '*********************Tunnel*********************'
for tu in foundtu:
    print tu

#SEC  Name                : HSO4181-WAP0012
	Tunnel/Sec Mode     : L3 (Unknown) / PSK
	State               : RUN
	Mesh Role           : ROOT AP
psec = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
foundsec = re.findall(psec, file)
print '*********************SEC MODE*********************'
for sec in foundsec:
    xsec = sec.split("/")
    print xsec[1]

#Mesh_Role
pmes = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
print '*********************Mesh_Role*********************'
foundmes = re.findall(pmes, file)
for mes in foundmes:
    print mes

#PSK
ppsk = re.compile(r'\s*PSK\s*:\s*(.*)')
foundpsk = re.findall(ppsk, file)
print '*********************PSK*********************'
for psk in foundpsk:
    print psk

#Timer
pti = re.compile(r'\s*Timer\s*:\s*(.*)')
foundti = re.findall(pti, file)
print '*********************TIMER*********************'
for ti in foundti:
    print ti

#HW version
phw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)/')
foundhw = re.findall(phw, file)
print '*********************HW Version*********************'
for hw in foundhw:
    print hw

#SW Version
psw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
foundsw = re.findall(psw, file)
print '*********************SW Version*********************'
for sw in foundsw:
    xsw = sw.split("/")
    print xsw[1]

#Model
pmo = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)/')
foundmo = re.findall(pmo, file)
print '*********************Model*********************'
for mo in foundmo:
    print mo

#Serial_number
pse = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
foundse = re.findall(pse, file)
print '*********************Serial_number*********************'
for se in foundse:
    xse = se.split("/")
    print xse[1]

if len(foundmac)==len(foundip)==len(foundsw)==len(foundhw)==len(foundna)==len(foundst)==len(foundtu)==len(foundsec)==len(foundmes)==len(foundpsk)==len(foundti)==len(foundmo)==len(foundse)==len(foundips):
    for i in range(len(foundmac)):
                cursor.execute("""INSERT INTO apt(Name,MACAddress,IPV4Address,SW_Version,HW_Version,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,Model,Serial_number,IPv6Address)
                 VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % (foundna[i],foundmac[i],foundip[i][1:-1],foundsw[i][11:23],foundhw[i],foundst[i],foundtu[i],foundsec[i][15:18],foundmes[i],foundpsk[i],foundti[i],foundmo[i],foundse[i][9:21],foundips[i]))

try:
   db.commit()
except:
   db.rollback()

db.close()


