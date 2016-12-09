import logger

class management_task(object):

    def __init__(self, chronos):
        logger.debug('Initializing App management task')
    
    def call(self, chronos, data):
        # Warning: for now, in this call you can block the entire framework if you never return
        logger.debug('Called App management task with data {}', data)
        return 'Got "{}"'.format(data)
