from morse.builder.creator import SensorCreator

class DepthSensor(SensorCreator):
    _classpath = "subseaSintef.sensors.DepthSensor.Depthsensor"
    _blendname = "DepthSensor"

    def __init__(self, name=None):
        SensorCreator.__init__(self, name)

