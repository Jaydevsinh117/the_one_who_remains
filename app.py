from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# App setup
app = Flask(
    __name__, template_folder="templates"
)  # Ensures Flask knows where to look for templates
CORS(app)
app.secret_key = "your_secret_key_here"

# Set up the SQLAlchemy database URI (SQLite in this case)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "gita_project.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
    False  # Disable Flask-SQLAlchemy modification tracking
)

# Initialize the database
from models.user_model import db

db.init_app(app)  # Initialize the db with the app

# Import routes (controllers)
from controllers.user_controller import user_bp

# Uncomment and import other controllers when they are implemented
# from controllers.product_controller import product_bp
# from controllers.blog_controller import blog_bp
# from controllers.quote_controller import quote_bp
# from controllers.chapter_controller import chapter_bp
# from controllers.admin_controller import admin_bp

# Register Blueprints
app.register_blueprint(user_bp)
# Register other blueprints when implemented
# app.register_blueprint(product_bp)
# app.register_blueprint(blog_bp)
# app.register_blueprint(quote_bp)
# app.register_blueprint(chapter_bp)
# app.register_blueprint(admin_bp)


# Routes for rendering pages
@app.route("/")
@app.route("/")
def home():
    return render_template(
        "home.html"
    )  # ✅ This will render the actual home page content


@app.route("/about")
def about():
    return render_template("about.html")  # Render the about.html template


@app.route("/contact")
def contact():
    return render_template("contact.html")  # Render the contact.html template


@app.route("/register")
def register():
    return render_template("register.html")  # Render the register.html template


@app.route("/product")
def product():
    return render_template("product.html")  # Render the product.html template


# @app.route("/showcase")
# def showcase():
#     return render_template("showcase.html")  # Render the showcase.html template
@app.route("/showcase")
def showcase():
    shlokas = [
        {
            "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।",
            "english": "You have the right to perform your prescribed duties, but you are not entitled to the fruits of your actions.",
            "chapter": 2,
            "verse": 47,
            "category": "karma",
            "audio_male": "/static/audio/2_47_male.mp3",
            "audio_female": "/static/audio/2_47_female.mp3",
        },
        {
            "sanskrit": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत ।",
            "english": "Whenever there is a decline in righteousness and an increase in unrighteousness, I manifest Myself.",
            "chapter": 4,
            "verse": 7,
            "category": "bhakti",
            "audio_male": "/static/audio/4_7_male.mp3",
            "audio_female": "/static/audio/4_7_female.mp3",
        },
        {
            "sanskrit": "न जायते म्रियते वा कदाचित् ।",
            "english": "The soul is neither born, nor does it ever die.",
            "chapter": 2,
            "verse": 20,
            "category": "jnana",
            "audio_male": "/static/audio/2_20_male.mp3",
            "audio_female": "/static/audio/2_20_female.mp3",
        },
        {
            "sanskrit": "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय ।",
            "english": "Be steadfast in yoga, O Arjuna. Perform your duty and abandon all attachment to success or failure.",
            "chapter": 2,
            "verse": 48,
            "category": "karma",
            "audio_male": "/static/audio/2_48_male.mp3",
            "audio_female": "/static/audio/2_48_female.mp3",
        },
        {
            "sanskrit": "कर्मण्यकर्म यः पश्येत् ।",
            "english": "He who sees inaction in action, and action in inaction, is intelligent among men.",
            "chapter": 4,
            "verse": 18,
            "category": "jnana",
            "audio_male": "/static/audio/4_18_male.mp3",
            "audio_female": "/static/audio/4_18_female.mp3",
        },
        {
            "sanskrit": "सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ ।",
            "english": "A person who is not disturbed by happiness and distress and is steady in both is certainly eligible for liberation.",
            "chapter": 2,
            "verse": 38,
            "category": "moksha",
            "audio_male": "/static/audio/2_38_male.mp3",
            "audio_female": "/static/audio/2_38_female.mp3",
        },
        {
            "sanskrit": "मच्चित्तः सर्वदुर्गाणि मत्प्रसादात्तरिष्यसि ।",
            "english": "By becoming conscious of Me, you will overcome all difficulties by My grace.",
            "chapter": 18,
            "verse": 58,
            "category": "bhakti",
            "audio_male": "/static/audio/18_58_male.mp3",
            "audio_female": "/static/audio/18_58_female.mp3",
        },
        {
            "sanskrit": "मत्तः परतरं नान्यत्किञ्चिदस्ति धनञ्जय ।",
            "english": "There is no truth superior to Me. Everything rests upon Me, as pearls are strung on a thread.",
            "chapter": 7,
            "verse": 7,
            "category": "jnana",
            "audio_male": "/static/audio/7_7_male.mp3",
            "audio_female": "/static/audio/7_7_female.mp3",
        },
        {
            "sanskrit": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज ।",
            "english": "Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.",
            "chapter": 18,
            "verse": 66,
            "category": "moksha",
            "audio_male": "/static/audio/18_66_male.mp3",
            "audio_female": "/static/audio/18_66_female.mp3",
        },
        {
            "sanskrit": "अहं सर्वस्य प्रभवो मत्तः सर्वं प्रवर्तते ।",
            "english": "I am the source of all spiritual and material worlds. Everything emanates from Me.",
            "chapter": 10,
            "verse": 8,
            "category": "bhakti",
            "audio_male": "/static/audio/10_8_male.mp3",
            "audio_female": "/static/audio/10_8_female.mp3",
        },
    ]
    return render_template("showcase.html", shlokas=shlokas)




