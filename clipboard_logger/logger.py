import clipboard
import csv
import sys
for arg in sys.argv:
    if arg == "start":
        val = ""
        while True:
            if val != clipboard.paste():
                val = clipboard.paste()
                with open("value.csv", mode="a") as csvval:
                    valuewriter = csv.writer(csvval)
                    valuewriter.writerow("{")
                    valuewriter.writerow([val])
                    valuewriter.writerow("}")
                    print("The value received is :", val)
            else:
                pass

