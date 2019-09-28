import m5
from m5.objects import *

root = Root(full_system=False)

root.hello = HelloObject(time_to_wait = '3us', number_of_fires = 1)
root.hello.goodbye_object = GoodbyeObject(buffer_size='1000B')

m5.instantiate()

print("Beginnning to run the simulation")
exit_event = m5.simulate()

print("Exiting at tick %d because %s" % (m5.curTick(), exit_event.getCause()))

