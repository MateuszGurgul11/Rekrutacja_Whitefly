from . import app, db, celery
from flask import request, render_template, flash, redirect, url_for, send_from_directory
from .forms import MessageForm
from .models import Message

@app.route("/")
def homepage():
    messages = Message.query.all()
    return render_template("form1.html", messages=messages)


@app.route("/add_message", methods=['GET', 'POST'])
def add_message():
    form = MessageForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_message = Message(title=title, content=content)
        db.session.add(new_message)
        db.session.commit()

        flash('Wiadomość została dodana prawidłowo')
        return redirect(url_for('homepage'))
        
    return render_template("add_message.html", form=form)


@app.route("/async_add_message", methods=['GET', 'POST'])
def async_add_message():
    form = MessageForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        add_message_celery.delay(title, content)
        flash('Wiadomość została dodana prawidłowo')
        return redirect(url_for('homepage'))
        
    return render_template("async_add_message.html", form=form)


@app.route("/delete_message/<int:message_id>", methods=['POST'])
def delete_message(message_id):
    message = Message.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash("Wiadomość została usunięta!")
    return redirect(url_for("homepage"))


@app.route("/loaderio-f606fbfce2f93c87c470c8e313ce6146")
def verify_loaderio():
    return send_from_directory(app.static_folder, 'loaderio-f606fbfce2f93c87c470c8e313ce6146')


@celery.task 
def add_message_celery(title, content):
    new_message = Message(title=title, content=content)
    db.session.add(new_message)
    db.session.commit()