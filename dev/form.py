from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UrlForm(FlaskForm):
    """Structure for form to get url to access."""
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField("Get")

    class Meta:
        csrf = False
