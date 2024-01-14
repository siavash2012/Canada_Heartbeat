import psycopg2
import pandas as pd


# establishing the connection. before running the file, open psql shell and configure the below parameters.
conn = psycopg2.connect(
    database="postgres", user='postgres', password='', host='127.0.0.1', port='5432'
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()



def create_salt():
    df_salt = pd.read_csv('C:/users/conta/desktop/physical_design/salt.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS SALT(
       SEQNO INT PRIMARY KEY,
       SALTCOOK INT NOT NULL,
       SALTFOOD int NOT NULL,
       SALTBP INT NOT NULL,
       SALTHA INT NOT NULL,
       SALTSTR INT NOT NULL
    );'''

    cursor.execute(sql)
    for row in df_salt.itertuples(index=False):

        query =\
            "INSERT INTO salt(SEQNO,SALTCOOK,SALTFOOD,SALTBP,SALTHA,SALTSTR) VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s" %\
            ('(',row.SEQNO,',',row.SALTCOOK,',',row.SALTFOOD,',',row.SALTBP,',',row.SALTHA,',', row.SALTSTR,')')
        cursor.execute(query)


def create_demographics():
    df_demographics = pd.read_csv('C:/users/conta/desktop/physical_design/demographics.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS DEMOGRAPHICS(
           SEQNO INT PRIMARY KEY,
           PROV INT NOT NULL,
           SEX int NOT NULL,
           AGE INT NOT NULL,
           EDUC INT NOT NULL,
           INCOME INT NOT NULL,
           INCADEQ INT NOT NULL,
           EMPLOY INT NOT NULL,
           WORKTYPE INT NOT NULL,
           MARITAL INT NOT NULL,
           HOUSEHLD INT NOT NULL,
           LANG INT NOT NULL
        );'''
    cursor.execute(sql)
    for row in df_demographics.itertuples(index=False):
        query = \
            "INSERT INTO DEMOGRAPHICS(SEQNO,PROV,SEX,AGE,EDUC,INCOME,INCADEQ,EMPLOY,WORKTYPE,MARITAL,HOUSEHLD,LANG)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            ('(', row.SEQNO, ',', row.PROV, ',', row.SEX, ',', row.AGE, ',',row.EDUC,',', row.INCOME, ',', row.INCADEQ,
             ',',row.EMPLOY,',',row.WORKTYPE,',',row.MARITAL,',',row.HOUSEHLD,',',row.LANG,
             ')')
        cursor.execute(query)


#"SEQNO", "ALCOHOL", "ALC12MTH", "ALCMTH", "ALCNUM"
def create_alcohol():
    df_alcohol = pd.read_csv('C:/users/conta/desktop/physical_design/alcohol.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS ALCOHOL(
           SEQNO INT PRIMARY KEY,
           ALCOHOL INT NOT NULL,
           ALC12MTH int NOT NULL,
           ALCMTH INT NOT NULL,
           ALCNUM INT NOT NULL
        );'''
    cursor.execute(sql)
    for row in df_alcohol.itertuples(index=False):
        query = \
            "INSERT INTO ALCOHOL(SEQNO,ALCOHOL,ALC12MTH,ALCMTH,ALCNUM)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s" % \
            (
            '(', row.SEQNO, ',', row.ALCOHOL, ',', row.ALC12MTH, ',', row.ALCMTH, ',', row.ALCNUM,
            ')')
        cursor.execute(query)


#"SEQNO", "REGSMOK", "SMOKECAT", "CIGCAT", "CIG_DAY", "PIPE", "CIGAR"
def create_tobacco():
    df_tobacco = pd.read_csv('C:/users/conta/desktop/physical_design/tobacco.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS TOBACCO(
              SEQNO INT PRIMARY KEY,
              REGSMOK INT NOT NULL,
              SMOKECAT int NOT NULL,
              CIGCAT INT NOT NULL,
              CIG_DAY INT NOT NULL,
              PIPE INT NOT NULL,
              CIGAR INT NOT NULL
           );'''
    cursor.execute(sql)
    for row in df_tobacco.itertuples(index=False):
        query = \
            "INSERT INTO TOBACCO(SEQNO,REGSMOK,SMOKECAT,CIGCAT,CIG_DAY,PIPE,CIGAR)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.REGSMOK, ',', row.SMOKECAT, ',', row.CIGCAT, ',', row.CIG_DAY,
                ',',row.PIPE,',',row.CIGAR,
                ')')
        cursor.execute(query)


