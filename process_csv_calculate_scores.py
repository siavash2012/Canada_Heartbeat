import pandas as pd
from calculator import Calculator



def split_csv():
    df = pd.read_csv('C:/users/conta/desktop/physical_design/CHH_ProvincialHeartHealthData.tab', encoding='ascii',
                     sep='\t')

    path = open('C:/users/conta/desktop/physical_design/demographics.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "PROV", "SEX", "AGE", "EDUC", "INCOME", "INCADEQ", "EMPLOY", "WORKTYPE", "MARITAL",
                 "HOUSEHLD", "LANG"], sep='\t', index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/demographics.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/alcohol.csv', 'w')
    df.to_csv(columns=["SEQNO", "ALCOHOL", "ALC12MTH", "ALCMTH", "ALCNUM"], sep='\t', index=False,
              path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/alcohol.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/tobacco.csv', 'w')
    df.to_csv(columns=["SEQNO", "REGSMOK", "SMOKECAT", "CIGCAT", "CIG_DAY", "PIPE", "CIGAR"], sep='\t',
              index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/tobacco.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/past_medical_history.csv', 'w')
    df.to_csv(columns=["SEQNO", "EVERHA", "EVERSTR", "OTHHD", "RXHEART", "FEMRX"], sep='\t',
              index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/past_medical_history.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/blood_pressure.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "SYSCAT", "DIASCAT", "HYPER", "HATCS", "PHARM", "BPSALT2", "BPWGT2", "BPSTR2", "BPSMOK2",
                 "BPALC2", "BPEXER2", "BPSALT", "BPFATS", "BPCALOR", "BPALC", "BPCAFF", "BPHEALTH"], sep='\t',
        index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/blood_pressure.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/physical_measurements.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "HGTC", "WGTC", "BMI", "BMICAT", "WAIST", "HIP", "WHR", "WHRCAT", "PULSE"], sep='\t',
        index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/physical_measurements.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/diabetes.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "DIABET", "DIABAGE", "DBNOTRT", "DBINS", "DBRX", "DBDIET", "DBWGT", "DBDK"], sep='\t',
        index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/diabetes.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/lipids_profile.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "TCHOL", "TCHOLCAT", "HDL", "LDL", "TRIG", "BCHRX", "BCHFAT", "BCHWGT", "CHOLBP", "CHOLHA",
                 "CHOLSTR"], sep='\t', index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/lipids_profile.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/salt.csv', 'w')
    df.to_csv(columns=["SEQNO", "SALTCOOK", "SALTFOOD", "SALTBP", "SALTHA", "SALTSTR"], sep='\t',
              index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/salt.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/physical_activity_level.csv', 'w')
    df.to_csv(columns=["SEQNO", "SEDENT", "EXER", "EXERSTRN", "EXERLONG", "EXERWORK"],
              sep='\t', index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/physical_activity_level.csv', sep='\t')
    print(df2.head())

    path = open('C:/users/conta/desktop/physical_design/cardiac_risk_factors_awareness.csv', 'w')
    df.to_csv(
        columns=["SEQNO", "HDPREV", "HDDIET", "HDWGT", "HDFATS", "HDSALT", "HDCHOLBD", "HDCHOLFD",
                 "HDSTRESS", "HDTIRED", "HDEXER", "HDSMOKE", "HDHERED", "HDHBP", "HDART", "HDDK"], sep='\t',
        index=False, path_or_buf=path)
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/cardiac_risk_factors_awareness.csv', sep='\t')
    print(df2.head())


def calcuLate_risk_create_fact():
    calculator = Calculator()
    framingham_list = []
    ascvd_list = []
    df = pd.read_csv('C:/users/conta/desktop/physical_design/CHH_ProvincialHeartHealthData.tab', encoding='ascii', sep='\t')
    for row in df.itertuples(index=False):
        framingham_list.append(calculator.framingham_10year_risk(
            row.SEX, row.AGE, row.TCHOL, row.HDL, row.MSYS, row.REGSMOK, row.PHARM))
    for row in df.itertuples(index=False):
        ascvd_list.append(calculator.compute_ascvd_score(row.SEX,row.REGSMOK,row.HYPER,row.DIABET,row.AGE,row.MSYS,row.TCHOL,row.HDL))
    cardiac_fact_df = df[['SEQNO']].copy()
    cardiac_fact_df = cardiac_fact_df.assign(demographics_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(physical_measurements_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(blood_pressure_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(lipids_profile_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(diabetes_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(alcohol_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(tobacco_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(salt_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(physical_activity_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(past_medical_history_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(cardiac_risk_factor_awareness_key=df['SEQNO'])
    cardiac_fact_df = cardiac_fact_df.assign(framingham_score=framingham_list)
    cardiac_fact_df = cardiac_fact_df.assign(ascvd_score=ascvd_list)

    path = open('C:/users/conta/desktop/physical_design/cardiac_fact.csv', 'w')
    cardiac_fact_df.to_csv(path_or_buf=path, index = False, sep = '\t')
    df2 = pd.read_csv('C:/users/conta/desktop/physical_design/cardiac_fact.csv', sep='\t')
    print(df2.head(30))






#split_csv()
calcuLate_risk_create_fact()



