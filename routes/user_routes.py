from controllers.user_controller import user_bp

def init_user_routes(app):
    # Register the user blueprint with the app
    app.register_blueprint(user_bp)