#"SEQNO", "EVERHA", "EVERSTR", "OTHHD", "RXHEART", "FEMRX"
def create_past_medical_history():
    df_past_medical_history = pd.read_csv('C:/users/conta/desktop/physical_design/past_medical_history.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS PAST_MEDICAL_HISTORY(
                 SEQNO INT PRIMARY KEY,
                 EVERHA INT NOT NULL,
                 EVERSTR int NOT NULL,
                 OTHHD INT NOT NULL,
                 RXHEART INT NOT NULL,
                 FEMRX INT NOT NULL
              );'''
    cursor.execute(sql)
    for row in df_past_medical_history.itertuples(index=False):
        query = \
            "INSERT INTO PAST_MEDICAL_HISTORY(SEQNO,EVERHA,EVERSTR,OTHHD,RXHEART,FEMRX)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.EVERHA, ',', row.EVERSTR, ',', row.OTHHD, ',', row.RXHEART,
                ',', row.FEMRX,
                ')')
        cursor.execute(query)


#"SEQNO", "SYSCAT", "DIASCAT", "HYPER", "HATCS", "PHARM", "BPSALT2", "BPWGT2", "BPSTR2", "BPSMOK2","BPALC2", "BPEXER2",
# "BPSALT", "BPFATS", "BPCALOR", "BPALC", "BPCAFF", "BPHEALTH"
def create_blood_pressure():
    df_blood_pressure = pd.read_csv('C:/users/conta/desktop/physical_design/blood_pressure.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS BLOOD_PRESSURE(
                 SEQNO INT PRIMARY KEY,
                 SYSCAT INT NOT NULL,
                 DIASCAT int NOT NULL,
                 HYPER INT NOT NULL,
                 HATCS INT NOT NULL,
                 PHARM INT NOT NULL,
                 BPSALT2 INT NOT NULL,
                 BPWGT2 INT NOT NULL,
                 BPSTR2 INT NOT NULL,
                 BPSMOK2 INT NOT NULL,
                 BPALC2 INT NOT NULL,
                 BPEXER2 INT NOT NULL,
                 BPSALT INT NOT NULL,
                 BPFATS INT NOT NULL,
                 BPCALOR INT NOT NULL,
                 BPALC INT NOT NULL,
                 BPCAFF INT NOT NULL,
                 BPHEALTH INT NOT NULL
              );'''
    cursor.execute(sql)
    for row in df_blood_pressure.itertuples(index=False):
        query = \
            "INSERT INTO BLOOD_PRESSURE(SEQNO,SYSCAT,DIASCAT,HYPER,HATCS,PHARM,BPSALT2,BPWGT2,BPSTR2,BPSMOK2," \
            "BPALC2,BPEXER2,BPSALT,BPFATS,BPCALOR,BPALC,BPCAFF,BPHEALTH)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.SYSCAT, ',', row.DIASCAT, ',', row.HYPER, ',', row.HATCS,
                ',', row.PHARM, ',', row.BPSALT2,',',row.BPWGT2,',',row.BPSTR2,',',row.BPSMOK2,',',row.BPALC2,
                ',',row.BPEXER2,',',row.BPSALT,',',row.BPFATS,',',row.BPCALOR,',',row.BPALC,',',row.BPCAFF,',',row.BPHEALTH,
                ')')
        cursor.execute(query)


#"SEQNO", "HGTC", "WGTC", "BMI", "BMICAT", "WAIST", "HIP", "WHR", "WHRCAT", "PULSE"
def create_physical_measurements():
    df_physical_measurements = pd.read_csv('C:/users/conta/desktop/physical_design/physical_measurements.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS PHYSICAL_MEASUREMENTS(
                  SEQNO INT PRIMARY KEY,
                  HGTC INT NOT NULL,
                  WGTC int NOT NULL,
                  BMI INT NOT NULL,
                  BMICAT INT NOT NULL,
                  WAIST INT NOT NULL,
                  HIP INT NOT NULL,
                  WHR INT NOT NULL,
                  WHRCAT INT NOT NULL,
                  PULSE INT NOT NULL
               );'''
    cursor.execute(sql)
    for row in df_physical_measurements.itertuples(index=False):
        query = \
            "INSERT INTO PHYSICAL_MEASUREMENTS(SEQNO,HGTC,WGTC,BMI,BMICAT,WAIST,HIP,WHR,WHRCAT,PULSE)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.HGTC, ',', row.WGTC, ',', row.BMI, ',', row.BMICAT,
                ',', row.WAIST, ',', row.HIP,',',row.WHR,',',row.WHRCAT,',',row.PULSE,
                ')')
        cursor.execute(query)


#"SEQNO", "DIABET", "DIABAGE", "DBNOTRT", "DBINS", "DBRX", "DBDIET", "DBWGT", "DBDK"
def create_diabetes():
    df_diabetes = pd.read_csv('C:/users/conta/desktop/physical_design/diabetes.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS DIABETES(
                      SEQNO INT PRIMARY KEY,
                      DIABET INT NOT NULL,
                      DIABAGE int NOT NULL,
                      DBNOTRT INT NOT NULL,
                      DBINS INT NOT NULL,
                      DBRX INT NOT NULL,
                      DBDIET INT NOT NULL,
                      DBWGT INT NOT NULL,
                      DBDK INT NOT NULL
                   );'''
    cursor.execute(sql)
    for row in df_diabetes.itertuples(index=False):
        query = \
            "INSERT INTO DIABETES(SEQNO,DIABET,DIABAGE,DBNOTRT,DBINS,DBRX,DBDIET,DBWGT,DBDK)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.DIABET, ',', row.DIABAGE, ',', row.DBNOTRT, ',', row.DBINS,
                ',', row.DBRX, ',', row.DBDIET, ',', row.DBWGT, ',', row.DBDK,
                ')')
        cursor.execute(query)


