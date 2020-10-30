# Flask WTF - 添加WTForms的渲染和验证

# class ContactForm(Form):
#    name = TextField("Name Of Student")


# <input id = "csrf_token" name = "csrf_token" type = "hidden" />
# <label for = "name">Name Of Student</label><br>
# <input id = "name" name = "name" type = "text" value = "" />


from flask import Flask, render_template, request, flash

from w3cschool.forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)