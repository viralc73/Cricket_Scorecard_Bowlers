import random
import math
import numpy as np
import pandas as pd
import copy
import time
import statistics

from sympy.stats.rv import probability

t20 = []
for i in range(0, 20):
    t20.append(0)
for i in range(0, 28):
    t20.append(1)
for i in range(0, 17):
    t20.append(2)
for i in range(0, 5):
    t20.append(3)
for i in range(0, 4):
    t20.append(4)
for i in range(0, 4):
    t20.append(5)
for i in range(0, 3):
    t20.append(6)

ODI = []
for i in range(0, 65):
    ODI.append(0)
for i in range(0, 35):
    ODI.append(1)
for i in range(0, 17):
    ODI.append(2)
for i in range(0, 5):
    ODI.append(3)
for i in range(0, 7):
    ODI.append(4)
for i in range(0, 3):
    ODI.append(5)
for i in range(0, 3):
    ODI.append(6)

t20_target = []
for i in range(0, 19):
    t20_target.append(0)
for i in range(0, 23):
    t20_target.append(1)
for i in range(0, 15):
    t20_target.append(2)
for i in range(0, 6):
    t20_target.append(3)
for i in range(0, 5):
    t20_target.append(4)
for i in range(0, 6):
    t20_target.append(5)
for i in range(0, 5):
    t20_target.append(6)

t20_target_2 = []
for i in range(0, 28):
    t20_target_2.append(0)
for i in range(0, 30):
    t20_target_2.append(1)
for i in range(0, 14):
    t20_target_2.append(2)
for i in range(0, 4):
    t20_target_2.append(3)
for i in range(0, 6):
    t20_target_2.append(4)
for i in range(0, 3):
    t20_target_2.append(5)
for i in range(0, 4):
    t20_target_2.append(6)

t20_target_extreme = []
for i in range(0, 15):
    t20_target_extreme.append(0)
for i in range(0, 20):
    t20_target_extreme.append(1)
for i in range(0, 15):
    t20_target_extreme.append(2)
for i in range(0, 4):
    t20_target_extreme.append(3)
for i in range(0, 7):
    t20_target_extreme.append(4)
for i in range(0, 9):
    t20_target_extreme.append(5)
for i in range(0, 8):
    t20_target_extreme.append(6)

ODI_target = []
for i in range(0, 56):
    ODI_target.append(0)
for i in range(0, 50):
    ODI_target.append(1)
for i in range(0, 16):
    ODI_target.append(2)
for i in range(0, 5):
    ODI_target.append(3)
for i in range(0, 10):
    ODI_target.append(4)
for i in range(0, 7):
    ODI_target.append(5)
for i in range(0, 5):
    ODI_target.append(6)

ODI_target_2 = []
for i in range(0, 90):
    ODI_target_2.append(0)
for i in range(0, 40):
    ODI_target_2.append(1)
for i in range(0, 21):
    ODI_target_2.append(2)
for i in range(0, 5):
    ODI_target_2.append(3)
for i in range(0, 6):
    ODI_target_2.append(4)
for i in range(0, 2):
    ODI_target_2.append(5)
for i in range(0, 2):
    ODI_target_2.append(6)

# Death
Tests_Death = []
for i in range(0, 280): #250 #275
    Tests_Death.append(0)
for i in range(0, 35):
    Tests_Death.append(1)
for i in range(0, 15):
    Tests_Death.append(2)
for i in range(0, 5):
    Tests_Death.append(3)
for i in range(0, 6):
    Tests_Death.append(4)
for i in range(0, 8): #5
    Tests_Death.append(5)
Tests_Death.append(6)

# Minefield
Tests_Mine = []
for i in range(0, 300): #250 #275
    Tests_Mine.append(0)
for i in range(0, 45):
    Tests_Mine.append(1)
for i in range(0, 16):
    Tests_Mine.append(2)
for i in range(0, 5):
    Tests_Mine.append(3)
for i in range(0, 7):
    Tests_Mine.append(4)
for i in range(0, 6): #5
    Tests_Mine.append(5)
Tests_Mine.append(6)

# Normal Scoring 300ish
Tests = []
for i in range(0, 270): #250 #275
    Tests.append(0)
for i in range(0, 36):
    Tests.append(1)
for i in range(0, 16):
    Tests.append(2)
for i in range(0, 5):
    Tests.append(3)
for i in range(0, 7):
    Tests.append(4)
for i in range(0, 4): #5
    Tests.append(5)
Tests.append(6)

# Highway
Tests_High = []
for i in range(0, 250): #250 #275
    Tests_High.append(0)
for i in range(0, 45):
    Tests_High.append(1)
for i in range(0, 18):
    Tests_High.append(2)
for i in range(0, 6):
    Tests_High.append(3)
for i in range(0, 10):
    Tests_High.append(4)
for i in range(0, 4): #5
    Tests_High.append(5)
Tests_High.append(6)

