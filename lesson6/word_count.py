import urllib.request
import ssl


if __name__ == "__main__":
    data = str(
        urllib.request.urlopen(
            "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy3/main/Lekcia6/scratch.txt",
            context=ssl._create_unverified_context()
        ).read().decode("utf-8"))

    print(data)