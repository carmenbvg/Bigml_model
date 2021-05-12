def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/609b8fa6fa7cb61321000006

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 143):
        if (glucose > 166):
            if (bmi is None):
                return u'True'
            if (bmi > 35.25):
                return u'True'
            if (bmi <= 35.25):
                if (age is None):
                    return u'True'
                if (age > 24):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.3135):
                        return u'True'
                    if (diabetes_pedigree <= 0.3135):
                        if (bmi > 30.7):
                            if (pregnancies is None):
                                return u'False'
                            if (pregnancies > 6):
                                return u'False'
                            if (pregnancies <= 6):
                                if (bmi > 31.9):
                                    return u'True'
                                if (bmi <= 31.9):
                                    return u'False'
                        if (bmi <= 30.7):
                            return u'True'
                if (age <= 24):
                    return u'False'
        if (glucose <= 166):
            if (diabetes_pedigree is None):
                return u'True'
            if (diabetes_pedigree > 0.3174):
                if (age is None):
                    return u'True'
                if (age > 50):
                    return u'True'
                if (age <= 50):
                    if (bmi is None):
                        return u'True'
                    if (bmi > 42.85):
                        return u'True'
                    if (bmi <= 42.85):
                        if (pregnancies is None):
                            return u'True'
                        if (pregnancies > 1):
                            if (insulin is None):
                                return u'True'
                            if (insulin > 108):
                                if (pregnancies > 3):
                                    if (pregnancies > 6):
                                        if (bmi > 34.5):
                                            if (bmi > 36.3):
                                                if (blood_pressure is None):
                                                    return u'True'
                                                if (blood_pressure > 84):
                                                    return u'False'
                                                if (blood_pressure <= 84):
                                                    return u'True'
                                            if (bmi <= 36.3):
                                                return u'False'
                                        if (bmi <= 34.5):
                                            return u'True'
                                    if (pregnancies <= 6):
                                        if (bmi > 37.45):
                                            return u'True'
                                        if (bmi <= 37.45):
                                            return u'False'
                                if (pregnancies <= 3):
                                    return u'True'
                            if (insulin <= 108):
                                return u'True'
                        if (pregnancies <= 1):
                            if (diabetes_pedigree > 0.373):
                                return u'False'
                            if (diabetes_pedigree <= 0.373):
                                if (diabetes_pedigree > 0.345):
                                    return u'True'
                                if (diabetes_pedigree <= 0.345):
                                    return u'False'
            if (diabetes_pedigree <= 0.3174):
                if (skinfold is None):
                    return u'False'
                if (skinfold > 28):
                    return u'False'
                if (skinfold <= 28):
                    if (diabetes_pedigree > 0.1785):
                        if (bmi is None):
                            return u'False'
                        if (bmi > 36.3):
                            return u'True'
                        if (bmi <= 36.3):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 85):
                                return u'True'
                            if (blood_pressure <= 85):
                                if (bmi > 31.4):
                                    if (bmi > 33.1):
                                        return u'False'
                                    if (bmi <= 33.1):
                                        if (blood_pressure > 68):
                                            return u'True'
                                        if (blood_pressure <= 68):
                                            return u'False'
                                if (bmi <= 31.4):
                                    return u'False'
                    if (diabetes_pedigree <= 0.1785):
                        return u'True'
    if (glucose <= 143):
        if (bmi is None):
            return u'False'
        if (bmi > 26.62544):
            if (age is None):
                return u'False'
            if (age > 30):
                if (glucose > 89):
                    if (age > 58):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.714):
                            return u'True'
                        if (diabetes_pedigree <= 0.714):
                            return u'False'
                    if (age <= 58):
                        if (glucose > 107):
                            if (bmi > 42.98333):
                                return u'True'
                            if (bmi <= 42.98333):
                                if (blood_pressure is None):
                                    return u'True'
                                if (blood_pressure > 67):
                                    if (insulin is None):
                                        return u'True'
                                    if (insulin > 109):
                                        if (age > 41):
                                            return u'True'
                                        if (age <= 41):
                                            if (insulin > 175):
                                                return u'False'
                                            if (insulin <= 175):
                                                if (glucose > 128):
                                                    if (bmi > 36.15):
                                                        return u'True'
                                                    if (bmi <= 36.15):
                                                        return u'False'
                                                if (glucose <= 128):
                                                    return u'True'
                                    if (insulin <= 109):
                                        if (skinfold is None):
                                            return u'False'
                                        if (skinfold > 33):
                                            return u'False'
                                        if (skinfold <= 33):
                                            if (blood_pressure > 69):
                                                if (blood_pressure > 73):
                                                    if (bmi > 34.05):
                                                        if (diabetes_pedigree is None):
                                                            return u'False'
                                                        if (diabetes_pedigree > 0.9005):
                                                            return u'True'
                                                        if (diabetes_pedigree <= 0.9005):
                                                            return u'False'
                                                    if (bmi <= 34.05):
                                                        if (glucose > 133):
                                                            if (blood_pressure > 92):
                                                                return u'True'
                                                            if (blood_pressure <= 92):
                                                                return u'False'
                                                        if (glucose <= 133):
                                                            if (diabetes_pedigree is None):
                                                                return u'True'
                                                            if (diabetes_pedigree > 0.502):
                                                                return u'True'
                                                            if (diabetes_pedigree <= 0.502):
                                                                if (bmi > 33.3):
                                                                    return u'True'
                                                                if (bmi <= 33.3):
                                                                    if (bmi > 27.4):
                                                                        if (diabetes_pedigree > 0.294):
                                                                            if (skinfold > 25):
                                                                                return u'False'
                                                                            if (skinfold <= 25):
                                                                                return u'True'
                                                                        if (diabetes_pedigree <= 0.294):
                                                                            return u'False'
                                                                    if (bmi <= 27.4):
                                                                        return u'True'
                                                if (blood_pressure <= 73):
                                                    return u'True'
                                            if (blood_pressure <= 69):
                                                return u'False'
                                if (blood_pressure <= 67):
                                    if (age > 32):
                                        return u'True'
                                    if (age <= 32):
                                        return u'False'
                        if (glucose <= 107):
                            if (skinfold is None):
                                return u'False'
                            if (skinfold > 37):
                                return u'False'
                            if (skinfold <= 37):
                                if (bmi > 40.2):
                                    return u'True'
                                if (bmi <= 40.2):
                                    if (bmi > 29.55):
                                        if (glucose > 104):
                                            if (bmi > 30.05):
                                                return u'False'
                                            if (bmi <= 30.05):
                                                if (blood_pressure is None):
                                                    return u'False'
                                                if (blood_pressure > 82):
                                                    return u'False'
                                                if (blood_pressure <= 82):
                                                    return u'True'
                                        if (glucose <= 104):
                                            if (age > 39):
                                                if (blood_pressure is None):
                                                    return u'False'
                                                if (blood_pressure > 73):
                                                    if (insulin is None):
                                                        return u'True'
                                                    if (insulin > 130):
                                                        return u'True'
                                                    if (insulin <= 130):
                                                        if (age > 51):
                                                            return u'True'
                                                        if (age <= 51):
                                                            if (bmi > 39.1):
                                                                return u'True'
                                                            if (bmi <= 39.1):
                                                                return u'False'
                                                if (blood_pressure <= 73):
                                                    return u'False'
                                            if (age <= 39):
                                                return u'True'
                                    if (bmi <= 29.55):
                                        return u'False'
                if (glucose <= 89):
                    return u'False'
            if (age <= 30):
                if (bmi > 42.49167):
                    if (glucose > 126):
                        return u'True'
                    if (glucose <= 126):
                        if (bmi > 45.4):
                            if (bmi > 56.15):
                                return u'False'
                            if (bmi <= 56.15):
                                return u'True'
                        if (bmi <= 45.4):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.6895):
                                return u'True'
                            if (diabetes_pedigree <= 0.6895):
                                return u'False'
                if (bmi <= 42.49167):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 31):
                        if (blood_pressure is None):
                            return u'False'
                        if (blood_pressure > 69):
                            if (insulin is None):
                                return u'False'
                            if (insulin > 154):
                                if (bmi > 35):
                                    return u'False'
                                if (bmi <= 35):
                                    return u'True'
                            if (insulin <= 154):
                                return u'False'
                        if (blood_pressure <= 69):
                            if (bmi > 35.25):
                                if (diabetes_pedigree is None):
                                    return u'False'
                                if (diabetes_pedigree > 0.327):
                                    if (age > 22):
                                        if (glucose > 125):
                                            return u'True'
                                        if (glucose <= 125):
                                            if (pregnancies is None):
                                                return u'False'
                                            if (pregnancies > 1):
                                                if (blood_pressure > 57):
                                                    return u'True'
                                                if (blood_pressure <= 57):
                                                    return u'False'
                                            if (pregnancies <= 1):
                                                return u'False'
                                    if (age <= 22):
                                        return u'False'
                                if (diabetes_pedigree <= 0.327):
                                    return u'False'
                            if (bmi <= 35.25):
                                if (bmi > 30.55):
                                    if (pregnancies is None):
                                        return u'True'
                                    if (pregnancies > 5):
                                        return u'False'
                                    if (pregnancies <= 5):
                                        return u'True'
                                if (bmi <= 30.55):
                                    return u'False'
                    if (skinfold <= 31):
                        if (pregnancies is None):
                            return u'False'
                        if (pregnancies > 5):
                            if (glucose > 118):
                                return u'True'
                            if (glucose <= 118):
                                return u'False'
                        if (pregnancies <= 5):
                            if (age > 22):
                                if (diabetes_pedigree is None):
                                    return u'False'
                                if (diabetes_pedigree > 0.74225):
                                    if (bmi > 32.25):
                                        return u'True'
                                    if (bmi <= 32.25):
                                        if (skinfold > 21):
                                            return u'False'
                                        if (skinfold <= 21):
                                            return u'True'
                                if (diabetes_pedigree <= 0.74225):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 40):
                                        return u'False'
                                    if (insulin <= 40):
                                        if (age > 25):
                                            return u'False'
                                        if (age <= 25):
                                            if (bmi > 35.65):
                                                return u'True'
                                            if (bmi <= 35.65):
                                                if (age > 23):
                                                    return u'False'
                                                if (age <= 23):
                                                    if (skinfold > 9):
                                                        return u'False'
                                                    if (skinfold <= 9):
                                                        return u'True'
                            if (age <= 22):
                                return u'False'
        if (bmi <= 26.62544):
            if (glucose > 132):
                if (skinfold is None):
                    return u'False'
                if (skinfold > 7):
                    return u'False'
                if (skinfold <= 7):
                    if (diabetes_pedigree is None):
                        return u'False'
                    if (diabetes_pedigree > 0.222):
                        return u'True'
                    if (diabetes_pedigree <= 0.222):
                        return u'False'
            if (glucose <= 132):
                return u'False'
