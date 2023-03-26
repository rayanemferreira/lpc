import sys
import controller, eventmanager

import model
import views


def run(mode):
    evManager = eventmanager.EventManager()
    gamemodel = model.Game(evManager)
    graphics = views.GraphicalView(evManager, gamemodel)
    keyboard = controller.Controller(evManager, gamemodel)

    gamemodel.run(mode)



if __name__ == "__main__":
    try:
        if sys.argv[1].lower() == "test":
            run("test")
    except IndexError:
        run(None)
