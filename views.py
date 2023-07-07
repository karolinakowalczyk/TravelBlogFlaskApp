import datetime
from flask import Blueprint, Flask, session, render_template, request, redirect, flash, url_for
from firebaseConfig import getAuth, getDb, getBucket
import os


from forms.registrationForm import RegistrationForm
from forms.addPostForm import AddPostForm


auth = getAuth()
db = getDb()
bucket = getBucket()


absolutePath = os.path.dirname(__file__)

site = Blueprint('site', __name__, static_folder="static", template_folder='templates')

@site.route("/")
def home():
    return render_template('home.html')


@ site.route("/register", methods=['POST', 'GET'])
def register():
    registerForm = RegistrationForm(request.form)
    if request.method == 'POST' and registerForm.validate():
        email = registerForm.email.data
        password = registerForm.password.data
        try:
            auth.create_user_with_email_and_password(email, password)
            return redirect('/login')
        except:
            return redirect('/register')

    return render_template('register.html', registerForm=registerForm)


@ site.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.sign_in_with_email_and_password(email, password)
            session['user'] = auth.current_user['localId']
            return redirect('/')
        except Exception as e:
            print(e)
            return redirect('/login')

    return render_template('login.html')


@ site.route('/logout')
def logout():
    if session.get('user') != None:
        session.pop('user')
    return redirect('/')


@ site.route("/my-posts", methods=['POST', 'GET'])
def myPosts():
    userPosts = db.collection('posts').where(
        'userId', "==", session['user']).get()
    userPostsData = []

    for post in userPosts:
        userPostsData.append(post.to_dict())
    for p in userPostsData:
        if p["image"]:
            blob = bucket.get_blob("images/" + p["image"])
            imageUrl = blob.generate_signed_url(
                expiration=datetime.timedelta(
                    days=365))
            p["image"] = imageUrl
    return render_template('my-posts.html', userPostsData=userPostsData)

hashtags = []
filename = None


@ site.route('/add-hashtag', methods=['POST'])
def addHashtag():
    global hashtags
    hashtag = request.get_json()
    hashtags.append(hashtag['hashtag'])
    return hashtags


@ site.route('/remove-hashtag', methods=['POST'])
def removeHashtag():
    global hashtags
    hashtag = request.get_json()
    hashtags.remove(hashtag['hashtag'])
    return hashtags

@ site.route("/add-post", methods=['POST', 'GET'])
def addPost():
    global fileUrl
    fileUrl = None
    global filename
    addPostForm = AddPostForm()

    if request.method == 'POST' and addPostForm.validate():
        addSubmit = request.form.get("add")
        uploadSubmit = request.form.get("upload")
        if uploadSubmit is not None:
            image = addPostForm.images.data
            if image is not None:
                filename = image.filename
                blob = bucket.blob('images/' + filename)
                blob.upload_from_string(image.read(), content_type='image/jpeg')
                blob.make_public()
                fileUrl = blob.public_url
            else:
                fileUrl = None

        elif addSubmit is not None:
            global hashtags
            data = {"userId": session['user'], "title": addPostForm.title.data,
                    "author": addPostForm.author.data, "content": addPostForm.content.data, "hashtags": hashtags, "image": filename}

            db.collection('posts').document().set(data)
            hashtags = []
            filename = []
            return redirect('/my-posts')

    return render_template('add-post.html', addPostForm=addPostForm, fileUrl=fileUrl)