import logger

class worker_task(object):

    def call(self, chronos):
        
        import time
        import machine
        import onewire, ds18x20
        
        # the device is on GPIO14
        dat = machine.Pin(14)
        
        temperature = -1
        
        # create the onewire object
        ds = ds18x20.DS18X20(onewire.OneWire(dat))
        
        # scan for devices on the bus
        roms = ds.scan()
        
        # loop 10 times and print all temperatures
        #for i in range(10):
        #print('temperatures:', end=' ')
        ds.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            #print(ds.read_temp(rom), end=' ')
            temperature = ds.read_temp(rom)
        #print()
            
        data ={'temperature_C': temperature}     

        return data
