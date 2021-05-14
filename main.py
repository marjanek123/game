from kaa.engine import Engine
from kaa.geometry import Vector
import settings
from scenes.gameplay import GameplayScene
from controller.assets_controler import AssetsController
import registry
with Engine(virtual_resolution=Vector(settings.WIDTH, settings.HEIGHT)) as engine:
    # set window to fullscreen mode
    registry.global_controllers.assets_controller = AssetsController()
    engine.window.fullscreen = True
    # initialize and run the scene
    registry.scenes.gameplay_scene = GameplayScene()
    engine.run(registry.scenes.gameplay_scene)