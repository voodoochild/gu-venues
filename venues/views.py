from flask import render_template
from venues import app
import simplejson


@app.route('/', methods=['GET'])
def index():
    """Index view."""
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