NewZealandT20 = "Finn Allen,Devon Conway(†),Kane Williamson(c),Glenn Phillips,Jimmy Neesham,Mark Chapman,Michael Santner,Ish Sodhi,Tim Southee,Lockie Ferguson,Trent Boult"
NZT20Bowl = [0, 0, 0.1, 0.7, 0.7, 0.4, 0.8, 0.9, 0.95, 0.95, 0.95]
NZT20Type = [None, None, "S", "S", "P", "S", "S", "S", "P", "P", "P"]
NewZealandODI = "Devon Conway,Rachin Ravindra,Kane Williamson(c),Daryl Mitchell,Tom Latham(†),Glenn Phillips,Mark Chapman,Mitchell Santner,Tim Southee,Trent Boult,Lockie Ferguson"
NZODIBowl = [0, 0.6, 0.1, 0.5, 0, 0.7, 0.4, 0.8, 0.95, 0.95, 0.95]
NZODIType = [None, "S", "S", "P", None, "S", "S", "S", "P", "P", "P"]
NewZealandTest = "Tom Latham(†),Devon Conway,Kane Williamson(c),Rachin Ravindra,Daryl Mitchell,Tom Blundell,Glenn Phillips,Tim Southee,Trent Boult,Matt Henry,Ben Sears"
NZTestBowl = [0,0,0.01,0.6,0.6,0,0.75,0.95,0.95,0.95,0.9]
NZTestType = [None, None, "S", "S", "P", None, "S", "P", "P", "P", "P"]
NewZealandT20Women = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze(†),Rosemary Mair,Lea Tahuhu,Eden Carson,Fran Jonas"
NZT20WBowl = [0.3,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
NZT20WType = ["S", None, "S", "P", "P", "S", None, "P", "P", "S", "S"]
NewZealandODIWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze(†),Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
NZODIWBowl = [0.1,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
NZODIWType = ["S", None, "S", "P", "P", "S", None, "P", "P", "P", "S"]
NewZealandTestWomen = "Suzie Bates,Georgia Plimmer,Amelia Kerr,Sophie Devine(c),Brooke Halliday,Maddy Green,Isabella Gaze(†),Hannah Rowe,Jess Kerr,Molly Penfold,Fran Jonas"
NZTestWBowl = [0.3,0,0.75,0.7,0.25,0.34,0,0.79,0.85,0.88,0.91]
NZTestWType = ["S", None, "S", "P", "P", "S", None, "P", "P", "P", "S"]
AustraliaT20 = "Travis Head,Jake Fraser-McGurk,Mitchell Marsh(c),Glenn Maxwell,Marcus Stoinis,Matthew Wade(†),Tim David,Ashton Agar,Pat Cummins,Mitchell Starc,Adam Zampa"
AUST20Bowl = [0.3,0,0.75,0.7,0.7,0,0.1,0.8,0.95,0.95,0.95]
AUST20Type = ["S", None, "P", "S", "P", None, "P", "S", "P", "P", "S"]
AustraliaODI = "Travis Head,Jake Fraser-McGurk,Mitchell Marsh,Steve Smith,Marnus Labuschagne,Glenn Maxwell,Alex Carey(†),Pat Cummins(c),Mitchell Starc,Adam Zampa,Jason Behrendoff"
AUSODIBowl = [0.3,0,0.75,0.2,0.3,0.7,0,0.95,0.95,0.95,0.9]
AUSODIType = ["S", None, "P", "S", "S", "S", None, "P", "P", "S", "P"]
AustraliaTest = "Sam Konstas,Usman Khawaja,Marnus Labuschagne,Steve Smith,Travis Head,Mitchell Marsh,Alex Carey(†),Pat Cummins(c),Mitchell Starc,Nathan Lyon,Josh Hazlewood"
AUSTestBowl = [0,0,0.3,0.05,0.02,0.8,0,0.95,0.9,0.8,0.9]
AUSTestType = [None, None, "S", "S", "S", "P", None, "P", "P", "S", "P"]
AustraliaAllTimeTest = "Justin Langer,Matthew Hayden,Don Bradman,Ricky Ponting(c),Shane Watson,Steve Smith,Adam Gilchrist(†),Pat Cummins,Mitchell Johnson,Shane Warne,Glenn McGrath"
AUSATTestBowl = [0.001, 0, 0.005, 0.0075, 0.85, 0.1, 0, 0.9, 0.9, 0.9, 0.91]
AUSATTestType = ["P", None, "S", "S", "P", "S", None, "P", "P", "S", "P"]
AustraliaT20Women = "Alyssa Healy(†),Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AUST20WBowl = [0,0,0.1,0.1,0.8,0.05,0.75,0.75,0.8,0.8,0.8]
AUST20WType = [None, None, "S", "P", "P", "S", "S", "P", "S", "P", "P"]
AustraliaODIWomen = "Alyssa Healy(†),Beth Mooney,Georgia Wareham,Tahlia McGrath(c),Ellyse Perry,Phoebe Litchfield,Ashleigh Gardner,Annabel Sutherland,Sophie Molineux,Megan Schutt,Darcie Brown"
AUSODIWBowl = [0,0,0.1,0.1,0.8,0.05,0.75,0.75,0.8,0.8,0.8]
AUSODIWType = [None, None, "S", "P", "P", "S", "S", "P", "S", "P", "P"]
AustraliaTestWomen = "Beth Mooney,Phoebe Litchfield,Ellyse Perry,Tahlia McGrath,Jess Jonassen,Alyssa Healy(c)(†),Ashleigh Gardner,Annabel Sutherland,Alana King,Kim Garth,Darcie Brown"
AUSTestWBowl = [0,0.005,0.9,0.4,0.5,0,0.75,0.75,0.8,0.8,0.8]
AUSTestWType = [None, "S", "P", "P", "S", None, "S", "P", "S", "P", "P"]
IndiaT20 = "Rohit Sharma(c),Abhishek Sharma,Virat Kohli,SKY,Rishabh Pant(†),Shivam Dube,Rinku Singh,Avesh Khan,Mayank Yadav,Yuzi Chahal,Jasprit Bumrah"
INDT20Bowl = [0.1,0.2,0.1,0.2,0,0.6,0.2,0.8,0.9,0.9,0.95]
INDT20Type = ["S", "S", "S", "S", None, "P", "S", "P", "P", "S", "P"]
IndiaODI = "Rohit Sharma(c),Shubman Gill,Virat Kohli,Shreyash Iyer,KL Rahul(†),Hardik Pandya,Ravindra Jadeja,Jasprit Bumrah,Mohd Shami,Kuldeep Yadav,Mohd Siraj"
INDODIBowl = [0.1,0.1,0.1,0.1,0,0.76,0.78,0.95,0.95,0.9,0.85]
INDODIType = ["S", "S", "S", "S", None, "P", "S", "P", "P", "S", "P"]
IndiaTest = "Rohit Sharma(c),Yashasvi Jaiswal,Shubman Gill,Virat Kohli,KL Rahul,Nitish Kumar Reddy,Rishabh Pant(†),Ravindra Jadeja,Mohd Shami,Jasprit Bumrah,Mohd Siraj"
INDTestBowl = [0.005,0,0.007,0.005,0,0.4,0,0.8,0.85,0.99,0.9]
INDTestType = ["S", None, "S", "S", None, "P", None, "S", "P", "P", "P"]
IndiaAllTimeTest = "Sunil Gavaskar,Virender Sehwag,Rahul Dravid,Sachin Tendulkar,Virat Kohli(c),Rishabh Pant(†),Kapil Dev,Ravichandran Ashwin,Anil Kumble,Jasprit Bumrah,Harbhajan Singh"
INDATTestBowl = [0, 0.01, 0, 0.35, 0.01, 0, 0.8, 0.9, 0.9, 0.9, 0.85]
INDATTestType = [None, "S", None, "S", "S", None, "P", "S", "S", "P", "S"]
IndiaT20Women = "Shafali Verma,Smriti Mandhana,Jemimah Rodrigues,Harmanpreet Kaur(c),Deepti Sharma,Richa Ghosh(†),Pooja Vastrakar,Arundhati Reddy,Shreyanka Patil,Radha Yadav,Renuka Singh"
INDT20WBowl = [0,0.1,0.1,0.3,0.6,0,0.8,0.78,0.9,0.8,0.88]
INDT20WType = [None, "S", "S", "S", "S", None, "P", "P", "S", "S", "P"]
IndiaODIWomen = "Shafali Verma,Smriti Mandhana,Dayalan Hemalatha,Harmanpreet Kaur(c),Jemimah Rodrigues,Richa Ghosh(†),Deepti Sharma,Pooja Vastrakar,Radha Yadav,Asha Sobhana,Renuka Singh"
INDODIWBowl = [0,0.1,0.3,0.4,0.1,0,0.7,0.88,0.85,0.85,0.9]
INDODIWType = [None, "S", "S", "S", "S", None, "S", "P", "S", "S","P"]
IndiaTestWomen = "Shafali Verma,Smriti Mandhana,Shubha Satheesh,Jemimah Rodrigues,Harmanpreet Kaur(c),Richa Ghosh(†),Deepti Sharma,Pooja Vastrakar,Shen Rana,Renuka Singh,Rajeshwari Gayakwad"
INDTestWBowl = [0,0.01,0,0.01,0.3,0,0.6,0.85,0.85,0.9,0.87]
INDTestWType = [None, "S", None, "S", "S", None, "S", "P", "S", "P", "S"]
EnglandODI = "Phil Salt,Zack Crawley,Joe Root,Harry Brook(c),Jos Buttler(†),Ben Stokes,Sam Curran,Chris Woakes,Jofra Archer,Adil Rashid,Mark Wood"
ENGODIBowl = [0,0,0.4,0,0,0.7,0.75,0.9,0.9,0.9,0.95]
ENGODIType = [None, None, "S", None, None, "P", "P", "P", "P", "S", "P"]
EnglandT20 = "Phil Salt,Jos Buttler(†),Jacob Bethell,Liam Livingstone,Harry Brook(c),Ben Stokes,Sam Curran,Chris Woakes,Jofra Archer,Adil Rashid,Mark Wood"
ENGT20Bowl = [0,0,0.3,0.5,0,0.5,0.78,0.85,0.9,0.95,0.95]
ENGT20Type = [None, None, "S", "S", None, "P", "P", "P", "P", "S", "P"]
EnglandTest = "Zack Crawley,Ben Duckett,Joe Root,Harry Brook,Ben Stokes(c),Jamie Smith(†),Chris Woakes,Gus Atkinson,Jofra Archer,Mark Wood,Jack Leach"
ENGTestBowl = [0,0,0.25,0,0.6,0,0.85,0.8,0.87,0.85,0.83]
ENGTestType = [None, None, "S", None, "P", None, "P", "P", "P", "P", "S"]
EnglandAllTimeTest = "Alec Stewart(†),Andrew Strauss,Michael Vaughan(c),Ian Bell,Joe Root,Kevin Pietersen,Ben Stokes,Andrew Flintoff,Stuart Broad,Graeme Swann,James Anderson"
ENGATTestBowl = [0, 0, 0, 0, 0.3, 0, 0.75, 0.9, 0.9, 0.9, 0.9]
ENGATTestType = [None, None, None, None, "S", None, "P", "P", "P", "S", "P"]
EnglandT20Women = "Maia Bouchier,Danni Wyatt-Hodge,Alice Capsey,Nat Sciver-Brunt,Heather Knight(c),Amy Jones(†),Charlie Dean,Sophie Ecclestone,Freya Kemp,Sarah Glenn,Lauren Bell"
ENGT20WBowl = [0,0,0.4,0.85,0.005,0,0.85,0.87,0.9,0.87,0.9]
ENGT20WType = [None, None, "S", "P", "S", None, "S", "S", "P", "S", "P"]
EnglandODIWomen = "Tammy Beaumont,Maia Bouchier,Heather Knight(c),Nat Sciver-Brunt,Danni Wyatt-Hodge,Amy Jones(†),Alice Capsey,Charlie Dean,Sophie Ecclestone,Kate Cross,Lauren Bell"
ENGODIWBowl = [0,0,0.01,0.8,0,0,0.4,0.85,0.9,0.9,0.95]
ENGODIWType = [None, None, "S", "P", None, None, "S", "S", "S", "P", "P"]
EnglandTestWomen = "Maia Bouchier,Tammy Beaumont,Heather Knight(c),Nat Sciver-Brunt,Sophia Dunkley,Danni Wyatt-Hodge,Amy Jones(†),Sophie Ecclestone,Kate Cross,Lauren Filer,Lauren Bell"
ENGTestWBowl = [0,0,0.02,0.8,0.005,0.005,0,0.85,0.9,0.87,0.92]
ENGTestWType = [None, None, "S", "P", "S", None, None, "S", "P", "P", "P"]
SouthAfricaT20 = "Reeza Hendricks,QDK(†),Aiden Markram(c),Tristan Stubbs,Heinrich Klaasen,David Miller,Marco Jansen,Keshav Maharaj,Kagiso Rabada,Anrich Nortje,Tabraiz Shamsi"
SAT20Bowl = [0,0,0,0,0,0,0.9,0.87,0.95,0.95,0.88]
SAT20Type = [None, None, None, None, None, None, "P", "S", "P", "P", "S"]
SouthAfricaODI = "QDK(†),Temba Bavuma(c),Rassie van der Dussen,Aiden Markram,Heinrich Klaasen,David Miller,Marco Jensen,Gerald Coetzee,Keshav Maharaj,Kagiso Rabada,Tabraiz Shamsi"
SAODIBowl = [0,0,0,0,0,0,0.87,0.87,0.85,0.95,0.8]
SAODIType = [None, None, None, None, None, None, "P", "P", "S", "P", "S"]
SouthAfricaNewTEST = "Aiden Markram,Temba Bavuma(c),Tony de Zorzi,Keegan Petersen,David Bedingham,Kyle Verreynne,Marco Jansen,Gerald Coetzee,Kagiso Rabada,Nandre Burger,Anrich Nortje"
SANewTestBowl = [0,0,0,0,0,0,0.8,0.9,0.95,0.8,0.9]
SouthAfricaTEST = "Dean Elgar,Aiden Markram,Hashim Amla,AB De Villiers,Faf Du Plessis(c),QDK(†),Vernon Philander,Keshav Maharaj,Kagiso Rabada,Morne Morkel,Lungi Ngidi"
SATestBowl = [0,0,0,0.01,0.005,0,0.85,0.8,0.9,0.865,0.84]
SATestType = [None,None,None,"P","P",None,"P","S","P","P","P"]
SouthAfricaAllTimeTEST = "Graeme Smith(c),Hashim Amla,Faf Du Plessis,Jacques Kallis,Herschelle Gibbs,AB De Villiers,Mark Boucher(†),Shaun Pollock,Keshav Maharaj,Dale Steyn,Allan Donald"
SAATTestBowl = [0, 0, 0.005, 0.8, 0.001, 0.005, 0, 0.8, 0.75, 0.9, 0.9]
SAATTestType = [None, None, "S", "P", "S", "P", None, "P", "S", "P", "P"]
SouthAfricaAllTimeODI = "Hashim Amla,QDK(†),Faf Du Plessis,AB De Villiers(c),Jacques Kallis,Herschelle Gibbs,Lance Klusener,Dale Steyn,Morne Morkel,Allan Donald,Imran Tahir"
SAATODIBowl = [0, 0, 0.001, 0.005, 0.8, 0, 0.75, 0.9, 0.85, 0.85, 0.85]
SAATODIType = [None, None, "P", "P", "P", None, "P", "P", "P", "P", "S"]
SouthAfricaAllTimeT20 = "QDK(†),Graeme Smith(c),Faf du Plessis,AB de Villiers,David Miller,JP Duminy,Albie Morkel,Chris Morris,Dale Steyn,Kagiso Rabada,Imran Tahir"
SAATT20Bowl = [0, 0, 0.001, 0.005, 0, 0.65, 0.75, 0.8, 0.9, 0.9, 0.87]
SAATT20Type = [None, None, "P", "P", None, "S", "P", "P", "P", "P", "S"]
SouthAfricaT20Women = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Marizanne Kapp,Nadine de Klerk,Chloe Tryon,Sune Luus,Annerie Dercksen,Sinalo Jafta,Nonkululeko Mlaba,Ayabonga Khaka"
SAT20WBowl = np.sort(np.random.beta(0.01, 0.9, size=11))
SAT20WBowl[8] = 0
SouthAfricaODIWomen = "Laura Wolvaardt(c),Tazmin Brits,Anneke Bosch,Sune Luus,Marizanne Kapp,Nadine de Klerk,Nondumiso Shangase,Mieke de Ridder,Masabata Klaas,Nonkululeko Mlaba,Ayabonga Khaka"
SAODIWBowl = np.sort(np.random.beta(0.01, 0.9, size=11))
SAODIWBowl[7] = 0
SouthAfricaTESTWomen = "Laura Wolvaardt(c),Anneke Bosch,Sune Luus,Marizanne Kapp,Delmari Tucker,Nadine de Klerk,Sinalo Jafta,Annerie Dercksen,Tumi Sekhukhune,Masabata Klaas,Nonkululeko Mlaba"
SATestWBowl = np.sort(np.random.beta(0.1, 0.9, size=11))
SATestWBowl[6] = 0
AfghanistanT20 = ""
WestIndiesAllTimeTest = "Gordon Greenidge,S Chanderpaul,George Headley,Viv Richards,Brian Lara(†),Garry Sobers,Jackie Hendriks,Malcolm Marshall,Michael Holding,Curtly Ambrose,Lance Gibbs"
WIATTestBowl = [0, 0, 0, 0, 0, 0.87, 0, 0.9, 0.9, 0.9, 0.87]
WIATTestType = [None, None, None, None, None, "P", None, "P", "P", "P", "S"]

HilariousXI = "David Warner,Chris Gayle,Wasim Jaffer(†),Marnus Labuschagne,Glenn Maxwell(c),Jimmy Neesham,Dinesh Karthik,Dwayne Bravo,Yuzi Chahal,Kate Cross,Alex Hartley"
HilariousBowl = [0, 0.2, 0, 0.2, 0.4, 0.6, 0, 0.75, 0.9, 0.9, 0.9]
HilariousType = [None, "S", None, "S", "S", "P", None, "P", "S", "P", "S"]
PeanutButter = "Peanut Butter(c),Peanut Sandwich,Peanut Pancake,Peanut Burger,Peanut Lasagne,Peanut Colada,Sergeant Peanut,Peanut Calculus,Square Peanut,Peanut Biryani,Peanut Rice"
PBBowl = np.sort(np.random.beta(0.25, 0.8, size=11))
PBBowl[6] = 0
DahliaXI = "Viral Chitlangia(c),Harsha Venkat,Akshit Saran,Ayush Saran,Bunny(†),Aryan,Rishit,Joshua Lijo,Nikhil Matthew,Anchit Kumar,Devajya Khanna"
DahliaBowl = [0.8,0.83,0.7,0.8,0,0,0,0.65,0.2,0.95,0.9]
DahliaType = ["P", "P", "P", "P", None, "P", "S", "S", "P", "P", "P"]
SDS = "Viral C(c),Zehaan Naik,Aditya V(†),Ishi Jain,Nandini Bhattad,Raghav Govind,Subham Anand,Yash Bihany,Devansh Gupta,P Sarath,Priyanshu Gupta"
SDSBowl = [0.8,0.1,0,0.2,0.2,0.3,0.7,0.8,0.85,0.93,0.9]
SDSType = ["P", "S", None, "S", "S", "P", "P", "P", "P", "S", "S"]
Beatles = "Paul McCartney,Ringo Starr,George Harrison,John Lennon(c),George Martin,Brian Epstein(†),Eleanor Rigby,Billy Shears,Geoff Emerick,Sergeant Pepper,Mr Kite"
BeatlesBowl = [0.5,0.4,0.2,0.5,0.2,0,0.8,0.75,0.9,0.85,0.85]
WomenArtist = "Olivia Rodrigo(c),Sabrina Carpenter,Lana Del Rey,Leah Kate,Dua Lipa,Dasha,Adele,Katy Perry,Avril Lavigne,Linda Ronstadt,Tiffany Stringer"
WABowl = [0.2,0.2,0.3,0,0.6,0.5,0.7,0.75,0.8,0.85,0.85]
ModernFamily = "Phil Dunphy(c),Luke Dunphy,Claire Dunphy,Cam Tucker,Jay Pritchett,Lily Tucker-Pritchett,Manny Delgado,Alex Dunphy,Mitchell Pritchett,Gloria Pritchett,Haley Dunphy"
MFBowl = [0.1,0.8,0,0.4,0.3,0.75,0.6,0.58,0.75,0.8,0.9]
WeatherXI = "Alex Halestone,Weather Knight(c),Chris Gaylestorm,Ebony Rainford-Brent,Ben Sun-strokes,Jonny Bairsnow(†),David Chilley,Rain Warne,Matthew Foggard,Jimmy Andersun,John Snow"
WeatherBowl = [0,0.1,0.4,0,0.5,0,0.8,0.95,0.76,0.85,0.8]
RCB = "Virat Kohli,Phil Salt,Liam Livingstone,Rajat Patidar,Devdutt Padikkal,Tim David,Jitesh Sharma(†),Josh Hazlewood,Bhuvneshwar Kumar,Yash Dayal,Suyash Sharma"
RCBBowl = [0, 0, 0.6, 0, 0, 0.2, 0, 0.9, 0.85, 0.85, 0.8]
RCBType = [None, None, "S", None, None, "P", None, "P", "P", "P", "S"]
KKR = "QDK(†),Sunil Narine,Angkrish Raghuvanshi,Venkatesh Iyer(c),Rinku Singh,Andre Russell,Ramandeep Singh,Harshit Rana,Vaibhav Arora,Anrich Nortje,Varun Chakravarthy"
KKRBowl = [0, 0.9, 0, 0.4, 0.2, 0.8, 0, 0.9, 0.85, 0.9, 0.9]
KKRType = [None, "S", None, "P", "S", "P", None, "P", "P", "P", "S"]
CSK = "Ruturaj Gaikwad(c),Rachin Ravindra,Rahul Tripathi,Shivam Dube,Sam Curran,Vijay Shankar,Ravindra Jadeja,MS Dhoni(†),Ravichandran Ashwin,Noor Ahmad,Matheesha Pathirana"
CSKBowl = [0, 0.7, 0, 0.7, 0.8, 0.6, 0.85, 0, 0.85, 0.85, 0.8]
CSKType = [None, "S", None, "P", "P", "P", "S", None, "S", "S", "P", "P"]
DC = "Jake Fraser-McGurk,KL Rahul(†),Faf du Plessis,Karun Nair,Tristan Stubbs,Axar Patel(c),Abishek Porel,Mitchell Starc,T Natarajan,Kuldeep Yadav,Mukesh Kumar"
DCBowl = [0, 0, 0, 0, 0, 0.8, 0, 0.9, 0.85, 0.9, 0.75]
DCType = [None, None, None, None, None, "S", None, "P", "P", "S", "P"]
MI = "Rohit Sharma,Will Jacks,Tilak Varma,Suryakumar Yadav,Hardik Pandya(c),Naman Dhir,Robin Minz(†),Deepak Chahar,Jasprit Bumrah,Trent Boult,Mujeeb-ur-Rahman"
MIBowl = [0.3, 0.6, 0, 0.25, 0.75, 0, 0, 0.9, 0.95, 0.93, 0.87]
MIType = ["S", "S", None, "S", "P", None, None, "P", "P", "P", "S"]
LSG = "Rishabh Pant(c)(†),Aiden Markram,Nicholas Pooran,Mitchell Marsh,Ayush Badoni,David Miller,Shahbaz Ahmed,Ravi Bishnoi,Avesh Khan,Mohsin Khan,Akash Deep"
LSGBowl = [0, 0, 0, 0.75, 0, 0, 0.75, 0.85, 0.9, 0.85, 0.8]
LSGType = [None, None, None, "P", None, None, "S", "S", "P", "P", "P"]
GT = "Shubman Gill(c),Jos Buttler(†),Sai Sudharsan,Glenn Phillips,Shahrukh Khan,Rahul Tewatia,Washington Sundar,Rashid Khan,Kagiso Rabada,Mohd Siraj,Prasidh Krishna"
GTBowl = [0, 0, 0.4, 0.75, 0, 0.75, 0.75, 0.95, 0.95, 0.9, 0.8]
GTType = [None, None, "S", "S", None, "S", "S", "S", "P", "P", "P"]
RR = "Yashasvi Jaiswal,Sanju Samson(c)(†),Nitish Rana,Shimron Hetmyer,Riyan Parag,Shubham Dubey,Wanindu Hasaranga,Jofra Archer,Sandeep Sharma,Akash Madhwal,Maheesh Theekshana"
RRBowl = [0, 0, 0.5, 0, 0.7, 0, 0.85, 0.9, 0.85, 0.8, 0.9]
RRType = [None, None, "S", None, "S", None, "S", "P", "P", "P", "S"]
SRH = "Abhishek Sharma,Travis Head,Ishan Kishan(†),Abhinav Manohar,Heinrich Klaasen,Nitish Kumar Reddy,Pat Cummins(c),Harshal Patel,Mohammed Shami,Adam Zampa,Jaydev Unadkat"
SRHBowl = [0.3, 0.3, 0, 0, 0, 0.7, 0.9, 0.9, 0.9, 0.9, 0.75]
SRHType = ["S", "S", None, None, None, "P", "P", "P", "P", "S", "P"]
PK = "Prabhsimran Singh,Josh Inglis(†),Shreyas Iyer(c),Nehal Wadhera,Glenn Maxwell,Marcus Stoinis,Shashank Singh,Marco Jansen,Yash Thakur,Arshdeep Singh,Yuzi Chahal"
PKBowl = [0, 0, 0, 0.2, 0.7, 0.75, 0, 0.85, 0.85, 0.95, 0.95]
PKType = [None, None, None, "S", "S", "P", None, "P", "P", "P", "S"]
RCBW = "Grace Harris,Smriti Mandhana(c),Dayalan Hemalatha,Richa Ghosh(†),Radha Yadav,Nadine de Klerk,Arundhati Reddy,Shreyanka Patil,Prema Rawat,Linsey Smith,Lauren Bell"
RCBWBowl = [0.2, 0, 0.3, 0, 0.85, 0.75, 0.85, 0.9, 0.8, 0.9, 0.95]
RCBWType = ["P", None, "S", None, "S", "P", "P", "S", "S", "S", "P"]
MIW = "Amelia Kerr,Gunalan Kamalini(†),Nat Sciver-Brunt,Harmanpreet Kaur(c),Nicola Carey,Sajeevan Sajana,Amanjot Kaur,Poonam Khemnar,Shabnim Ismail,Sanskriti Gupta,Saika Ishaque"
MIWBowl = [0.9, 0, 0.8, 0.3, 0.7, 0.8, 0.75, 0.4, 0.95, 0.85, 0.9]
MIWType = ["S", None, "P", None, "P", "S", "P", "S", "P", "S", "S"]
GGW = "Beth Mooney(†),Sophie Devine,Anushka Sharma,Ashleigh Gardner(c),Georgia Wareham,Bharti Fulmali,Kanika Ahuja,Kashvee Gautam,Tanuja Kanwar,Rajeshwari Gayakwad,Renuka Singh"
GGWBowl = [0, 0.4, 0, 0.85, 0.9, 0, 0.5, 0.9, 0.85, 0.95, 0.95]
GGWType = [None, None, None, "S", "S", None, "S", "P", "S", "S", "P"]
UPWW = "Kiran Navgire,Meg Lanning(c),Phoebe Litchfield,Harleen Deol,Deepti Sharma,Shweta Sehrawat(†),Deandra Dottin,Sophie Ecclestone,Asha Sobhana,Shikha Pandey,Kranti Gaud"
UPWWBowl = [0, 0, 0, 0.3, 0.85, 0, 0.8, 0.95, 0.9, 0.85, 0.75]
UPWWType = [None, None, None, None, "S", None, "P", "S", "S", "P", "S"]
DCW = "Lizelle Lee(†),Shafali Verma,Laura Wolvaardt,Chinelle Henry,Jemimah Rodrigues(c),Marizanne Kapp,Sneh Rana,Niki Prasad,Minnu Mani,Nallapureddy Charani,Nandani Sharma"
DCWBowl = [0, 0, 0, 0.6, 0, 0.9, 0.85, 0.7, 0.8, 0.85, 0.9]
DCWType = [None, None, None, "P", None, "P", "S", "S", "S", "S", "P"]

print("Pre defined Teams - New Zealand, Australia, India, England, South Africa(SA), West Indies(WI), PeanutButter(PB), DahliaXI, Beatles, WomenArtist(WA), ModernFamily(MF), SDS, WeatherXI, Hilarious, RCB, MI, CSK, SRH, KKR, GT, LSG, PK, RR, DC")
Teams = [NewZealandT20, NewZealandODI, NewZealandTest, NewZealandT20Women, NewZealandODIWomen, NewZealandTestWomen, AustraliaODI, AustraliaT20, AustraliaTest, AustraliaAllTimeTest, AustraliaODIWomen, AustraliaT20Women, AustraliaTestWomen, IndiaODI, IndiaT20, IndiaTest, IndiaAllTimeTest, IndiaODIWomen, IndiaT20Women, IndiaTestWomen, EnglandT20, EnglandODI, EnglandTest, EnglandAllTimeTest, EnglandT20Women, EnglandODIWomen, EnglandTestWomen, SouthAfricaT20, SouthAfricaODI, SouthAfricaTEST, SouthAfricaAllTimeTEST, SouthAfricaAllTimeODI, SouthAfricaAllTimeT20, SouthAfricaT20Women, SouthAfricaODIWomen, SouthAfricaTESTWomen, WestIndiesAllTimeTest, PeanutButter, DahliaXI, Beatles, WomenArtist, ModernFamily, SDS, WeatherXI, HilariousXI, RCB, MI, CSK, SRH, KKR, GT, LSG, PK, RR, DC, RCBW, MIW, DCW, GGW, UPWW]
TeamBowl = [NZT20Bowl, NZODIBowl, NZTestBowl, NZT20WBowl, NZODIWBowl, NZTestWBowl, AUSODIBowl, AUST20Bowl, AUSTestBowl, AUSATTestBowl, AUSODIWBowl, AUST20WBowl, AUSTestWBowl, INDODIBowl, INDT20Bowl, INDTestBowl, INDATTestBowl, INDODIWBowl, INDT20WBowl, INDTestWBowl, ENGT20Bowl, ENGODIBowl, ENGTestBowl, ENGATTestBowl, ENGT20WBowl, ENGODIWBowl, ENGTestWBowl, SAT20Bowl, SAODIBowl, SATestBowl, SAATTestBowl, SAATODIBowl, SAATT20Bowl, SAT20WBowl, SAODIWBowl, SATestWBowl, WIATTestBowl, PBBowl, DahliaBowl, BeatlesBowl, WABowl, MFBowl, SDSBowl, WeatherBowl, HilariousBowl, RCBBowl, MIBowl, CSKBowl, SRHBowl, KKRBowl, GTBowl, LSGBowl, PKBowl, RRBowl, DCBowl, RCBWBowl, MIWBowl, DCWBowl, GGWBowl, UPWWBowl]
TeamType = [NZT20Type, NZODIType, NZTestType, NZT20WType, NZODIWType, NZTestWType, AUSODIType, AUST20Type, AUSTestType, AUSATTestType, AUSODIWType, AUST20WType, AUSTestWType, INDODIType, INDT20Type, INDTestType, INDATTestType, INDODIWType, INDT20WType, INDTestWType, ENGT20Type, ENGODIType, ENGTestType, ENGATTestType, ENGT20WType, ENGODIWType, ENGTestWType, SAT20Type, SAODIType, SATestType, SAATTestType, SAATODIType, SAATT20Type, None, None, None, WIATTestType, None, DahliaType, None, None, None, SDSType, None, HilariousType, RCBType, MIType, CSKType, SRHType, KKRType, GTType, LSGType, PKType, RRType, DCType, RCBWType, MIWType, DCWType, GGWType, UPWWType]
t = ["NZT20", "NZODI", "NZTEST", "NZWT20", "NZWODI", "NZWTEST", "AUSODI", "AUST20", "AUSTEST", "AUSATTEST", "AUSWODI", "AUSWT20", "AUSWTEST", "INDODI", "INDT20", "INDTEST", "INDATTEST", "INDWODI", "INDWT20", "INDWTEST", "ENGT20", "ENGODI", "ENGTEST", "ENGATTEST", "ENGWT20", "ENGWODI", "ENGWTEST", "SAT20", "SAODI", "SATEST", "SAATTEST", "SAATODI", "SAATT20", "SAWT20", "SAWODI", "SAWTEST", "WIATTEST", "PB", "DAHLIAXI", "BEATLES", "WA", "MF", "SDS", "WEATHER", "HILARIOUS", "RCB", "MI", "CSK", "SRH", "KKR", "GT", "LSG", "PK", "RR", "DC", "RCBW", "MIW", "DCW", "GGW", "UPWW"]
def removeCap(s):
    return s.replace("(c)", "")

def isInt(p):
    return type(p) == int

def total(A):
    return sum(A) - 5*A.count(5)

def BallsToOvers(b):
    return str(b//6) + "." + str(b%6)

def Bernoulli(p):
    if random.random() < p:
        return 1
    return 0

# ith index gets k times the weight
def weighted_choice(i, k):
    numbers = list(range(11))  # 0 through 10
    weights = [1] * 11         # Start with equal weights
    weights[i] = k
    return random.choices(numbers, weights=weights, k=1)[0]

def Toss():
    if Bernoulli(0.5) == 1:
        return "H"
    return "T"

# Prints scoreline of series as it is going on.
def seriesGoing(S, N):
    K = list(S.keys())
    if S[K[0]] > S[K[1]]:
        print(K[0] + " leads by " + str(S[K[0]]) + " - " + str(S[K[1]]))
    if S[K[0]] < S[K[1]]:
        print(K[1] + " leads by " + str(S[K[1]]) + " - " + str(S[K[0]]))
    if S[K[0]] == S[K[1]]:
        print(N + " is level at " + str(S[K[0]]) + " - " + str(S[K[1]]))

# Prints scoreline of finished series.
def seriesOutput(S, N):
    K = list(S.keys())
    if S[K[0]] > S[K[1]]:
        print(K[0] + " wins " + N + " by " + str(S[K[0]]) + " - " + str(S[K[1]]))
    if S[K[0]] < S[K[1]]:
        print(K[1] + " wins " + N + " by " + str(S[K[1]]) + " - " + str(S[K[0]]))
    if S[K[0]] == S[K[1]]:
        print(N + " is drawn at " + str(S[K[0]]) + " - " + str(S[K[1]]))

class Bowler:
    def __init__(self):
        self.Economy = None
        self.Overs = None
        self.Runs = None
        self.Wickets = None
        self.Average = None
        self.Figures = None
        self.Sixes = None
        self.Fours = None
    def makeStats(self, B):
        Balls = len(B)
        self.Runs = sum(B) - 5*B.count(5)
        self.Economy = round(self.Runs/Balls * 6, 2)
        self.Overs = str(int(Balls/6)) + "." + str(Balls%6)
        self.Wickets = B.count(5)
        if self.Wickets != 0:
            self.Average = round(self.Runs/self.Wickets, 2)
        else:
#           self.Average = self.Runs
            self.Average = None
        self.Figures = 10000*self.Wickets + 1000 - self.Runs
        self.Sixes = B.count(6)
        self.Fours = B.count(4)
    def printStats(self):
        print(self.Overs + "-" + str(self.Runs) + "-" + str(self.Wickets) + "-" + str(self.Economy))

class Batter:
    def __init__(self):
        self.runs = 0
        self.strikerate = 0
        self.average = 0
        self.consistency = 0
        self.sixes = 0
        self.fours = 0
    def makeStats(self, Batting):
        Total = 0
        Wickets = 0
        Scores = []
        TotalS = 0
        for i in range(0, len(Batting)):
            if isInt(Batting[i]):
                Total += Batting[i]
                TotalS += Batting[i]
            else:
                Wickets += 1
                Scores.append(TotalS)
                TotalS = 0
        if Batting == []:
            self.average = 0
            self.runs = 0
            self.strikerate = 0
            self.sixes = 0
            self.fours = 0
            return
        if isInt(Batting[-1]):
            Scores.append(TotalS)
        if Wickets != 0:
            self.average = round(Total/Wickets, 2)
        else:
            self.average = Total
        self.runs = Total
        if len(Batting) != 0:
            self.strikerate = round(Total/len(Batting) * 100, 2)
        else:
            self.strikerate = 0
        if Wickets <= 1:
            self.consistency = Total
        elif statistics.stdev(Scores) == 0:
            self.consistency = Total
        else:
            self.consistency = 1/statistics.stdev(Scores)
        self.sixes = Batting.count(6)
        self.fours = Batting.count(4)


A_Team = []
A_Bowl = []
B_Team = []
B_Bowl = []
for i in range(0, 11):
    A_Team.append("A" + str(i + 1))
    B_Team.append("B" + str(i + 1))
    if i <= 5:
        A_Bowl.append(0)
        B_Bowl.append(0)
    if i > 5:
        A_Bowl.append(i/10)
        B_Bowl.append(i/10)
B_Bowl[5] = 0.5
B_Bowl[-1] = 0.99
A_Bowl[-1] = 0.99

def DistBowl(Team, Bowl, Overs):
    S = 0
    counter = 0
    D = dict(sorted(dict(zip(Team, Bowl)).items(), key=lambda x: x[1], reverse= True))
    T = list(D.keys())
    B = list(D.values())
    DOut = {}
    MaxPer = int(Overs/5)
    for i in range(0, len(T)):
        DOut[T[i]] = 0
    j = 0
    while S < Overs:
        counter += 1
        ma = min(MaxPer, Overs - S + DOut[T[j]])
        mi = DOut[T[j]]
        K = True
        while K:
            if ma < mi:
                j += 1
                j = j % len(T)
                K = False
                break
            c = Bernoulli(B[j])
            if c == 1:
                ex = DOut[T[j]]
                DOut[T[j]] = ma
                S = S - ex + ma
                j += 1
                j = j % len(T)
                K = False
            else:
                ma -= 1
    return DOut

def DistBowlTest(Team, Bowl, Overs):
     Curr = random.choices(Team, weights = Bowl, k = 1)[0]
     D = {}
     D[Curr] = 1
     Count = 1
     while Count < Overs:
         L = []
         Lw = []
         Count += 1
         for i in range(0, len(Team)):
             if Team[i] != Curr:
                 L.append(Team[i])
                 Lw.append(Bowl[i])
         Curr = random.choices(L, weights = Lw, k = 1)[0]
         try:
             D[Curr] += 1
         except:
             D[Curr] = 1
     return D

def generate_bowling_order(player_overs):
    # Create a list of players with their overs left
    overs_left = [(player, overs) for player, overs in player_overs.items()]
    # Sort players by the number of overs in descending order
    overs_left.sort(key=lambda x: x[1], reverse=True)

    bowling_order = []

    while any(overs > 0 for _, overs in overs_left):
        for i, (player, overs) in enumerate(overs_left):
            if overs > 0 and (not bowling_order or bowling_order[-1] != player):
                # Add the player to the bowling order
                bowling_order.append(player)
                # Decrease the overs for this player
                overs_left[i] = (player, overs - 1)
                break
        # Re-sort the list to prioritize players with the most overs left
        overs_left.sort(key=lambda x: x[1], reverse=True)
    print()
    return bowling_order

# Prob is the array with probability distribution of 1 to 6.
def dice(Prob):
    return Prob[random.randint(0, len(Prob) - 1)]

# Merge D2 to D1
def mergeDict(D1, D2):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x].extend(D2[x])
        except:
            D[x] = D2[x]
    return D

# Merge D2 to D1, with an i to indicate match number
def mergeDict_i(D1, D2, i):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x + "_" + str(i)].extend(D2[x + "_" + str(i)])
        except:
            D[x + "_" + str(i)] = D2[x + "_" + str(i)]
    return D

def addDict(D1, D2):
    D = copy.deepcopy(D1)
    for x in D2.keys():
        try:
            D[x] += D2[x]
        except:
            D[x] = D2[x]
    return D

def dict_arrange(d):
    d1 = list(d.values())
    d1.sort()
    de = d1[::-1]
    ar = []
    for i in range(0, len(d1)):
        for j in d:
            if d[j] == de[i]:
                ar.append(j)
    return ar

def showStats(D, cut = None, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(round(V[i], 2)))
    else:
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(round(V[i], 2)))

