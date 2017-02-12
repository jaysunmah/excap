import os
import sys

def checkSuccessLogin():
    with open("canary.txt", "r") as f:
        status = f.readlines()[0]
        return status == "success"

