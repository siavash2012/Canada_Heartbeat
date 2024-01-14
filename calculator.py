import math


class Calculator:
    #code  adopted from https://github.com/videntity/python-framingham10yr/blob/master/framingham10yr/framingham10yr.py
    def framingham_10year_risk(self, row_SEX, row_AGE, row_TCHOL, row_HDL, row_MSYS, row_REGSMOK, row_PHARM):
        if row_REGSMOK == 9 or row_TCHOL == 999.97 or row_TCHOL == 999.99 or row_HDL == 999.97 or row_HDL == 999.99 or row_MSYS == 9999.9:
            return 999
        if row_SEX == 1:
            sex = "male"
        if row_SEX == 2:
            sex = "female"
        if row_REGSMOK == 1:
            smoker = True
        if row_REGSMOK == 0:
            smoker = False
        if row_PHARM == 1:
            blood_pressure_med_treatment = True
        if row_PHARM == 0:
            blood_pressure_med_treatment = False
        points = 0
        age = row_AGE
        total_cholesterol = row_TCHOL * 38.67
        hdl_cholesterol = row_HDL * 38.67
        systolic_blood_pressure = row_MSYS

        if not 20 <= age <= 79:
            return 999

        if not 130 <= total_cholesterol <= 320:
            return 999

        if not 20 <= hdl_cholesterol <= 100:
            return 999

        if not 90 <= systolic_blood_pressure <= 200:
            return 999

        if sex.lower() == "male":

            # Age - male
            if 20 <= age <= 34:
                points -= 9
            if 35 <= age <= 39:
                points -= 4
            if 40 <= age <= 44:
                points -= 0
            if 45 <= age <= 49:
                points += 3
            if 50 <= age <= 54:
                points += 6
            if 55 <= age <= 59:
                points += 8
            if 60 <= age <= 64:
                points += 10
            if 65 <= age <= 69:
                points += 12
            if 70 <= age <= 74:
                points += 14
            if 75 <= age <= 79:
                points += 16

            # Total cholesterol, mg/dL - Male ------------------------
            if 20 <= age <= 39:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 4
                if 200 <= total_cholesterol <= 239:
                    points += 7
                if 240 <= total_cholesterol <= 279:
                    points += 9
                if total_cholesterol > 289:
                    points += 11
            if 40 <= age <= 49:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 3
                if 200 <= total_cholesterol <= 239:
                    points += 5
                if 240 <= total_cholesterol <= 279:
                    points += 6
                if total_cholesterol > 289:
                    points += 8
            if 50 <= age <= 59:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 2
                if 200 <= total_cholesterol <= 239:
                    points += 3
                if 240 <= total_cholesterol <= 279:
                    points += 4
                if total_cholesterol > 289:
                    points += 5
            if 60 <= age <= 69:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 1
                if 200 <= total_cholesterol <= 239:
                    points += 1
                if 240 <= total_cholesterol <= 279:
                    points += 2
                if total_cholesterol > 289:
                    points += 3
            if 70 <= age <= 79:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 0
                if 200 <= total_cholesterol <= 239:
                    points += 0
                if 240 <= total_cholesterol <= 279:
                    points += 1
                if total_cholesterol > 289:
                    points += 1
            # smoking - male
            if smoker:
                if 20 <= age <= 39:
                    points += 8
                if 40 <= age <= 49:
                    points += 5
                if 50 <= age <= 59:
                    points += 3
                if 60 <= age <= 69:
                    points += 1
                if 70 <= age <= 79:
                    points += 1
            else:  # nonsmoker
                points += 0

            # hdl cholesterol
            if hdl_cholesterol > 60:
                points -= 1
            if 50 <= hdl_cholesterol <= 59:
                points += 0
            if 40 <= hdl_cholesterol <= 49:
                points += 1
            if hdl_cholesterol < 40:
                points += 2

            # systolic blood pressure
            if not blood_pressure_med_treatment:
                if systolic_blood_pressure < 120:
                    points += 0
                if 120 <= systolic_blood_pressure <= 129:
                    points += 0
                if 130 <= systolic_blood_pressure <= 139:
                    points += 1
                if 140 <= systolic_blood_pressure <= 159:
                    points += 1
                if systolic_blood_pressure >= 160:
                    points += 2
            else:  # if the patient is on blood pressure meds
                if systolic_blood_pressure < 120:
                    points += 0
                if 120 <= systolic_blood_pressure <= 129:
                    points += 1
                if 130 <= systolic_blood_pressure <= 139:
                    points += 1
                if 140 <= systolic_blood_pressure <= 159:
                    points += 2
                if systolic_blood_pressure >= 160:
                    points += 3

            # calulate % risk for males
            if points <= 0:
                percent_risk = 0
            elif points == 1:
                percent_risk = 1

            elif points == 2:
                percent_risk = 1

            elif points == 3:
                percent_risk = 1

            elif points == 4:
                percent_risk = 1

            elif points == 5:
                percent_risk = 2

            elif points == 6:
                percent_risk = 2

            elif points == 7:
                percent_risk = 2

            elif points == 8:
                percent_risk = 2

            elif points == 9:
                percent_risk = 5

            elif points == 10:
                percent_risk = 6

            elif points == 11:
                percent_risk = 8

            elif points == 12:
                percent_risk = 10

            elif points == 13:
                percent_risk = 12

            elif points == 14:
                percent_risk = 16

            elif points == 15:
                percent_risk = 20

            elif points == 16:
                percent_risk = 25

            elif points >= 17:
                percent_risk = 30

        # process females ----------------------------------------------------------
        elif sex.lower() == "female":
            # Age - female
            if 20 <= age <= 34:
                points -= 7
            if 35 <= age <= 39:
                points -= 3
            if 40 <= age <= 44:
                points -= 0
            if 45 <= age <= 49:
                points += 3
            if 50 <= age <= 54:
                points += 6
            if 55 <= age <= 59:
                points += 8
            if 60 <= age <= 64:
                points += 10
            if 65 <= age <= 69:
                points += 12
            if 70 <= age <= 74:
                points += 14
            if 75 <= age <= 79:
                points += 16

            # Total cholesterol, mg/dL - Female ------------------------
            if 20 <= age <= 39:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 4
                if 200 <= total_cholesterol <= 239:
                    points += 8
                if 240 <= total_cholesterol <= 279:
                    points += 11
                if total_cholesterol > 289:
                    points += 13
            if 40 <= age <= 49:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 3
                if 200 <= total_cholesterol <= 239:
                    points += 6
                if 240 <= total_cholesterol <= 279:
                    points += 8
                if total_cholesterol > 289:
                    points += 10
            if 50 <= age <= 59:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 2
                if 200 <= total_cholesterol <= 239:
                    points += 4
                if 240 <= total_cholesterol <= 279:
                    points += 5
                if total_cholesterol > 289:
                    points += 7
            if 60 <= age <= 69:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 1
                if 200 <= total_cholesterol <= 239:
                    points += 2
                if 240 <= total_cholesterol <= 279:
                    points += 3
                if total_cholesterol > 289:
                    points += 4
            if 70 <= age <= 79:
                if total_cholesterol < 160:
                    points += 0
                if 160 <= total_cholesterol <= 199:
                    points += 1
                if 200 <= total_cholesterol <= 239:
                    points += 1
                if 240 <= total_cholesterol <= 279:
                    points += 2
                if total_cholesterol > 289:
                    points += 2
            # smoking - female
            if smoker:
                if 20 <= age <= 39:
                    points += 9
                if 40 <= age <= 49:
                    points += 7
                if 50 <= age <= 59:
                    points += 4
                if 60 <= age <= 69:
                    points += 2
                if 70 <= age <= 79:
                    points += 1
            else:  # nonsmoker
                points += 0

            # hdl cholesterol - female
            if hdl_cholesterol > 60:
                points -= 1
            if 50 <= hdl_cholesterol <= 59:
                points += 0
            if 40 <= hdl_cholesterol <= 49:
                points += 1
            if hdl_cholesterol < 40:
                points += 2

            # systolic blood pressure
            if not blood_pressure_med_treatment:  # untreated
                if systolic_blood_pressure < 120:
                    points += 0
                if 120 <= systolic_blood_pressure <= 129:
                    points += 1
                if 130 <= systolic_blood_pressure <= 139:
                    points += 2
                if 140 <= systolic_blood_pressure <= 159:
                    points += 3
                if systolic_blood_pressure >= 160:
                    points += 4
            else:  # if the patient is on blood pressure meds
                if systolic_blood_pressure < 120:
                    points += 0
                if 120 <= systolic_blood_pressure <= 129:
                    points += 3
                if 130 <= systolic_blood_pressure <= 139:
                    points += 4
                if 140 <= systolic_blood_pressure <= 159:
                    points += 5
                if systolic_blood_pressure >= 160:
                    points += 6

            # calulate % risk for females
            if points <= 9:
                percent_risk = 0
            elif 9 <= points <= 12:
                percent_risk = 1

            elif 13 <= points <= 14:
                percent_risk = 2

            elif points == 15:
                percent_risk = 3


            elif points == 16:
                percent_risk = 4

            elif points == 17:
                percent_risk = 5

            elif points == 18:
                percent_risk = 6

            elif points == 19:
                percent_risk = 8

            elif points == 20:
                percent_risk = 11

            elif points == 21:
                percent_risk = 14

            elif points == 22:
                percent_risk = 17

            elif points == 23:
                percent_risk = 22

            elif points == 24:
                percent_risk = 27

            elif points >= 25:
                percent_risk = 30

        return percent_risk




