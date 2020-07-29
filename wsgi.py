
from lib.logging import init_logging
from sif.app import create_app

if __name__ == '__main__':
    init_logging(console=True)
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=8100)
else:
    init_logging(console=True)
    app = create_app()


