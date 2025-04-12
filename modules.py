import requests
from requests import get
import sys
from IPython.display import Javascript, display
from google.colab import output, files
def version_check(colabversion):
    url = "https://raw.githubusercontent.com/Prozoon700/MI-Test/main/version.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        latest_version = data[0]['latest_version']
        print(f"Latest version available: {latest_version}")
        user_decision=None
        versionok=None
        if latest_version != colabversion:
            user_decision = output.eval_js("window.confirm('Version out of date. Do you want to continue using this version?')")
            versionok=False
        else:
          print("Yehaa! Version up to date, you can continue using this notebook!")
          versionok=True
    except Exception as e:
        print("Error trying to obtain the latest version... Check that the notebook is up to date.")
        raise Exception(e)
    else:
      if not user_decision and versionok==False:
        raise Exception("Execution stopped: Version out of date. Please update MineColab from discord/github")
      elif user_decision and versionok==True:
        print("Warning: Using old version. Compatibility is not guaranteed.")