#"SEQNO", "TCHOL", "TCHOLCAT", "HDL", "LDL", "TRIG", "BCHRX", "BCHFAT", "BCHWGT", "CHOLBP", "CHOLHA"
def create_lipids_profile():
    df_lipids_profile = pd.read_csv('C:/users/conta/desktop/physical_design/lipids_profile.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS LIPIDS_PROFILE(
                      SEQNO INT PRIMARY KEY,
                      TCHOL FLOAT4 NOT NULL,
                      TCHOLCAT INT NOT NULL,
                      HDL FLOAT4 NOT NULL,
                      LDL FLOAT4 NOT NULL,
                      TRIG FLOAT4 NOT NULL,
                      BCHRX INT NOT NULL,
                      BCHFAT INT NOT NULL,
                      BCHWGT INT NOT NULL,
                      CHOLBP INT NOT NULL,
                      CHOLHA INT NOT NULL
                   );'''
    cursor.execute(sql)
    for row in df_lipids_profile.itertuples(index=False):
        query = \
            "INSERT INTO LIPIDS_PROFILE(SEQNO,TCHOL,TCHOLCAT,HDL,LDL,TRIG,BCHRX,BCHFAT,BCHWGT,CHOLBP,CHOLHA)" \
            " VALUES %s%d%s%f%s%d%s%f%s%f%s%f%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.TCHOL, ',', row.TCHOLCAT, ',', row.HDL, ',', row.LDL,
                ',', row.TRIG, ',', row.BCHRX, ',', row.BCHFAT, ',', row.BCHWGT, ',', row.CHOLBP,',',row.CHOLHA,
                ')')
        cursor.execute(query)


#"SEQNO", "SEDENT", "EXER", "EXERSTRN", "EXERLONG", "EXERWORK"
def create_physical_activity_level():
    df_physical_activity_level = pd.read_csv('C:/users/conta/desktop/physical_design/physical_activity_level.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS PHYSICAL_ACTIVITY_LEVEL(
                     SEQNO INT PRIMARY KEY,
                     SEDENT INT NOT NULL,
                     EXER int NOT NULL,
                     EXERSTRN INT NOT NULL,
                     EXERLONG INT NOT NULL,
                     EXERWORK INT NOT NULL
                  );'''
    cursor.execute(sql)
    for row in df_physical_activity_level.itertuples(index=False):
        query = \
            "INSERT INTO PHYSICAL_ACTIVITY_LEVEL(SEQNO,SEDENT,EXER,EXERSTRN,EXERLONG,EXERWORK)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.SEDENT, ',', row.EXER, ',', row.EXERSTRN, ',', row.EXERLONG,
                ',', row.EXERWORK,
                ')')
        cursor.execute(query)


