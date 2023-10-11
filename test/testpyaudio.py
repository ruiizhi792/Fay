import pyaudio
audio = pyaudio.PyAudio()
print(audio.get_device_count())
# B站官方账号有另一版本audio检索,可以尝试在系统问题时使用