def convertToFig(N):
    Wickets = N//10000 - 1
    Runs = 10000 * (Wickets + 1) + 1000 - N
    return str(Wickets) + "/" + str(Runs)

def showFigures(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if len(K[0].split("_")) == 2:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]))
    else:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))

def showFiguresTournament(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3])

    else:
        for i in range(cut):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3])


def showFiguresTournamentTest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))
    else:
        for i in range(min(cut, len(K))):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + convertToFig(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))

def showHighest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if len(K[0].split("_")) == 2:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]))
    else:
        if cut == None:
            for i in range(len(K)):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))
        else:
            for i in range(cut):
                A = K[i].split("_")
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - Match " + str(A[1]) + " - Innings " + str(A[2]))

def showHighestTournament(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + str(A[2]) + " vs " + str(A[3]))
    else:
        for i in range(cut):
            A = K[i].split("_")
            if len(A) == 3:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + str(A[2]) + " vs " + str(A[3]))

def showHighestTournamentTest(D, cut = 15, Reverse = True):
    DA = sorted(D.items(), key=lambda x: x[1], reverse= Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())
    if cut == None:
        for i in range(len(K)):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))
    else:
        for i in range(min(cut, len(K))):
            A = K[i].split("_")
            if len(A) == 4:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " vs " + str(A[2]) + " - Innings " + str(A[3]))
            else:
                print(str(i + 1) + ") " + str(A[0]) + " - " + str(V[i]) + " - " + str(A[1]) + " - " + A[2] + " vs " + A[3] + " - Innings " + str(A[4]))