# code adopted from https://github.com/brandones/ascvd/blob/master/ascvd/__init__.py
    def compute_ascvd_score(
            self,
            row_SEX,
            row_REGSMOK,
            row_HYPER,
            row_DIABET,
            row_AGE,
            row_MSYS,
            row_TCHOL,
            row_HDL,
    ):
        if row_REGSMOK == 9 or row_TCHOL == 999.97 or row_TCHOL == 999.99 or row_HDL == 999.97 or row_HDL == 999.99 or row_MSYS == 9999.9\
                or row_DIABET == 7 or row_DIABET == 9:
            #print(row_REGSMOK, row_TCHOL, row_HDL,row_MSYS, row_DIABET)
            return 999
        isBlack = False
        if row_SEX == 1:
            isMale = True
        if row_SEX == 2:
            isMale = False
        if row_DIABET == 1:
            diabetic = True
        if row_DIABET == 2:
            diabetic = False
        if row_HYPER == 1:
            hypertensive = True
        if row_HYPER == 0:
            hypertensive = False
        if row_REGSMOK == 1:
            smoker = True
        if row_REGSMOK == 0:
            smoker = False
        age = row_AGE
        if age < 40 or age > 79:
            return 999
        lnAge = math.log(age)
        lnTotalChol = math.log(int(row_TCHOL * 38.67))
        lnHdl = math.log(int(row_HDL * 38.67))
        trlnsbp = math.log(row_MSYS) if hypertensive else 0
        ntlnsbp = 0 if hypertensive else math.log(row_MSYS)
        ageTotalChol = lnAge * lnTotalChol
        ageHdl = lnAge * lnHdl
        agetSbp = lnAge * trlnsbp
        agentSbp = lnAge * ntlnsbp
        ageSmoke = lnAge if smoker else 0
        if isBlack and not isMale:
            s010Ret = 0.95334
            mnxbRet = 86.6081
            predictRet = (
                    17.1141 * lnAge
                    + 0.9396 * lnTotalChol
                    + -18.9196 * lnHdl
                    + 4.4748 * ageHdl
                    + 29.2907 * trlnsbp
                    + -6.4321 * agetSbp
                    + 27.8197 * ntlnsbp
                    + -6.0873 * agentSbp
                    + (0.6908 if smoker else 0)
                    + (0.8738 if diabetic else 0)
            )
        elif not isBlack and not isMale:
            s010Ret = 0.96652
            mnxbRet = -29.1817
            predictRet = (
                    -29.799 * lnAge
                    + 4.884 * lnAge ** 2
                    + 13.54 * lnTotalChol
                    + -3.114 * ageTotalChol
                    + -13.578 * lnHdl
                    + 3.149 * ageHdl
                    + 2.019 * trlnsbp
                    + 1.957 * ntlnsbp
                    + (7.574 if smoker else 0)
                    + -1.665 * ageSmoke
                    + (0.661 if diabetic else 0)
            )
        elif isBlack and isMale:
            s010Ret = 0.89536
            mnxbRet = 19.5425
            predictRet = (
                    2.469 * lnAge
                    + 0.302 * lnTotalChol
                    + -0.307 * lnHdl
                    + 1.916 * trlnsbp
                    + 1.809 * ntlnsbp
                    + (0.549 if smoker else 0)
                    + (0.645 if diabetic else 0)
            )
        else:
            s010Ret = 0.91436
            mnxbRet = 61.1816
            predictRet = (
                    12.344 * lnAge
                    + 11.853 * lnTotalChol
                    + -2.664 * ageTotalChol
                    + -7.99 * lnHdl
                    + 1.769 * ageHdl
                    + 1.797 * trlnsbp
                    + 1.764 * ntlnsbp
                    + (7.837 if smoker else 0)
                    + -1.795 * ageSmoke
                    + (0.658 if diabetic else 0)
            )

        pct = 1 - s010Ret ** math.exp(predictRet - mnxbRet)
        return round(pct * 100 * 10) / 10