@app.route("/blog")
def blog():
    return render_template("blog.html")  # Render the blog.html template


@app.route("/deep-dive")
def deep_dive():
    return render_template("deep_dive.html")  # Render the deep_dive.html template


@app.route("/deep-dive/chapter-1")
def chapter_1():
    return render_template("deep-dive/chapter_1.html")


@app.route("/deep-dive/chapter-2")
def chapter_2():
    return render_template("deep-dive/chapter_2.html")


@app.route("/deep-dive/chapter-3")
def chapter_3():
    return render_template("deep-dive/chapter_3.html")


@app.route("/deep-dive/chapter-4")
def chapter_4():
    return render_template("deep-dive/chapter_4.html")


@app.route("/deep-dive/chapter-5")
def chapter_5():
    return render_template("deep-dive/chapter_5.html")


@app.route("/deep-dive/chapter-6")
def chapter_6():
    return render_template("deep-dive/chapter_6.html")


@app.route("/deep-dive/chapter-7")
def chapter_7():
    return render_template("deep-dive/chapter_7.html")


@app.route("/deep-dive/chapter-8")
def chapter_8():
    return render_template("deep-dive/chapter_8.html")


@app.route("/deep-dive/chapter-9")
def chapter_9():
    return render_template("deep-dive/chapter_9.html")


@app.route("/deep-dive/chapter-10")
def chapter_10():
    return render_template("deep-dive/chapter_10.html")


@app.route("/deep-dive/chapter-11")
def chapter_11():
    return render_template("deep-dive/chapter_11.html")


@app.route("/deep-dive/chapter-12")
def chapter_12():
    return render_template("deep-dive/chapter_12.html")


@app.route("/deep-dive/chapter-13")
def chapter_13():
    return render_template("deep-dive/chapter_13.html")


@app.route("/deep-dive/chapter-14")
def chapter_14():
    return render_template("deep-dive/chapter_14.html")


@app.route("/deep-dive/chapter-15")
def chapter_15():
    return render_template("deep-dive/chapter_15.html")


@app.route("/deep-dive/chapter-16")
def chapter_16():
    return render_template("deep-dive/chapter_16.html")


@app.route("/deep-dive/chapter-17")
def chapter_17():
    return render_template("deep-dive/chapter_17.html")


@app.route("/deep-dive/chapter-18")
def chapter_18():
    return render_template("deep-dive/chapter_18.html")




if __name__ == "__main__":
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the app
    app.run(debug=True)
