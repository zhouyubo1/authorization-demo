from . import user_bp


@user_bp.route('/register', methods=['POST'])
def register():
    pass


@user_bp.route('/login', methods=['POST'])
def login():
    pass