def numFifties(D, cut = 15, Reverse = True):
    K = list(D.keys())
    V = list(D.values())
    D = {}
    for i in range(len(K)):
        A = K[i].split("_")[0]
        if V[i] >= 50 and V[i] < 100:
            try:
                D[A] += 1
            except:
                D[A] = 1
    DA = sorted(D.items(), key=lambda x: x[1], reverse=Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())

    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))
    else:
        if cut > len(K):
            cut = len(K)
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))


def numHundreds(D, cut=15, Reverse=True):
    K = list(D.keys())
    V = list(D.values())
    D = {}
    for i in range(len(K)):
        A = K[i].split("_")[0]
        if V[i] >= 100:
            try:
                D[A] += 1
            except:
                D[A] = 1
    DA = sorted(D.items(), key=lambda x: x[1], reverse=Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())

    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))
    else:
        if cut > len(K):
            cut = len(K)
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))

def numFifers(D, cut = 15, Reverse = True):
    K = list(D.keys())
    V = list(D.values())
    D = {}
    for i in range(len(K)):
        A = K[i].split("_")[0]
        v = V[i]//10000 - 1
        if v >= 5:
            try:
                D[A] += 1
            except:
                D[A] = 1

    DA = sorted(D.items(), key=lambda x: x[1], reverse=Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())

    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))
    else:
        if cut > len(K):
            cut = len(K)
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))

def numThreefers(D, cut = 15, Reverse = True):
    K = list(D.keys())
    V = list(D.values())
    D = {}
    for i in range(len(K)):
        A = K[i].split("_")[0]
        v = V[i]//10000 - 1
        if v >= 3 and v < 5:
            try:
                D[A] += 1
            except:
                D[A] = 1

    DA = sorted(D.items(), key=lambda x: x[1], reverse=Reverse)
    D = dict(DA)
    K = list(D.keys())
    V = list(D.values())

    if cut == None:
        for i in range(len(K)):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))
    else:
        if cut > len(K):
            cut = len(K)
        for i in range(cut):
            print(str(i + 1) + ") " + str(K[i]) + " - " + str(V[i]))


def getBalls(Balls, Prob):
    A = []
    count = 0
    for i in range(0, Balls):
        K = dice(Prob)
        A.append(K)
        if K == 5:
            count += 1
        if count == 10:
            return A
    return A

def getBallsTest(Prob):
    A = []
    count = 0
    while count < 10:
        K = dice(Prob)
        A.append(K)
        if K == 5:
            count += 1
        if count == 10:
            return A
    return A

