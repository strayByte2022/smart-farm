from rs485 import *
import time

MIXER_ID = 1
AREA_SELECTOR = 4
PUMP_IN = 7
PUMP_OUT = 8


def fertilizer_on(relay_id):
    setDevice1(True)

    print('Fertilizer ' + str(relay_id) + ' on')


def fertilizer_off(relay_id):
    setDevice1(False)
    print('Fertilizer ' + str(relay_id) + ' off')

def pump_in(relay_id):
    setDevice1(True)
    print('Pump in ID ' + str(relay_id) + 'started')
    time.sleep(20)
    setDevice1(False)
    print('Pump in ID ' + str(relay_id) + ' off')

def pump_out(relay_id):
    setDevice1(True)
    print('Pump out ID ' + str(relay_id) + ' started')
    time.sleep(20)
    setDevice1(False)
    print('Pump out ID ' + str(relay_id) + ' off')

def control_mixer(relay_id):
    fertilizer_on(relay_id)
    time.sleep(10)
    fertilizer_off(relay_id)

def irrigation():
    control_mixer(MIXER_ID)
    control_mixer(MIXER_ID + 1)
    control_mixer(MIXER_ID + 2)
    pump_in(PUMP_IN)
    pump_out(PUMP_OUT)


