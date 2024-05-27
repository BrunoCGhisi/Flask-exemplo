from controllers.cargosController import cargosController

def cargosRoutes(app):
    app.route('/cargos', methods=['POST', 'GET'])(cargosController)