#"SEQNO", "HDPREV", "HDDIET", "HDWGT", "HDFATS", "HDSALT", "HDCHOLBD", "HDCHOLFD",
# "HDSTRESS", "HDTIRED", "HDEXER", "HDSMOKE", "HDHERED", "HDHBP", "HDART", "HDDK"
def create_cardiac_risk_factors_awareness():
    df_cardiac_risk_factors_awareness = pd.read_csv('C:/users/conta/desktop/physical_design/cardiac_risk_factors_awareness.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS CARDIAC_RISK_FACTORS_AWARENESS(
                    SEQNO INT PRIMARY KEY,
                    HDPREV INT NOT NULL,
                    HDDIET INT NOT NULL,
                    HDWGT INT NOT NULL,
                    HDFATS INT NOT NULL,
                    HDSALT INT NOT NULL,
                    HDCHOLBD INT NOT NULL,
                    HDCHOLFD INT NOT NULL,
                    HDSTRESS INT NOT NULL,
                    HDTIRED INT NOT NULL,
                    HDEXER INT NOT NULL,
                    HDSMOKE INT NOT NULL,
                    HDHERED INT NOT NULL,
                    HDHBP INT NOT NULL,
                    HDART INT NOT NULL,
                    HDDK INT NOT NULL
                 );'''
    cursor.execute(sql)
    for row in df_cardiac_risk_factors_awareness.itertuples(index=False):
        query = \
            "INSERT INTO CARDIAC_RISK_FACTORS_AWARENESS(SEQNO,HDPREV,HDDIET,HDWGT,HDFATS,HDSALT,HDCHOLBD,HDCHOLFD,HDSTRESS,HDTIRED," \
            "HDEXER,HDSMOKE,HDHERED,HDHBP,HDART,HDDK)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s" % \
            (
                '(', row.SEQNO, ',', row.HDPREV, ',', row.HDDIET, ',', row.HDWGT, ',', row.HDFATS,
                ',', row.HDSALT, ',', row.HDCHOLBD, ',', row.HDCHOLFD, ',', row.HDSTRESS, ',', row.HDTIRED, ',', row.HDEXER,
                ',', row.HDSMOKE, ',', row.HDHERED, ',', row.HDHBP, ',', row.HDART, ',', row.HDDK,
                ')')
        cursor.execute(query)



def create_cardiac_fact():
    df_cardiac_fact = pd.read_csv('C:/users/conta/desktop/physical_design/cardiac_fact.csv', sep='\t')
    sql = '''CREATE TABLE IF NOT EXISTS CARDIAC_FACT(
                          SEQNO INT PRIMARY KEY,
                          DEMOGRAPHICS_KEY INT NOT NULL REFERENCES DEMOGRAPHICS(SEQNO),
                          PHYSICAL_MEASUREMENTS_KEY INT NOT NULL REFERENCES PHYSICAL_MEASUREMENTS(SEQNO),
                          BLOOD_PRESSURE_KEY INT NOT NULL REFERENCES BLOOD_PRESSURE(SEQNO),
                          LIPIDS_PROFILE_KEY INT NOT NULL REFERENCES LIPIDS_PROFILE(SEQNO),
                          DIABETES_KEY INT NOT NULL REFERENCES DIABETES(SEQNO),
                          ALCOHOL_KEY INT NOT NULL REFERENCES ALCOHOL(SEQNO),
                          TOBACCO_KEY INT NOT NULL REFERENCES TOBACCO(SEQNO),
                          SALT_KEY INT NOT NULL REFERENCES SALT(SEQNO),
                          PHYSICAL_ACTIVITY_LEVEL_KEY INT NOT NULL REFERENCES PHYSICAL_ACTIVITY_LEVEL(SEQNO),
                          PAST_MEDICAL_HISTORY_KEY INT NOT NULL REFERENCES PAST_MEDICAL_HISTORY(SEQNO),
                          CARDIAC_RISK_FACTORS_AWARENESS_KEY INT NOT NULL REFERENCES CARDIAC_RISK_FACTORS_AWARENESS(SEQNO),
                          FRAMINGHAM_SCORE INT NOT NULL,
                          ASCVD_SCORE FLOAT4 NOT NULL
                       );'''
    cursor.execute(sql)
    for row in df_cardiac_fact.itertuples(index=False):
        query = \
            "INSERT INTO CARDIAC_FACT(SEQNO,DEMOGRAPHICS_KEY,PHYSICAL_MEASUREMENTS_KEY,BLOOD_PRESSURE_KEY," \
            "LIPIDS_PROFILE_KEY,DIABETES_KEY,ALCOHOL_KEY,TOBACCO_KEY,SALT_KEY,PHYSICAL_ACTIVITY_LEVEL_KEY," \
            "PAST_MEDICAL_HISTORY_KEY,CARDIAC_RISK_FACTORS_AWARENESS_KEY,FRAMINGHAM_SCORE,ASCVD_SCORE)" \
            " VALUES %s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%d%s%f%s" % \
            (
                '(', row.SEQNO, ',', row.demographics_key, ',', row.physical_measurements_key, ','
                ,row.blood_pressure_key, ',', row.lipids_profile_key,
                ',', row.diabetes_key, ',', row.alcohol_key, ',', row.tobacco_key, ',', row.salt_key, ','
                ,row.physical_activity_key, ',', row.past_medical_history_key,',',row.cardiac_risk_factor_awareness_key
                ,',',row.framingham_score,',',row.ascvd_score,
                ')')
        cursor.execute(query)


#create_salt()
#create_demographics()
#create_alcohol()
#create_tobacco()
#create_past_medical_history()
#create_blood_pressure()
#create_physical_measurements()
#create_diabetes()
#create_lipids_profile()
#create_physical_activity_level()
#create_cardiac_risk_factors_awareness()
#create_cardiac_fact()












# Closing the connection
conn.close()
