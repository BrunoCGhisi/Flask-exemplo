from controllers.clientesController import clienteController, clientesHtmlController

def clientesRoutes(app):
    app.route('/clientesHTML', method=['GET'])(clientesHtmlController)
    app.route('/clientes', methods=['GET', 'POST', 'PUT', 'DELETE'])(clienteController)