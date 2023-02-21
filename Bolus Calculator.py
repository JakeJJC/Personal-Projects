print("Welcome to Jake's Bolus Calculator\n")
input("Press any key to continue\n")

def calc():
    whichCalculator = input("Would you like to calculate your (1) carb correction, (2) insulin correction or (3) both? : ")
    
    # Check to see if the entered input is an integer
    try:
        intCheck = int(whichCalculator)
    except ValueError:
        print("\nPlease use a number between 1 and 3\n")
        calc()
        return

    # Carb Correction Calculator
    if int(whichCalculator) == 1:
        carbsAmount = input("\nHow many carbohydrates are you going to be eating? : ")
        carbsCorrection = input("\nWhat is your current carbohydrate correction factor? (1:15 enter 15) : ")
        
        # Calculates how much insulin is needed for correction
        carbResult = float(carbsAmount) / float (carbsCorrection)

        print("\nYou will need " + str(carbResult) + " units of insulin.\n")

        input("Press any key to exit the calculator.")
        
    # Insulin Correction Calculator
    elif int(whichCalculator) == 2:
        bloodGlucose = input("\nWhat is your current blood glucose levels? : ")
        correctionTarget = input("\nWhat is your target blood glucose? : ")
        correctionFactor = input("\nWhat is your correction factor? : ")

        # Calculates how much correction is needed
        bgcorrectionResult1 = float(bloodGlucose) - float(correctionTarget) 
        # Calculates how much insulin is needed for correction 
        bgcorrectionResult2 = float(bgcorrectionResult1) / float(correctionFactor)

        print("\nYou will need " + str(round(bgcorrectionResult2,1)) + " units of insulin.\n")

        input("Press any key to exit the calculator.")

    # Both Correction Calculators together
    elif int(whichCalculator) == 3:
        carbsAmount = input("\nHow many carbohydrates are you going to be eating? : ")
        carbsCorrection = input("\nWhat is your current carbohydrate correction factor? (1:15 enter 15) : ")
        
        # Calculates how much insulin is needed for correction
        carbResult = float(carbsAmount) / float (carbsCorrection)

        bloodGlucose = input("\nWhat is your current blood glucose levels? : ")
        correctionTarget = input("\nWhat is your target blood glucose? : ")
        correctionFactor = input("\nWhat is your correction factor? : ")

        # Calculates how much correction is needed
        bgcorrectionResult1 = float(bloodGlucose) - float(correctionTarget) 
        # Calculates how much insulin is needed for correction 
        bgcorrectionResult2 = float(bgcorrectionResult1) / float(correctionFactor)

        # Adds both values together to find the total amount of insulin required for correction
        finalResult = float(carbResult) + float(bgcorrectionResult2)

        print("\nYou will need " + str(round(finalResult,1)) + " units of insulin.\n")

        input("Press any key to exit the calculator.")
    
    # Asks the user to use a number between 1 and 3 if they input any other number
    else:
        print("\nPlease use a number between 1 and 3\n")
        calc()
        return
calc()