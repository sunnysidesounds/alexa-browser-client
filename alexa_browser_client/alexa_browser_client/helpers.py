import command_lifecycle


class AudioLifecycle(command_lifecycle.BaseAudioLifecycle):
    audio_converter_class = command_lifecycle.helpers.WebAudioToWavConverter

    def __init__(self,
        on_command_started, on_command_finished, *args, **kwargs
    ):
        self.on_command_started = on_command_started
        self.on_command_finished = on_command_finished
        super().__init__(*args, **kwargs)

    @property
    def as_file(self):
        return command_lifecycle.helpers.LifeCycleFileLike(self)

    def handle_command_started(self):
        super().handle_command_started()
        self.on_command_started()

    def handle_command_finised(self):
        super().handle_command_finised()
        self.on_command_finished()
