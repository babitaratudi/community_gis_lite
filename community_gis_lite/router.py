class DatastoreRouter(object):

    route_app_labels = {'form_cms'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'form_cms':
            return 'datastore'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'form_cms':
            return 'datastore'
        return 'default'

    def allow_syncdb(self, db, model):
        if db == 'datastore' or model._meta.app_label == "form_cms":
            return True # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return False