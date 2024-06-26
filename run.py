import subprocess
def run_tests_with_allure():
    command = 'behave --no-capture --format allure_behave.formatter:AllureFormatter -o allure-results/ features -k'
    subprocess.run(command, shell=True)
    #'behave --tags="@smoke" --no-capture --format allure_behave.formatter:AllureFormatter -o allure-results/ features -k'
    # Run Behave scenarios with Allure reporting for tutorial feature
    #subprocess.run(["behave", "--tags=@smoke and @regression", "--tags=@regression", "--no-capture", "--format", "allure_behave.formatter:AllureFormatter", "-o","allure-results/", "features"])
    #"features/Login.feature", "features/DashboardTierCard.feature", "features/DashboardUnityPoints.feature"
    #subprocess.run(["allure", "clean"])
    subprocess.run(["allure", "serve", "allure-results"])

     #Run Behave scenarios with Allure reporting for login feature
    '''
    subprocess.run(
        ["behave", "features/Login.feature", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure-results"])
    '''

if __name__ == "__main__":
    run_tests_with_allure()