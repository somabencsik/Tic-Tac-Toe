"""Define a mangager, that takes care of scenes."""


class SceneManager:
    def __init__(self) -> None:
        self.scenes: dict[str, "Scene"] = {}
        self.current_scene_idx = 0

    def add_scene(self, scene: "Scene") -> None:
        self.scenes[scene.name] = scene

    def get_next_scene(self) -> "Scene":
        scene = self.scenes[list(self.scenes.keys())[self.current_scene_idx]]
        self.current_scene_idx += 1
        return scene

    def get_scene_by_name(self, scene_name: str) -> "Scene":
        return self.scenes[scene_name]
