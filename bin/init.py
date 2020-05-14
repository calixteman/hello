from hello import models


while True:
    try:
        models.create()
        break
    except:  # NOQA
        pass