# Here, Balls is the getBalls output, aka array of balls. Order is bowling order
def bowlingStats(Order, Balls):
    D = {}
    for i in range(len(Balls)):
        try:
            D[Order[i//6]].append(Balls[i])
        except:
            D[Order[i//6]] = [Balls[i]]
    bowlers = list(D.keys())
    F = {}
    for i in range(len(D)):
        init = Bowler()
        init.makeStats(D[bowlers[i]])
        F[bowlers[i]] = init
    return F, D

Basic = [0, 1, 2, 3, 4, 5, 6]

def outType(P="P"):
    if P == "S":
        P = [0.25, 0.25, 0.25, 0.25]
        A = ["c", "b", "lbw", "st"]
        return random.choices(A, P, k = 1)[0]
    else:
        P = [0.33, 0.33, 0.33]
        A = ["c", "b", "lbw"]
        return random.choices(A, P, k=1)[0]


#D = bowlingStats(generate_bowling_order(DistBowl(A_Team, A_Bowl, 20)), getBalls(120, Basic))

def BattingOrder(Team, Bowling, Balls):
    Curr = Team[0]
    Curr_i = 0
    Non = Team[1]
    Non_i = 1
    D = {}
    D[Curr] = []
    D[Non] = []
    FOW = {}
    Wicket = 1
    Part = 0
    B = 0
    for i in range(len(Balls)):
        B += 1
        if Balls[i] == 5:
            D[Curr].append(Bowling[int(i/6)])
            Curr_i = max(Curr_i, Non_i) + 1
            FOW[Wicket] = [Curr, Part, B]
            Wicket += 1
            Part = 0
            B = 0
            try:
                Curr = Team[Curr_i]
                D[Curr] = []
            except:
                x = 5
        else:
            D[Curr].append(Balls[i])
            Part += Balls[i]
            if Balls[i] % 2 == 1:
                New = Curr
                New_i = Curr_i
                Curr = Non
                Curr_i = Non_i
                Non = New
                Non_i = New_i
        if (i + 1)%6 == 0:
            New = Curr
            New_i = Curr_i
            Curr = Non
            Curr_i = Non_i
            Non = New
            Non_i = New_i
    return D, FOW

# Balls is getBalls output, which we truncate, and Total is the opponent score
def SecondBalls(Balls, Total):
    if total(Balls) <= Total:
        return Balls
    T = 0
    B = []
    for i in range(0, len(Balls)):
        if T <= Total:
            if Balls[i] != 5:
                T += Balls[i]
            B.append(Balls[i])
        if T > Total:
            return B
    return B

def Combinations(A):
    B = []
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            B.append([A[i], A[j]])
    return random.sample(B, len(B))

def MatchLimitedOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, Format):
    Batting_Score_1 = {}
    Batting_Score_2 = {}
    Balls_Score_1 = {}
    Balls_Score_2 = {}
    Batting_Sheet = {}
    Bowling_Perf = {}
    Bowling_1 = {}
    Bowling_2 = {}
    Prob = t20
    Overs = 20
    if Format.upper() == "T20":
        Overs = 20
        Prob = t20
    if Format.upper() == "ODI":
        Overs = 50
        Prob = ODI
    if Format.upper() == "CUSTOM":
        Prob = ODI
        Overs = int(input("Number of Overs : "))
    t = input(Name_1 + "'s Call : ")
    K = ["H", "T"]
    if t.upper() not in K:
        t = K[random.randint(0, 1)]
    if t.upper() == Toss():
        T1 = input(Name_1 + " chooses to : ").upper()
        while (T1.upper() not in ["BAT", "BOWL"]):
            T1 = input(Name_1 + " chooses to : ").upper()
        if T1 == "BOWL":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Type_3 = Type_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Type_1 = Type_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
            Type_2 = Type_3
    else:
        T2 = input(Name_2 + " chooses to : ").upper()
        while (T2.upper() not in ["BAT", "BOWL"]):
            T2 = input(Name_2 + " chooses to : ").upper()
        if T2 == "BAT":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Type_3 = Type_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Type_1 = Type_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
            Type_2 = Type_3


    ### First Innings
    # Bowling Team Distribution
    Bowl_Dist = DistBowl(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Batting_Balls = getBalls(6*Overs, Prob)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        try:
            Bowling_Perf[Keys[i]].extend(D[Keys[i]])
        except:
            Bowling_Perf[Keys[i]] = D[Keys[i]]
    for i in range(len(Keys)):
        Bowling_1[Keys[i]] = D[Keys[i]]
    Team_2_WK_Index = None
    for i in range(len(Team_2)):
        if Team_2[i][-2] == "†":
            Team_2_WK_Index = i
            break
    print(150*"-")
    print(Name_1 + (85 - len(Name_1)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4 * " " + "4s" + 13 * " " + "6s")
    print(150*"-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-") + (15 - 1)*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = 0
            Balls_Score_1[Team_1[i]] = 0
            Batting_Sheet[Team_1[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A)/float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = sum(A)
            Balls_Score_1[Team_1[i]] = len(A)
            Batting_Sheet[Team_1[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_2[Team_2.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")
            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
#                D = Team_2[random.randint(0, 10)]
                D = Team_2[weighted_choice(Team_2_WK_Index, 2)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " +  " b " + w + (19 - len(w)) * " "
            print(Team_1[i] + (35 - len(Team_1[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = Runs
            Balls_Score_1[Team_1[i]] = Balls
            Batting_Sheet[Team_1[i]] = A
    print(150 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150*"-")
    T1 = total(Batting_Balls)
    B1 = Overs * 6
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)
    print(pd.DataFrame({"Name" : Name, "Overs" : Over, "Runs" : Runs, "Wickets" : Wickets, "Economy" : Economy, "Fours" : Fours, "Sixes" : Sixes}))
    print(" ")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")

    X = input("Continue ? : ")
    print(" ")
    ### Second Innings
    # Bowling Team Distribution
    if Format.upper() == "ODI":
        if T1 > 300:
            Prob = ODI_target
        if T1 < 235:
            Prob = ODI_target_2
    if Format.upper() == "T20":
        if T1 >= 190 and T1 < 220:
            Prob = t20_target
        if T1 >= 220:
            Prob = t20_target_extreme
        if T1 <= 135:
            Prob = t20_target_2
    Bowl_Dist = DistBowl(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Batting_Balls = getBalls(6 * Overs, Prob)
    Batting_Balls = SecondBalls(Batting_Balls, T1)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        try:
            Bowling_Perf[Keys[i]].extend(D[Keys[i]])
        except:
            Bowling_Perf[Keys[i]] = D[Keys[i]]
    for i in range(len(Keys)):
        Bowling_2[Keys[i]] = D[Keys[i]]

    Team_1_WK_Index = None
    for i in range(len(Team_1)):
        if Team_1[i][-2] == "†":
            Team_1_WK_Index = i
            break
    print(150 * "-")
    print(Name_2 + (85 - len(Name_2)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4 * " " + "4s" + 13 * " " + "6s")
    print(150 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-") + (15 - 1)* " " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = 0
            Balls_Score_2[Team_2[i]] = 0
            Batting_Sheet[Team_2[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))* " " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = sum(A)
            Balls_Score_2[Team_2[i]] = len(A)
            Batting_Sheet[Team_2[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_1[Team_1.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")
            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
#                D = Team_1[random.randint(0, 10)]
                D = Team_1[weighted_choice(Team_1_WK_Index, 2)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " + " b " + w + (19 - len(w)) * " "
#            print(Team_2[i] + (25 - len(Team_2[i])) * " " + W + (50 - len(W)) * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs/float(Balls)))))*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            print(Team_2[i] + (35 - len(Team_2[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = Runs
            Balls_Score_2[Team_2[i]] = Balls
            Batting_Sheet[Team_2[i]] = A
    print(150 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150 * "-")
    Total = 0
    Balls = 0
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)
    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy, "Fours" : Fours, "Sixes" : Sixes}))
    T2 = total(Batting_Balls)
    B2 = len(Batting_Balls)
    print(" ")
    Winner = None
    if T1 > T2:
        print(Name_1 + " wins by " + str(T1 - T2) + " runs!")
        Winner = Name_1
    if T1 == T2:
        print("It's a draw!!!")
        Winner = None
    if T1 < T2:
        print(Name_2 + " wins by " + str(10 - Batting_Balls.count(5)) + " wickets!")
        Winner = Name_2
    Impact_Points = {}
    for i in range(0, len(Team_1)):
        try:
            Impact_Points[Team_1[i]] = Batting_Score_1[Team_1[i]]**2 / Balls_Score_1[Team_1[i]]
            if Batting_Score_1[Team_1[i]] >= 50:
                Impact_Points[Team_1[i]] += 25
            if Batting_Score_1[Team_1[i]] >= 100:
                Impact_Points[Team_1[i]] += 75
        except:
            x = 5
        try:
            A = Bowling_2[Team_1[i]]
            if Team_1[i] in Impact_Points.keys():
                if Format == "T20":
                    Impact_Points[Team_1[i]] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[Team_1[i]] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[Team_1[i]] += 25
                if A.count(5) >= 5:
                    Impact_Points[Team_1[i]] += 75
            else:
                if Format == "T20":
                    Impact_Points[Team_1[i]] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[Team_1[i]] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[Team_1[i]] += 25
                if A.count(5) >= 5:
                    Impact_Points[Team_1[i]] += 75
        except:
            x = 5

    for i in range(0, len(Team_2)):
        try:
            if Team_2[i] in Impact_Points.keys():
                Impact_Points[Team_2[i]] += Batting_Score_2[Team_2[i]]**2 / Balls_Score_2[Team_2[i]]
                if Batting_Score_2[Team_2[i]] >= 50:
                    Impact_Points[Team_2[i]] += 25
                if Batting_Score_2[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 75
            else:
                Impact_Points[Team_2[i]] = Batting_Score_2[Team_2[i]] ** 2 / Balls_Score_2[Team_2[i]]
                if Batting_Score_2[Team_2[i]] >= 50:
                    Impact_Points[Team_2[i]] += 25
                if Batting_Score_2[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 75
        except:
            x = 5
        try:
            A = Bowling_1[Team_2[i]]
            if Team_2[i] in Impact_Points.keys():
                if Format == "T20":
                    Impact_Points[Team_2[i]] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[Team_2[i]] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[Team_2[i]] += 25
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 75
            else:
                if Format == "T20":
                    Impact_Points[Team_2[i]] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[Team_2[i]] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[Team_2[i]] += 25
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 75
        except:
            x = 5
    if Winner == Name_1:
        for i in range(len(Team_1)):
            try:
                if Format == "T20":
                    Impact_Points[Team_1[i]] += 100
                if Format == "ODI":
                    Impact_Points[Team_1[i]] += 250
            except:
                if Format == "T20":
                    Impact_Points[Team_1[i]] = 100
                if Format == "ODI":
                    Impact_Points[Team_1[i]] = 250
    if Winner == Name_2:
        for i in range(len(Team_2)):
            try:
                if Format == "T20":
                    Impact_Points[Team_2[i]] += 100
                if Format == "ODI":
                    Impact_Points[Team_2[i]] += 250
            except:
                if Format == "T20":
                    Impact_Points[Team_2[i]] = 100
                if Format == "ODI":
                    Impact_Points[Team_2[i]] = 250

    Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
    Impact_Sorted = list(Impact_Sorted_Dict.keys())
    print("")
    if Impact_Sorted[0] in Team_1:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_1 + ")")
    else:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_2 + ")")
    print("")
    """
    if Impact_Sorted[-1] in Team_1:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
    else:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
    print("")
    """
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20*" " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")
        print(" ")
    NRR_Dict = {}
    NRR_Dict[Name_1] = [T1, B1]
    if Winner == Name_1:
        NRR_Dict[Name_2] = [T2, B1]
    else:
        NRR_Dict[Name_2] = [T2, B2]
    return Winner, Batting_Score_1, Batting_Score_2, Balls_Score_1, Balls_Score_2, Bowling_1, Bowling_2, Batting_Sheet, Bowling_Perf, NRR_Dict

#Format = input("Format : ").upper()
#MatchLimitedOne("A", A_Team, A_Bowl, "B", B_Team, B_Bowl, Format)

def MatchTestOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, P_death = None, P_mine = None, P_norm = None, P_high = None):
    Batting_Score_1 = {}
    Batting_Score_2 = {}
    Batting_Score_3 = {}
    Batting_Score_4 = {}
    Batting_Sheet = {}
#    Bowling_Perf = {}
    Bowling_1 = {}
    Bowling_2 = {}
    Bowling_3 = {}
    Bowling_4 = {}
    Prob = Tests
    if P_mine == None:
        P_death = 1/4
        P_mine = 1/4
        P_norm = 1/4
        P_high = 1/4
    R = random.random()
    if R < P_mine:
        Prob = Tests_Mine
        print("Match Conditions - Dusty pitch")
    elif R < P_mine + P_norm:
        Prob = Tests
        print("Match Conditions - Green pitch")
    elif R < P_mine + P_norm + P_death:
        Prob = Tests_Death
        print("Match Conditions - Death Pitch")
    else:
        Prob = Tests_High
        print("Match Conditions - Highway pitch")
    print("")
    t = input(Name_1 + "'s Call : ")
    K = ["H", "T"]
    if t.upper() not in K:
        t = K[random.randint(0, 1)]
    if t.upper() == Toss():
        T1 = input(Name_1 + " chooses to : ").upper()
        while (T1.upper() not in ["BAT", "BOWL"]):
            T1 = input(Name_1 + " chooses to : ").upper()
        if T1 == "BOWL":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Type_3 = Type_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Type_1 = Type_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
            Type_2 = Type_3
    else:
        T2 = input(Name_2 + " chooses to : ").upper()
        while (T2.upper() not in ["BAT", "BOWL"]):
            T2 = input(Name_2 + " chooses to : ").upper()
        if T2 == "BAT":
            Name_3 = Name_1
            Team_3 = Team_1
            Bowl_3 = Bowl_1
            Type_3 = Type_1
            Name_1 = Name_2
            Team_1 = Team_2
            Bowl_1 = Bowl_2
            Type_1 = Type_2
            Name_2 = Name_3
            Team_2 = Team_3
            Bowl_2 = Bowl_3
            Type_2 = Type_3


    ### First Innings
    # Bowling Team Distribution
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls)//6 + 2
    Bowl_Dist = DistBowlTest(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)
    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_1[Keys[i]] = D[Keys[i]]
    Team_2_WK_Index = None
    for i in range(len(Team_2)):
        if Team_2[i][-2] == "†":
            Team_2_WK_Index = i
            break
    print(150*"-")
#    print(Name_1)
    print(Name_1 + (85 - len(Name_1)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4*" " + "4s" + 13*" " + "6s")
    print(150*"-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-") + (15 - 1)*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = 0
            Batting_Sheet[Team_1[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A)/float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = sum(A)
            Batting_Sheet[Team_1[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_2[Team_2.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")

            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
#                D = Team_2[random.randint(0, 10)]
                D = Team_2[weighted_choice(Team_2_WK_Index, 4)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " + " b " + w + (19 - len(w)) * " "
            print(Team_1[i] + (35 - len(Team_1[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            Batting_Score_1[Team_1[i]] = Runs
            Batting_Sheet[Team_1[i]] = A
    print(150 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150*"-")
    T1 = total(Batting_Balls)
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)

    print(pd.DataFrame({"Name" : Name, "Overs" : Over, "Runs" : Runs, "Wickets" : Wickets, "Economy" : Economy, "Fours" : Fours, "Sixes" : Sixes}))
    print(" ")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")
        print("")
    X = input("Continue ? : ")
    print(" ")

    ### Second Innings
    # Bowling Team Distribution
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls)//6 + 2
    Bowl_Dist = DistBowlTest(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_2[Keys[i]] = D[Keys[i]]

    Team_1_WK_Index = None
    for i in range(len(Team_1)):
        if Team_1[i][-2] == "†":
            Team_1_WK_Index = i
            break
    print(150 * "-")
    print(Name_2 + (85 - len(Name_2)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4 * " " + "4s" + 13 * " " + "6s")
    print(150 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-")  + (15 - 1)*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = 0
            Batting_Sheet[Team_2[i]] = []
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))* " " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = sum(A)
            Batting_Sheet[Team_2[i]] = A
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_1[Team_1.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")
            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
#                D = Team_1[random.randint(0, 10)]
                D = Team_1[weighted_choice(Team_1_WK_Index, 4)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " + " b " + w + (19 - len(w)) * " "
            print(Team_2[i] + (35 - len(Team_2[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            Batting_Score_2[Team_2[i]] = Runs
            Batting_Sheet[Team_2[i]] = A
    print(150 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150 * "-")
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)

    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy, "Fours" : Fours, "Sixes" : Sixes}))
    T2 = total(Batting_Balls)
    print("")
    if T1 > T2:
        print(Name_1 + " leads by " + str(T1 - T2) + " runs.")
    if T1 < T2:
        print(Name_2 + " leads by " + str(T2 - T1) + " runs.")
    if T1 == T2:
        print("Scores are level.")
    print("")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    Total = 0
    Balls = 0
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")
    print(" ")
    X = input("Continue ? : ").upper()
    # Third Innings
    print(" ")
    Batting_Balls = getBallsTest(Prob)
    Overs = len(Batting_Balls) // 6 + 2
    Bowl_Dist = DistBowlTest(Team_2, Bowl_2, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_1, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())

    for i in range(len(Keys)):
        Bowling_3[Keys[i]] = D[Keys[i]]
    Team_2_WK_Index = None
    for i in range(len(Team_2)):
        if Team_2[i][-2] == "†":
            Team_2_WK_Index = i
            break
    print(150 * "-")
    print(Name_1 + (85 - len(Name_1)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4*" " + "4s" + 13*" " + "6s")
    print(150 * "-")
    for i in range(0, len(Team_1)):
        try:
            A = Batting_Stats[Team_1[i]]
        except:
            A = []
            print(Team_1[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str("-") + (15 - 1)*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            try:
                Batting_Sheet[Team_1[i]].extend([])
            except:
                Batting_Sheet[Team_1[i]] = []
            Batting_Score_3[Team_1[i]] = 0
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_1[i] + "*" + (84 - len(Team_1[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            try:
                Batting_Sheet[Team_1[i]].extend(A)
            except:
                Batting_Sheet[Team_1[i]] = A
            Batting_Score_3[Team_1[i]] = sum(A)
        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_2[Team_2.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")
            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
 #               D = Team_2[random.randint(0, 10)]
                D = Team_2[weighted_choice(Team_2_WK_Index, 4)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " + " b " + w + (19 - len(w)) * " "
            print(Team_1[i] + (35 - len(Team_1[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            try:
                Batting_Sheet[Team_1[i]].extend(A)
            except:
                Batting_Sheet[Team_1[i]] = A
            Batting_Score_3[Team_1[i]] = Runs

    print(150 * "-")
    print(Name_1 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150 * "-")
    T3 = total(Batting_Balls)
    Total = 0
    Balls = 0
    print("")
    print(Name_2 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Over = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Over.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)

    print(pd.DataFrame({"Name": Name, "Overs": Over, "Runs": Runs, "Wickets": Wickets, "Economy": Economy, "Fours" : Fours, "Sixes" : Sixes}))
    print(" ")
    if T1 + T3 < T2:
        print(Name_2 + " wins the match by an innings and " + str(T2 - T1 - T3) + " runs!")
    else:
        print("Target for " + Name_2 + " - " + str(T1 + T3 - T2 + 1) + " runs")
    if T1 + T3 >= T2:
        print(" ")
        Y = input("Fall of Wickets ? : ").upper()
        print("")
        if Y != "N":
            print(60 * "-")
            print("Fall of Wickets")
            print(60 * "-")
            for i in range(len(FOW)):
               K = FOW[i + 1]
               Total += K[1]
               Balls += K[2]
               S = str(Total) + "/" + str(i + 1)
               print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
            print(60 * "-")
            S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
            print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
            print(60 * "-")
    if T1 + T3 < T2:
        Impact_Points = {}
        for i in range(0, len(Team_1)):
            Impact_Points[Team_1[i]] = 0
            try:
                Impact_Points[Team_1[i]] += Batting_Score_1[Team_1[i]]
                if Batting_Score_1[Team_1[i]] >= 100:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5
            try:
                Impact_Points[Team_1[i]] += Batting_Score_3[Team_1[i]]
                if Batting_Score_3[Team_1[i]] >= 100:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_2[Team_1[i]]
                Impact_Points[Team_1[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_1[i]] += 25
            except:
                x = 5

        for i in range(0, len(Team_2)):
            Impact_Points[Team_2[i]] = 50
            try:
                Impact_Points[Team_2[i]] += Batting_Score_2[Team_2[i]]
                if Batting_Score_2[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                Impact_Points[Team_2[i]] += Batting_Score_4[Team_2[i]]
                if Batting_Score_4[Team_2[i]] >= 100:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_1[Team_2[i]]
                Impact_Points[Team_2[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
            try:
                A = Bowling_3[Team_2[i]]
                Impact_Points[Team_2[i]] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[Team_2[i]] += 25
            except:
                x = 5
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        if Impact_Sorted[0] in Team_1:
            print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_1 + ")")
        else:
            print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_2 + ")")
        print("")
        if Impact_Sorted[-1] in Team_1:
            print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
        else:
            print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
        print("")
        Y = input("Fall of Wickets ? : ").upper()
        print("")
        if Y != "N":
            print(60 * "-")
            print("Fall of Wickets")
            print(60 * "-")
            for i in range(len(FOW)):
                K = FOW[i + 1]
                Total += K[1]
                Balls += K[2]
                S = str(Total) + "/" + str(i + 1)
                print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")
        return Name_2, Batting_Score_1, Batting_Score_2, Batting_Score_3, Batting_Score_4, Batting_Sheet, Bowling_1, Bowling_2, Bowling_3, Bowling_4, {Name_1 : [T1 + T3, 20], Name_2 : [T2, 10]}
    X = input("Continue ? : ")
    print(" ")
    # Fourth Innings
    Batting_Balls = getBallsTest(Prob)
    Batting_Balls = SecondBalls(Batting_Balls, T1 + T3 - T2)
    Overs = len(Batting_Balls) // 6 + 2
    Bowl_Dist = DistBowlTest(Team_1, Bowl_1, Overs)
    Bowl_Order = generate_bowling_order(Bowl_Dist)
    Bowling_Stats, D = bowlingStats(Bowl_Order, Batting_Balls)
    Batting_Stats, FOW = BattingOrder(Team_2, Bowl_Order, Batting_Balls)

    Keys = list(D.keys())
    for i in range(len(Keys)):
        Bowling_4[Keys[i]] = D[Keys[i]]
    Team_1_WK_Index = None
    for i in range(len(Team_1)):
        if Team_1[i][-2] == "†":
            Team_1_WK_Index = i
            break
    print(150 * "-")
    print(Name_2 + (85 - len(Name_2)) * " " + "Runs" + (25 - 4) * " " + "Strike Rate" + 4*" " + "4s" + 13*" " + "6s")
    print(150 * "-")
    for i in range(0, len(Team_2)):
        try:
            A = Batting_Stats[Team_2[i]]
        except:
            A = []
            print(Team_2[i])
            continue
        if A == []:
            s = "0(0)"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str("-") + (15 - 1)*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            try:
                Batting_Sheet[Team_2[i]].extend([])
            except:
                Batting_Sheet[Team_2[i]] = []
            Batting_Score_4[Team_2[i]] = 0
            continue
        if isInt(A[-1]):
            s = str(sum(A)) + "(" + str(len(A)) + ")"
            print(Team_2[i] + "*" + (84 - len(Team_2[i])) * " " + s + (25 - len(s)) * " " + str(round(100 * sum(A) / float(len(A)))) + (15 - len(str(round(100 * sum(A)/float(len(A))))))*" " + str(A.count(4)) + (15 - len(str(A.count(4))))*" " + str(A.count(6)))
            try:
                Batting_Sheet[Team_2[i]].extend(A)
            except:
                Batting_Sheet[Team_2[i]] = A
            Batting_Score_4[Team_2[i]] = sum(A)

        else:
            Runs = sum(A[:-1])
            Balls = len(A)
            s = str(Runs) + "(" + str(Balls) + ")"
            W = None
            w = A[-1]
            O = None
            if Type_1[Team_1.index(w)] == "P":
                O = outType("P")
            else:
                O = outType("S")
            if O in ["b", "lbw", "st"]:
                W = O + " " + w + (19 - len(w)) * " "
            else:
#                D = Team_1[random.randint(0, 10)]
                D = Team_1[weighted_choice(Team_1_WK_Index, 4)]
                if D == w:
                    W = "c & b " + w + (19 - len(w)) * " "
                else:
                    W = "c " + D + (19 - len(D)) * " " + " b " + w + (19 - len(w)) * " "
            print(Team_2[i] + (35 - len(Team_2[i])) * " " + (45 - len(W)) * " " + W + 5 * " " + s + (25 - len(s)) * " " + str(round(100 * Runs / float(Balls))) + (15 - len(str(round(100 * Runs / float(Balls))))) * " " + str(A.count(4)) + (15 - len(str(A.count(4)))) * " " + str(A.count(6)))
            try:
                Batting_Sheet[Team_2[i]].extend(A)
            except:
                Batting_Sheet[Team_2[i]] = A
            Batting_Score_4[Team_2[i]] = Runs
    print(150 * "-")
    print(Name_2 + " score = " + str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5)) + " in " + str(len(Batting_Balls) // 6) + "." + str(len(Batting_Balls) % 6) + " overs")
    print("Run Rate = " + str(round(total(Batting_Balls) * 6 / float(len(Batting_Balls)), 2)))
    print(150 * "-")
    Total = 0
    Balls = 0
    print("")

    print(Name_1 + " Bowling")
    Name = list(Bowling_Stats.keys())
    Economy = []
    Runs = []
    Wickets = []
    Overs = []
    Sixes = []
    Fours = []
    for i in range(len(Name)):
        Economy.append(Bowling_Stats[Name[i]].Economy)
        Runs.append(Bowling_Stats[Name[i]].Runs)
        Wickets.append(Bowling_Stats[Name[i]].Wickets)
        Overs.append(Bowling_Stats[Name[i]].Overs)
        Sixes.append(Bowling_Stats[Name[i]].Sixes)
        Fours.append(Bowling_Stats[Name[i]].Fours)

    print(pd.DataFrame({"Name": Name, "Overs": Overs, "Runs": Runs, "Wickets": Wickets, "Economy": Economy, "Fours" : Fours, "Sixes" : Sixes}))
    T4 = total(Batting_Balls)
    print("")
    Winner = None
    if T1 + T3 > T2 + T4:
        print(Name_1 + " wins by " + str(T1 + T3 - T2 - T4) + " runs!")
        Winner = Name_1
    if T1 + T3 < T2 + T4:
        if Batting_Balls.count(5) != 9:
            print(Name_2 + " wins by " + str(10 - Batting_Balls.count(5)) + " wickets!")
            Winner = Name_2
        else:
            print(Name_2 + " wins by 1 wicket!")
            Winner = Name_2
    if T1 + T3 == T2 + T4:
        print("It is a tie!")
        Winner = None

    Impact_Points = {}
    for i in range(0, len(Team_1)):
        if Winner == Name_1:
            Impact_Points[Team_1[i]] = 50
        else:
            Impact_Points[Team_1[i]] = 0
        try:
            Impact_Points[Team_1[i]] += Batting_Score_1[Team_1[i]]
            if Batting_Score_1[Team_1[i]] >= 100:
                Impact_Points[Team_1[i]] += 25
        except:
            x = 5
        try:
            Impact_Points[Team_1[i]] += Batting_Score_3[Team_1[i]]
            if Batting_Score_3[Team_1[i]] >= 100:
                Impact_Points[Team_1[i]] += 25
        except:
            x = 5
        try:
            A = Bowling_2[Team_1[i]]
            Impact_Points[Team_1[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_1[i]] += 5*A.count(5)
        except:
            x = 5
        try:
            A = Bowling_4[Team_1[i]]
            Impact_Points[Team_1[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_1[i]] += 5*A.count(5)
        except:
            x = 5

    for i in range(0, len(Team_2)):
        if Winner == Name_2:
            Impact_Points[Team_2[i]] = 50
        else:
            Impact_Points[Team_2[i]] = 0
        try:
            Impact_Points[Team_2[i]] += Batting_Score_2[Team_2[i]]
            if Batting_Score_2[Team_2[i]] >= 100:
                Impact_Points[Team_2[i]] += 25
        except:
            x = 5
        try:
            Impact_Points[Team_2[i]] += Batting_Score_4[Team_2[i]]
            if Batting_Score_4[Team_2[i]] >= 100:
                Impact_Points[Team_2[i]] += 25
        except:
            x = 5
        try:
            A = Bowling_1[Team_2[i]]
            Impact_Points[Team_2[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_2[i]] += 5*A.count(5)
        except:
            x = 5
        try:
            A = Bowling_3[Team_2[i]]
            Impact_Points[Team_2[i]] += 20*A.count(5) - 0.1*total(A)
            if A.count(5) >= 5:
                Impact_Points[Team_2[i]] += 5*A.count(5)
        except:
            x = 5
    Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
    Impact_Sorted = list(Impact_Sorted_Dict.keys())
    print("")
    if Impact_Sorted[0] in Team_1:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_1 + ")")
    else:
        print("Player of the Match - " + Impact_Sorted[0] + " (" + Name_2 + ")")
    print("")
    if Impact_Sorted[-1] in Team_1:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
    else:
        print("Flog of the Match - " + Impact_Sorted[-1] + " (" + Name_2 + ")")

    print("")
    Y = input("Fall of Wickets ? : ").upper()
    print(" ")
    if Y != "N":
        print(60 * "-")
        print("Fall of Wickets")
        print(60 * "-")
        for i in range(len(FOW)):
            K = FOW[i + 1]
            Total += K[1]
            Balls += K[2]
            S = str(Total) + "/" + str(i + 1)
            print(K[0] + (25 - len(K[0])) * " " + S + (7 - len(S)) * " " + BallsToOvers(Balls))
        print(60 * "-")
        S = str(total(Batting_Balls)) + "/" + str(Batting_Balls.count(5))
        print("Total" + 20 * " " + S + (7 - len(S)) * " " + BallsToOvers(len(Batting_Balls)))
        print(60 * "-")
    print(" ")
    return Winner, Batting_Score_1, Batting_Score_2, Batting_Score_3, Batting_Score_4, Batting_Sheet, Bowling_1, Bowling_2, Bowling_3, Bowling_4, {Name_1 : [T1 + T3, 20], Name_2 : [T2 + T4, 10 + Batting_Balls.count(5)]}

#Format = input("Format ? : ").upper()
#MatchLimitedOne("Australia", AustraliaT20.split(","), AUST20Bowl, "Dahlia", DahliaXI.split(","), DahliaBowl, Format)
#MatchTestOne("Australia", AustraliaTest.split(","), AUSTestBowl, "Dahlia", DahliaXI.split(","), DahliaBowl)

def Series():
    P = input("Pre Defined or Custom ? ").upper()
    Name_1 = None
    Team_1 = None
    Bowl_1 = None
    Type_1 = None
    Name_2 = None
    Team_2 = None
    Bowl_2 = None
    Type_2 = None
    if P == "C":
        Name_2 = input("Home Team Name : ").upper()
        Team_2 = input("Home Team : ").split(",")
        Bowl_2 = input("Home Team Bowling : ").split(",")
        Type_2 = input("Home Team Bowling Type : ").split(",")
        for i in range(len(Bowl_2)):
            Bowl_2[i] = float(Bowl_2[i])

        Name_1 = input("Visiting Team Name : ").upper()
        Team_1 = input("Visiting Team : ").split(",")
        Bowl_1 = input("Visiting Team Bowling : ").split(",")
        Type_1 = input("Visiting Team Bowling Type : ").split(",")
        for i in range(len(Bowl_1)):
            Bowl_1[i] = float(Bowl_1[i])

    if P == "P":
        Name_2 = input("Home Team Name : ").upper()
        pos = t.index(Name_2)
        Team_2 = Teams[pos].split(",")
        Bowl_2 = TeamBowl[pos]
        Type_2 = TeamType[pos]

        Name_1 = input("Visiting Team Name : ").upper()
        pos = t.index(Name_1)
        Team_1 = Teams[pos].split(",")
        Bowl_1 = TeamBowl[pos]
        Type_1 = TeamType[pos]
    Series_Name = input("Series Name : ").upper()

    Format = input("Format : ").upper()
    Number = int(input("Number of matches : "))
    Score = {Name_1 : 0, Name_2 : 0}
    BattingSheet = {}
    BattingScores = {}
    BowlingStats = {}
    Figures_Bowl = {}
    if Format == "TEST":
        P_death = None
        P_mine = None
        P_norm = None
        P_high = None
        Location = input("Location : ").upper()
        if Location == "ENG":
            P_death = 0.05
            P_mine = 0.20
            P_norm = 0.55
            P_high = 0.20
        elif Location == "IND":
            P_death = 0.20
            P_mine = 0.30
            P_norm = 0.30
            P_high = 0.20
        elif Location == "DEADLY IND":
            P_death = 0.25
            P_mine = 0.55
            P_norm = 0.20
            P_high = 0.00
        elif Location == "AUS":
            P_death = 0.10
            P_mine = 0.15
            P_norm = 0.25
            P_high = 0.50
        elif Location == "SA":
            P_death = 0.20
            P_mine = 0.30
            P_norm = 0.15
            P_high = 0.35
        elif Location == "WI":
            P_death = 0.14
            P_mine = 0.16
            P_norm = 0.30
            P_high = 0.40
        elif Location == "NZ":
            P_death = 0.08
            P_mine = 0.08
            P_norm = 0.24
            P_high = 0.60
        elif Location == "DAHLIA":
            P_death = 0.5
            P_mine = 0
            P_norm = 0
            P_high = 0.5
        elif Location == "MOON":
            P_death = 1
            P_mine = 0
            P_norm = 0
            P_high = 0
        elif Location == "HIGHWAY":
            P_death = 0
            P_mine = 0
            P_norm = 0
            P_high = 1
        Impact_Points = {}
        for i in range(len(Team_1)):
            Impact_Points[Team_1[i]] = 0
        for i in range(len(Team_2)):
            Impact_Points[Team_2[i]] = 0
        for i in range(Number - 1):
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, P_death, P_mine, P_norm, P_high)
            for x in BF1.keys():
                A = BF1[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i + 1) + "_" + str(1)] = Figure
                Impact_Points[x] += 20*A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF2.keys():
                A = BF2[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(2)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF3.keys():
                A = BF3[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(3)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BF4.keys():
                A = BF4[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
                Figures_Bowl[x + "_" + str(i  + 1) + "_" + str(4)] = Figure
                Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
                if A.count(5) >= 5:
                    Impact_Points[x] += 6 * A.count(5)
                elif A.count(5) >= 3:
                    Impact_Points[x] += 3 * A.count(5)
            for x in BSco1.keys():
                A = BSco1[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(1)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                A = BSco2[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(2)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                A = BSco3[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(3)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                A = BSco4[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(4)] = A
                Impact_Points[x] += A
                if A >= 100:
                    Impact_Points[x] += 25
            if W != None:
                Score[W] += 1
            print("")
            seriesGoing(Score, Series_Name)
            print(" ")
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
 #           BattingScores = mergeDict_i(BattingScores, BSco, i + 1)
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
        W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, P_death, P_mine, P_norm, P_high)
        for x in BF1.keys():
            A = BF1[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(1)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF2.keys():
            A = BF2[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(2)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF3.keys():
            A = BF3[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(3)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BF4.keys():
            A = BF4[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number) + "_" + str(4)] = Figure
            Impact_Points[x] += 20 * A.count(5) - 0.1 * total(A)
            if A.count(5) >= 5:
                Impact_Points[x] += 6 * A.count(5)
            elif A.count(5) >= 3:
                Impact_Points[x] += 3 * A.count(5)
        for x in BSco1.keys():
            A = BSco1[x]
            BattingScores[x + "_" + str(Number) + "_" + str(1)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco2.keys():
            A = BSco2[x]
            BattingScores[x + "_" + str(Number) + "_" + str(2)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco3.keys():
            A = BSco3[x]
            BattingScores[x + "_" + str(Number) + "_" + str(3)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        for x in BSco4.keys():
            A = BSco4[x]
            BattingScores[x + "_" + str(Number) + "_" + str(4)] = A
            Impact_Points[x] += A
            if A >= 100:
                Impact_Points[x] += 25
        if W != None:
            Score[W] += 1
        if Score[Name_1] > Score[Name_2]:
            for i in range(len(Team_1)):
                Impact_Points[Team_1[i]] += 100
        if Score[Name_2] > Score[Name_1]:
            for i in range(len(Team_2)):
                Impact_Points[Team_2[i]] += 100

        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        if Impact_Sorted[0] in Team_1:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_1 + ")")
        else:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_2 + ")")
        print("")
        if Impact_Sorted[-1] in Team_1:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
        else:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
        print("")
        seriesOutput(Score, Series_Name)
        print(" ")
        BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
        BattingSheet = mergeDict(BattingSheet, BShe)
        BowlingStats = mergeDict(BowlingStats, BF)
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        ConsArray = [Batting[Batters[i]].consistency for i in range(len(Batters))]
        SixArray = [Batting[Batters[i]].sixes for i in range(len(Batters))]
        FourArray = [Batting[Batters[i]].fours for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))
        Cons = dict(zip(Batters, ConsArray))
        Six = dict(zip(Batters, SixArray))
        Four = dict(zip(Batters, FourArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
#        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets >= 1.5 * Number:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print(" ")
        print(40*"*")
        print("BATTERS")
        print(40*"*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print("")
        print("Most 50s - ")
        numFifties(BattingScores, cut = None)
        print(" ")
        print("Most 100s - ")
        numHundreds(BattingScores, cut=None)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighest(BattingScores, cut = 10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print("Most Sixes - ")
        showStats(Six, cut = 10)
        print(" ")
        print("Most Fours - ")
        showStats(Four, cut=10)
        print(" ")
        print(40*"*")
        print("BOWLERS")
        print(40*"*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Most Fifers - ")
        numFifers(Figures_Bowl, cut = None)
        print(" ")
        print("Most Threefers - ")
        numThreefers(Figures_Bowl, cut=None)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse = False)
        print(" ")
        print("Best Figures - ")
        showFigures(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

    else:
        Impact_Points = {}
        """
        for i in range(len(Team_1)):
            Impact_Points[Team_1[i]] = 0
        for i in range(len(Team_2)):
            Impact_Points[Team_2[i]] = 0
        """
        for i in range(Number - 1):
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, Format)
            if W != None:
                Score[W] += 1
            print("")
            seriesGoing(Score, Series_Name)
            print(" ")
            for x in BF.keys():
                A = BF[x]
                Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5*A.count(5))
                Figures_Bowl[x + "_" + str(i + 1)] = Figure
            for x in BSco_1.keys():
                A = BSco_1[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(1)] = A
                try:
                    Impact_Points[x] += A**2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5

            for x in BSco_2.keys():
                A = BSco_2[x]
                BattingScores[x + "_" + str(i + 1) + "_" + str(2)] = A
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_2[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 +1.5* A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75

            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
        W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(Name_1, Team_1, Bowl_1, Type_1, Name_2, Team_2, Bowl_2, Type_2, Format)
        for x in BF.keys():
            A = BF[x]
            Figure = 10000 * (A.count(5) + 1) + 1000 - (sum(A) - 5 * A.count(5))
            Figures_Bowl[x + "_" + str(Number)] = Figure
        for x in BSco_1.keys():
            A = BSco_1[x]
            BattingScores[x + "_" + str(Number) + "_" + str(1)] = A
            try:
                Impact_Points[x] += A ** 2 / Balls_1[x]
                if A >= 50:
                    Impact_Points[x] += 25
                if A >= 100:
                    Impact_Points[x] += 75
            except:
                try:
                    Impact_Points[x] = A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    x = 5
        for x in BSco_2.keys():
            A = BSco_2[x]
            BattingScores[x + "_" + str(Number) + "_" + str(2)] = A
            try:
                Impact_Points[x] += A ** 2 / Balls_2[x]
                if A >= 50:
                    Impact_Points[x] += 25
                if A >= 100:
                    Impact_Points[x] += 75
            except:
                try:
                    Impact_Points[x] = A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    x = 5
        for x in Bowler_1.keys():
            A = Bowler_1[x]
            try:
                if Format == "T20":
                    Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[x] += 25
                if A.count(5) >= 5:
                    Impact_Points[x] += 75
            except:
                if Format == "T20":
                    Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[x] += 25
                if A.count(5) >= 5:
                    Impact_Points[x] += 75
        for x in Bowler_2.keys():
            A = Bowler_2[x]
            try:
                if Format == "T20":
                    Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[x] += 25
                if A.count(5) >= 5:
                    Impact_Points[x] += 75
            except:
                if Format == "T20":
                    Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                if Format == "ODI":
                    Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                if A.count(5) >= 3:
                    Impact_Points[x] += 25
                if A.count(5) >= 5:
                    Impact_Points[x] += 75
        if W != None:
            Score[W] += 1
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        if Impact_Sorted[0] in Team_1:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_1 + ")")
        else:
            print("Player of the Series - " + Impact_Sorted[0] + " (" + Name_2 + ")")
        print("")
        if Impact_Sorted[-1] in Team_1:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_1 + ")")
        else:
            print("Flog of the Series - " + Impact_Sorted[-1] + " (" + Name_2 + ")")
        print("")
        seriesOutput(Score, Series_Name)
        print(" ")
 #       BattingScores = mergeDict_i(BattingScores, BSco, Number)
        BattingSheet = mergeDict(BattingSheet, BShe)
        BowlingStats = mergeDict(BowlingStats, BF)
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        SixArray = [Batting[Batters[i]].sixes for i in range(len(Batters))]
        FourArray = [Batting[Batters[i]].fours for i in range(len(Batters))]

        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))
        Four = dict(zip(Batters, FourArray))
        Six = dict(zip(Batters, SixArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
#        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]

        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets >= 0.25 * Number:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print(" ")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Most 50s - ")
        numFifties(BattingScores, cut=None)
        print(" ")
        print("Most 100s - ")
        numHundreds(BattingScores, cut=None)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighest(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print("Most Sixes - ")
        showStats(Six, cut = 10)
        print(" ")
        print("Most Fours - ")
        showStats(Four, cut = 10)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Most Fifers - ")
        numFifers(Figures_Bowl, cut = None)
        print(" ")
        print("Most Threefers - ")
        numThreefers(Figures_Bowl, cut=None)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFigures(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

#Series()

def Tournament():
    N_Teams = input("Teams playing the Tournament : ").upper().replace(" ", "").split(",")
    if len(N_Teams) == 1:
        if N_Teams == ["T20"]:
            N_Teams = "engt20,engwt20,aust20,auswt20,indt20,indwt20,saatt20,nzt20,nzwt20".upper().replace(" ", "").split(",")
        if N_Teams == ["ODI"]:
            N_Teams = "engodi,engwodi,ausodi,auswodi,indodi,indwodi,saatodi,nzodi,nzwodi".upper().replace(" ", "").split(",")
        if N_Teams == ["TEST"]:
            N_Teams = "engtest,engwtest,austest,auswtest,indtest,indwtest,satest,nztest,nzwtest".upper().replace(" ", "").split(",")
        if N_Teams == ["WT20"]:
            N_Teams = "engwt20,auswt20,indwt20,nzwt20".upper().replace(" ", "").split(",")
        if N_Teams == ["WODI"]:
            N_Teams = "engwodi,auswodi,indwodi,nzwodi".upper().replace(" ", "").split(",")
        if N_Teams == ["WTEST"]:
            N_Teams = "engwtest,auswtest,indwtest,nzwtest".upper().replace(" ", "").split(",")
        if N_Teams == ["AT"]:
            N_Teams = "engattest,engwtest,ausattest,auswtest,indattest,indwtest,saattest,wiattest,nztest,nzwtest".upper().replace(" ", "").split(",")
        if N_Teams == ["IPL"]:
            N_Teams = "RCB, MI, CSK, SRH, KKR, GT, LSG, PK, RR, DC".upper().replace(" ", "").split(",")
        if N_Teams == ["WPL"]:
            N_Teams = "RCBW, MIW, DCW, GGW, UPWW".upper().replace(" ", "").split(",")
        if N_Teams == ["ASHESATTEST"]:
            N_Teams = "engattest, ausattest, engwtest,auswtest".upper().replace(" ", "").split(",")
        if N_Teams == ["ASHESTEST"]:
            N_Teams = "engtest, austest, engwtest,auswtest".upper().replace(" ", "").split(",")
        if N_Teams == ["ASHEST20"]:
            N_Teams = "engt20, aust20, engwt20,auswt20".upper().replace(" ", "").split(",")
        if N_Teams == ["ASHESODI"]:
            N_Teams = "engodi, ausodi, engwodi,auswodi".upper().replace(" ", "").split(",")
    if N_Teams[0] == "T20":
        N_Teams_1 = "engt20,engwt20,aust20,auswt20,indt20,indwt20,saatt20,nzt20,nzwt20".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ODI":
        N_Teams_1 = "engodi,engwodi,ausodi,auswodi,indodi,indwodi,saatodi,nzodi,nzwodi".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "TEST":
        N_Teams_1 = "engtest,engwtest,austest,auswtest,indtest,indwtest,satest,nztest,nzwtest".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "WT20":
        N_Teams_1 = "engwt20,auswt20,indwt20,nzwt20".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "WODI":
        N_Teams_1 = "engwodi,auswodi,indwodi,nzwodi".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "WTEST":
        N_Teams_1 = "engwtest,auswtest,indwtest,nzwtest".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "AT":
        N_Teams_1 = "engattest,engwtest,ausattest,auswtest,indattest,indwtest,saattest,wiattest,nztest,nzwtest".upper().replace( " ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ATMEN":
        N_Teams_1 = "engattest,ausattest,indattest,saattest,wiattest,nztest".upper().replace( " ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "IPL":
        N_Teams_1 = "RCB, MI, CSK, SRH, KKR, GT, LSG, PK, RR, DC".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "WPL":
        N_Teams_1 = "RCBW, MIW, DCW, GGW, UPWW".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ASHESATTEST":
        N_Teams_1 = "engattest, ausattest, engwtest,auswtest".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ASHESTEST":
        N_Teams_1 = "engtest, austest, engwtest,auswtest".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ASHEST20":
        N_Teams_1 = "engt20, aust20, engwt20,auswt20".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    if N_Teams[0] == "ASHESODI":
        N_Teams_1 = "engodi, ausodi, engwodi,auswodi".upper().replace(" ", "").split(",")
        for i in range(1, len(N_Teams)):
            N_Teams_1.append(N_Teams[i])
        N_Teams = N_Teams_1
    Tour_Name = input("Tournament Name : ").upper()
    IndexArray = [t.index(N_Teams[i]) for i in range(len(N_Teams))]
    MatchOrder = Combinations(IndexArray)
    Format = input("Format : ").upper()
    P = None
    if Format == "TEST":
        Location = input("Location : ").upper()
        if Location == "ENG":
            P_death = 0.05
            P_mine = 0.20
            P_norm = 0.55
            P_high = 0.20
        elif Location == "IND":
            P_death = 0.20
            P_mine = 0.30
            P_norm = 0.30
            P_high = 0.20
        elif Location == "DEADLY IND":
            P_death = 0.25
            P_mine = 0.55
            P_norm = 0.20
            P_high = 0.00
        elif Location == "AUS":
            P_death = 0.10
            P_mine = 0.15
            P_norm = 0.25
            P_high = 0.50
        elif Location == "SA":
            P_death = 0.20
            P_mine = 0.30
            P_norm = 0.15
            P_high = 0.35
        elif Location == "WI":
            P_death = 0.14
            P_mine = 0.16
            P_norm = 0.30
            P_high = 0.40
        elif Location == "NZ":
            P_death = 0.08
            P_mine = 0.08
            P_norm = 0.24
            P_high = 0.60
        elif Location == "DAHLIA":
            P_death = 0.5
            P_mine = 0
            P_norm = 0
            P_high = 0.5
        elif Location == "MOON":
            P_death = 1
            P_mine = 0
            P_norm = 0
            P_high = 0
        elif Location == "HIGHWAY":
            P_death = 0
            P_mine = 0
            P_norm = 0
            P_high = 1
    PointsTable = pd.DataFrame({"Teams" : N_Teams, "Matches" : np.zeros(len(N_Teams)), "Won" : np.zeros(len(N_Teams)), "Lost" : np.zeros(len(N_Teams)), "Draw" : np.zeros(len(N_Teams)), "Points" : np.zeros(len(N_Teams)), "NRR" : np.zeros(len(N_Teams)), "Runs Scored" : np.zeros(len(N_Teams)), "Runs Conceded" : np.zeros(len(N_Teams)), "Balls Bowled" : np.zeros(len(N_Teams)), "Balls Played" : np.zeros(len(N_Teams)), "Wickets Taken" : np.zeros(len(N_Teams)), "Wickets Lost" : np.zeros(len(N_Teams))})
    PointsTable['Matches'] = PointsTable['Matches'].astype(int)
    PointsTable['Won'] = PointsTable['Won'].astype(int)
    PointsTable['Lost'] = PointsTable['Lost'].astype(int)
    PointsTable['Draw'] = PointsTable['Draw'].astype(int)
    PointsTable['Points'] = PointsTable['Points'].astype(int)
    PointsTable['Wickets Taken'] = PointsTable['Wickets Taken'].astype(int)
    PointsTable['Wickets Lost'] = PointsTable['Wickets Lost'].astype(int)
    BattingSheet = {}
    BattingScores = {}
    BowlingStats = {}
    Figures_Bowl = {}
    print("")
    print("Fixture - ")
    for i in range(len(MatchOrder)):
        A = MatchOrder[i]
        print("Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - " + t[A[0]] + " vs " + t[A[1]])
    print("")
    print("Points Table")
    print(PointsTable.loc[:, "Teams":"NRR"])
    print("")
    if Format.upper() != "TEST":
        Impact_Points = {}
        for i in range(len(MatchOrder)):
            A = MatchOrder[i]
            print("Next Match" + " - " + "Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - "+ t[A[0]] + " vs " + t[A[1]])
            print("")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, NRR_Dict = MatchLimitedOne(t[A[0]], Teams[A[0]].split(","), TeamBowl[A[0]], TeamType[A[0]], t[A[1]], Teams[A[1]].split(","), TeamBowl[A[1]], TeamType[A[1]], Format)
            i1 = np.where(PointsTable["Teams"] == t[A[0]])[0][0]
            i2 = np.where(PointsTable["Teams"] == t[A[1]])[0][0]
            PointsTable.loc[i1, "Runs Scored"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i1, "Runs Conceded"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i1, "Balls Bowled"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i1, "Balls Played"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i1, "NRR"] = 6 * (PointsTable.loc[i1, "Runs Scored"]/PointsTable.loc[i1, "Balls Played"] - PointsTable.loc[i1, "Runs Conceded"]/PointsTable.loc[i1, "Balls Bowled"])
            PointsTable.loc[i1, "Matches"] += 1
            PointsTable.loc[i2, "Runs Scored"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i2, "Runs Conceded"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i2, "Balls Bowled"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i2, "Balls Played"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i2, "NRR"] = 6 * (PointsTable.loc[i2, "Runs Scored"] / PointsTable.loc[i2, "Balls Played"] - PointsTable.loc[i2, "Runs Conceded"] / PointsTable.loc[i2, "Balls Bowled"])
            PointsTable.loc[i2, "Matches"] += 1
            if W == None:
                PointsTable.loc[i1, "Draw"] += 1
                PointsTable.loc[i2, "Draw"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            if W == t[A[0]]:
                PointsTable.loc[i1, "Won"] += 1
                PointsTable.loc[i2, "Lost"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
            if W == t[A[1]]:
                PointsTable.loc[i1, "Lost"] += 1
                PointsTable.loc[i2, "Won"] += 1
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam] = K
            for x in BSco_1.keys():
                A = BSco_1[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in BSco_2.keys():
                A = BSco_2[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_2[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            PointsTable = PointsTable.sort_values(by=['Points', 'NRR'], ascending=[False, False]).reset_index().iloc[:, 1:]
            print("Points Table")
            print(PointsTable.loc[:, "Teams":"NRR"])
            print("")
        if len(N_Teams) < 5:
            FinalNames = list(PointsTable.loc[[0, 1], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam] = K
            for x in BSco_1.keys():
                A = BSco_1[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in BSco_2.keys():
                A = BSco_2[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_2[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the " + Tour_Name + "!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the " + Tour_Name)
            print("")
        else:
            FinalNames = list(PointsTable.loc[[0, 1, 2, 3], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("SEMI FINAL 1 - " + FinalNames[0] + " vs " + FinalNames[3])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[3]], Teams[FinalIndexArray[3]].split(","), TeamBowl[FinalIndexArray[3]], TeamType[FinalIndexArray[3]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam] = K
            for x in BSco_1.keys():
                A = BSco_1[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in BSco_2.keys():
                A = BSco_2[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 +1.5* A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W1 = None
            if W != None:
                print(W + " advances to the Finals.")
                W1 = W
            else:
                print(FinalNames[0] + " advances to the Finals.")
                W1 = FinalNames[0]
            print("")
            print(40 * "-")
            print("SEMI FINAL 2 - " + FinalNames[1] + " vs " + FinalNames[2])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], t[FinalIndexArray[2]], Teams[FinalIndexArray[2]].split(","), TeamBowl[FinalIndexArray[2]], TeamType[FinalIndexArray[2]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam] = K
            for x in BSco_1.keys():
                A = BSco_1[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in BSco_2.keys():
                A = BSco_2[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_2[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W2 = None
            if W != None:
                print(W + " advances to the Finals.")
                W2 = W
            else:
                print(FinalNames[1] + " advances to the Finals.")
                W2 = FinalNames[1]
            print("")
            FinalNames = [W1, W2]
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40 * "-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco_1, BSco_2, Balls_1, Balls_2, Bowler_1, Bowler_2, BShe, BF, _ = MatchLimitedOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], Format)
            BSco = mergeDict(BSco_1, BSco_2)
            for x in BF.keys():
                K = BF[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam] = Figure
            for x in BSco.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam] = K
            for x in BSco_1.keys():
                A = BSco_1[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_1[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_1[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in BSco_2.keys():
                A = BSco_2[x]
                try:
                    Impact_Points[x] += A ** 2 / Balls_2[x]
                    if A >= 50:
                        Impact_Points[x] += 25
                    if A >= 100:
                        Impact_Points[x] += 75
                except:
                    try:
                        Impact_Points[x] = A ** 2 / Balls_2[x]
                        if A >= 50:
                            Impact_Points[x] += 25
                        if A >= 100:
                            Impact_Points[x] += 75
                    except:
                        x = 5
            for x in Bowler_1.keys():
                A = Bowler_1[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            for x in Bowler_2.keys():
                A = Bowler_2[x]
                try:
                    if Format == "T20":
                        Impact_Points[x] += 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] += 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
                except:
                    if Format == "T20":
                        Impact_Points[x] = 160 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/24)**2 / max(1, total(A))
                    if Format == "ODI":
                        Impact_Points[x] = 80 * (1 + 1.5*A.count(5)) * (len(A) / 6) * (len(A)/60)**2 / max(1, total(A))
                    if A.count(5) >= 3:
                        Impact_Points[x] += 25
                    if A.count(5) >= 5:
                        Impact_Points[x] += 75
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the " + Tour_Name + "!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the " + Tour_Name)
            print("")
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        ConsArray = [Batting[Batters[i]].consistency for i in range(len(Batters))]
        SixArray = [Batting[Batters[i]].sixes for i in range(len(Batters))]
        FourArray = [Batting[Batters[i]].fours for i in range(len(Batters))]

        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))
        Cons = dict(zip(Batters, ConsArray))
        Six = dict(zip(Batters, SixArray))
        Four = dict(zip(Batters, FourArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
        #        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets  > len(N_Teams):
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        print("")
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        Team_0 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[0] in Teams[IndexArray[i]].split(","):
                Team_0 = t[IndexArray[i]]
        print("Player of the Tournament - " + Impact_Sorted[0] + " (" + Team_0 + ")")
        print("")

        Team_1 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[-1] in Teams[IndexArray[i]].split(","):
                Team_1 = t[IndexArray[i]]
        print("Flog of the Tournament - " + Impact_Sorted[-1] + " (" + Team_1 + ")")
        print("")
        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print(" ")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Most 50s - ")
        numFifties(BattingScores, cut = None)
        print(" ")
        print("Most 100s - ")
        numHundreds(BattingScores, cut = None)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighestTournament(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print("Most Sixes - ")
        showStats(Six, cut = 10)
        print(" ")
        print("Most Fours - ")
        showStats(Four, cut=10)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Most Fifers - ")
        numFifers(Figures_Bowl, cut = None)
        print(" ")
        print("Most Threefers - ")
        numThreefers(Figures_Bowl, cut=None)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFiguresTournament(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")
    else:
        Impact_Points = {}
        for i in range(len(MatchOrder)):
            A = MatchOrder[i]
            print("Next Match" + " - " + "Match " + str(i + 1) + " of " + str(len(MatchOrder)) + " - "+ t[A[0]] + " vs " + t[A[1]])
            print("")
            K = input("Continue ? ")
            print(" ")
            for i in range(len(Teams[A[0]].split(","))):
                try:
                    x = Impact_Points[Teams[A[0]].split(",")[i]]
                except:
                    Impact_Points[Teams[A[0]].split(",")[i]] = 0
            for i in range(len(Teams[A[1]].split(","))):
                try:
                    x = Impact_Points[Teams[A[1]].split(",")[i]]
                except:
                    Impact_Points[Teams[A[1]].split(",")[i]] = 0
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, NRR_Dict = MatchTestOne(t[A[0]], Teams[A[0]].split(","), TeamBowl[A[0]], TeamType[A[0]], t[A[1]], Teams[A[1]].split(","), TeamBowl[A[1]], TeamType[A[1]], P_death, P_mine, P_norm, P_high)
            i1 = np.where(PointsTable["Teams"] == t[A[0]])[0][0]
            i2 = np.where(PointsTable["Teams"] == t[A[1]])[0][0]
            PointsTable.loc[i1, "Runs Scored"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i1, "Runs Conceded"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i1, "Wickets Taken"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i1, "Wickets Lost"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i1, "NRR"] = 6 * (PointsTable.loc[i1, "Runs Scored"]/PointsTable.loc[i1, "Wickets Lost"] - PointsTable.loc[i1, "Runs Conceded"]/PointsTable.loc[i1, "Wickets Taken"])
            PointsTable.loc[i1, "Matches"] += 1
            PointsTable.loc[i2, "Runs Scored"] += NRR_Dict[t[A[1]]][0]
            PointsTable.loc[i2, "Runs Conceded"] += NRR_Dict[t[A[0]]][0]
            PointsTable.loc[i2, "Wickets Taken"] += NRR_Dict[t[A[0]]][1]
            PointsTable.loc[i2, "Wickets Lost"] += NRR_Dict[t[A[1]]][1]
            PointsTable.loc[i2, "NRR"] = 6 * (PointsTable.loc[i2, "Runs Scored"] / PointsTable.loc[i2, "Wickets Lost"] - PointsTable.loc[i2, "Runs Conceded"] / PointsTable.loc[i2, "Wickets Taken"])
            PointsTable.loc[i2, "Matches"] += 1

            if W == None:
                PointsTable.loc[i1, "Draw"] += 1
                PointsTable.loc[i2, "Draw"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
            if W == t[A[0]]:
                PointsTable.loc[i1, "Won"] += 1
                PointsTable.loc[i2, "Lost"] += 1
                PointsTable.loc[i1, "Points"] = 2 * PointsTable.loc[i1, "Won"] + PointsTable.loc[i1, "Draw"]
            if W == t[A[1]]:
                PointsTable.loc[i1, "Lost"] += 1
                PointsTable.loc[i2, "Won"] += 1
                PointsTable.loc[i2, "Points"] = 2 * PointsTable.loc[i2, "Won"] + PointsTable.loc[i2, "Draw"]
 #           BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5*K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                Figures_Bowl[x + "_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco1[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco2[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco3[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[A[0]]:
                    HomeTeam = t[A[0]]
                    OppTeam = t[A[1]]
                else:
                    HomeTeam = t[A[1]]
                    OppTeam = t[A[0]]
                K = BSco4[x]
                BattingScores[x + "_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            PointsTable = PointsTable.sort_values(by=['Points', 'NRR'], ascending=[False, False]).reset_index().iloc[:, 1:]
            print("Points Table")
            print(PointsTable.loc[:, "Teams":"NRR"])
            print("")
        if len(N_Teams) < 5:
            FinalNames = list(PointsTable.loc[[0, 1], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], P_death, P_mine, P_norm, P_high)
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Finals_"+ HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)

            if W != None:
                print(W + " wins the " + Tour_Name + "!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the " + Tour_Name)
            print("")
        else:
            FinalNames = list(PointsTable.loc[[0, 1, 2, 3], "Teams"])
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40*"-")
            print("SEMI FINAL 1 - " + FinalNames[0] + " vs " + FinalNames[3])
            print(40*"-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[3]], Teams[FinalIndexArray[3]].split(","), TeamBowl[FinalIndexArray[3]], TeamType[FinalIndexArray[3]], P_death, P_mine, P_norm, P_high)
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[3]]
                else:
                    HomeTeam = t[FinalIndexArray[3]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Semi Final 1_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W1 = None
            if W != None:
                print(W + " advances to the Finals.")
                W1 = W
            else:
                print(FinalNames[0] + " advances to the Finals.")
                W1 = FinalNames[0]
            print("")
            print(40 * "-")
            print("SEMI FINAL 2 - " + FinalNames[1] + " vs " + FinalNames[2])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], t[FinalIndexArray[2]], Teams[FinalIndexArray[2]].split(","), TeamBowl[FinalIndexArray[2]], TeamType[FinalIndexArray[2]], P_death, P_mine, P_norm, P_high)
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                Figures_Bowl[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco1[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco2[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco3[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[1]]:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[2]]
                else:
                    HomeTeam = t[FinalIndexArray[2]]
                    OppTeam = t[FinalIndexArray[1]]
                K = BSco4[x]
                BattingScores[x + "_Semi Final 2_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            W2 = None
            if W != None:
                print(W + " advances to the Finals.")
                W2 = W
            else:
                print(FinalNames[1] + " advances to the Finals.")
                W2 = FinalNames[1]
            print("")
            FinalNames = [W1, W2]
            FinalIndexArray = [t.index(FinalNames[i]) for i in range(len(FinalNames))]
            print(40 * "-")
            print("FINALS - " + FinalNames[0] + " vs " + FinalNames[1])
            print(40 * "-")
            K = input("Continue ? ")
            print(" ")
            W, BSco1, BSco2, BSco3, BSco4, BShe, BF1, BF2, BF3, BF4, _ = MatchTestOne(t[FinalIndexArray[0]], Teams[FinalIndexArray[0]].split(","), TeamBowl[FinalIndexArray[0]], TeamType[FinalIndexArray[0]], t[FinalIndexArray[1]], Teams[FinalIndexArray[1]].split(","), TeamBowl[FinalIndexArray[1]], TeamType[FinalIndexArray[1]], P_death, P_mine, P_norm, P_high)
#            BSco = mergeDict(mergeDict(mergeDict(BSco1, BSco2), BSco3), BSco4)
            BF = mergeDict(mergeDict(mergeDict(BF1, BF2), BF3), BF4)
            for x in BF1.keys():
                K = BF1[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF2.keys():
                K = BF2[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF3.keys():
                K = BF3[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BF4.keys():
                K = BF4[x]
                Figure = 10000 * (K.count(5) + 1) + 1000 - (sum(K) - 5 * K.count(5))
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                Figures_Bowl[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = Figure
                Impact_Points[x] += 20 * K.count(5) - 0.1 * total(K)
                if K.count(5) >= 5:
                    Impact_Points[x] += 6 * K.count(5)
                elif K.count(5) >= 3:
                    Impact_Points[x] += 3 * K.count(5)
            for x in BSco1.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco1[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_1"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco2.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco2[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_2"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco3.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco3[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_3"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            for x in BSco4.keys():
                HomeTeam = None
                OppTeam = None
                if x in Teams[FinalIndexArray[0]]:
                    HomeTeam = t[FinalIndexArray[0]]
                    OppTeam = t[FinalIndexArray[1]]
                else:
                    HomeTeam = t[FinalIndexArray[1]]
                    OppTeam = t[FinalIndexArray[0]]
                K = BSco4[x]
                BattingScores[x + "_Finals_" + HomeTeam + "_" + OppTeam + "_4"] = K
                Impact_Points[x] += K
                if K >= 100:
                    Impact_Points[x] += 25
            BattingSheet = mergeDict(BattingSheet, BShe)
            BowlingStats = mergeDict(BowlingStats, BF)
            if W != None:
                print(W + " wins the " + Tour_Name +"!!!")
            else:
                print(FinalNames[0] + " and " + FinalNames[1] + " won the " + Tour_Name)
            print("")
        Batting = {}
        Bowling = {}
        for x in BattingSheet.keys():
            B = Batter()
            B.makeStats(BattingSheet[x])
            Batting[x] = B
        for x in BowlingStats.keys():
            B = Bowler()
            B.makeStats(BowlingStats[x])
            Bowling[x] = B
        Batters = list(Batting.keys())
        RunsArray = [Batting[Batters[i]].runs for i in range(len(Batters))]
        SRArray = [Batting[Batters[i]].strikerate for i in range(len(Batters))]
        AvgArray = [Batting[Batters[i]].average for i in range(len(Batters))]
        ConsArray = [Batting[Batters[i]].consistency for i in range(len(Batters))]
        SixArray = [Batting[Batters[i]].sixes for i in range(len(Batters))]
        FourArray = [Batting[Batters[i]].fours for i in range(len(Batters))]
        Runs = dict(zip(Batters, RunsArray))
        SR = dict(zip(Batters, SRArray))
        Avg = dict(zip(Batters, AvgArray))
        Cons = dict(zip(Batters, ConsArray))
        Six = dict(zip(Batters, SixArray))
        Four = dict(zip(Batters, FourArray))

        Bowlers = list(Bowling.keys())
        RunsBowlArray = [Bowling[Bowlers[i]].Runs for i in range(len(Bowlers))]
        EconArray = [Bowling[Bowlers[i]].Economy for i in range(len(Bowlers))]
        WicketsArray = [Bowling[Bowlers[i]].Wickets for i in range(len(Bowlers))]
        #        AvgBowlArray = [Bowling[Bowlers[i]].Average for i in range(len(Bowlers))]
        AvgBowlArray = []
        BowlAvg = []
        for i in range(len(Bowlers)):
            if Bowling[Bowlers[i]].Average != None and Bowling[Bowlers[i]].Wickets  > 2*len(N_Teams) - 2:
                BowlAvg.append(Bowlers[i])
                AvgBowlArray.append(Bowling[Bowlers[i]].Average)
        RunsBowl = dict(zip(Bowlers, RunsBowlArray))
        Econ = dict(zip(Bowlers, EconArray))
        Wickets = dict(zip(Bowlers, WicketsArray))
        AvgBowl = dict(zip(BowlAvg, AvgBowlArray))
        print("")
        Impact_Sorted_Dict = dict(sorted(Impact_Points.items(), key=lambda x: x[1], reverse=True))
        Impact_Sorted = list(Impact_Sorted_Dict.keys())
        print("")
        Team_0 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[0] in Teams[IndexArray[i]].split(","):
                Team_0 = t[IndexArray[i]]
        print("Player of the Tournament - " + Impact_Sorted[0] + " (" + Team_0 + ")")
        print("")

        Team_1 = None
        for i in range(0, len(IndexArray)):
            if Impact_Sorted[-1] in Teams[IndexArray[i]].split(","):
                Team_1 = t[IndexArray[i]]
        print("Flog of the Tournament - " + Impact_Sorted[-1] + " (" + Team_1 + ")")
        print("")

        stats = input("Show Stats ? : ").upper()
        if stats == "N":
            return
        print("")
        print("Highest Impact Points - ")
        showStats(Impact_Sorted_Dict)
        print("")
        print(40 * "*")
        print("BATTERS")
        print(40 * "*")
        print("")
        print("Most Runs - ")
        showStats(Runs)
        print(" ")
        print("Most 50s - ")
        numFifties(BattingScores, cut = None)
        print(" ")
        print("Most 100s - ")
        numHundreds(BattingScores, cut = None)
        print(" ")
        print("Highest Average - ")
        showStats(Avg)
        print(" ")
        print("Highest Scores - ")
        showHighestTournamentTest(BattingScores, cut=10)
        print(" ")
        print("Highest Strike Rates - ")
        showStats(SR)
        print(" ")
        print("Most Sixes - ")
        showStats(Six, cut = 10)
        print(" ")
        print("Most Fours - ")
        showStats(Four, cut = 10)
        print(" ")
        print(40 * "*")
        print("BOWLERS")
        print(40 * "*")
        print("")
        print("Most Wickets - ")
        showStats(Wickets)
        print(" ")
        print("Most Fifers - ")
        numFifers(Figures_Bowl, cut = None)
        print(" ")
        print("Most Threefers - ")
        numThreefers(Figures_Bowl, cut=None)
        print(" ")
        print("Best Average - ")
        showStats(AvgBowl, Reverse=False)
        print(" ")
        print("Best Figures - ")
        showFiguresTournamentTest(Figures_Bowl)
        print(" ")
        print("Best Economy - ")
        showStats(Econ, Reverse=False)
        print(" ")
        print("Most Runs Conceded - ")
        showStats(RunsBowl)
        print(" ")

def cricket():
    ST = input("Series/Tournament : ").upper()
    while ST not in ["S", "T"]:
        ST = input("Series/Tournament : ").upper()
    if ST == "S":
        Series()
    if ST == "T":
        Tournament()

cricket()
