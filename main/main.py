from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify
from config.config import ROOT
import codecs
from markdown import Markdown
import glob

blueprint = Blueprint('main', __name__,
                      template_folder='../',
                      static_url_path='/static',
                      static_folder='../static')

templates_path = "main/templates/"
posts_folder = "main/posts/"

# --------------------------------------------
# ------------------ HOME --------------------
# --------------------------------------------
from datetime import datetime


@blueprint.route("/", methods=['GET'])
def index():
    path = ROOT + "/mdposts/*.md"
    meta_list = []

    for file in glob.glob(path):
        html = codecs.open(file, mode='r', encoding="UTF-8").read()
        md = Markdown(extensions=['meta'])
        md.convert(html)
        meta_list.append(md.Meta)

    meta_list = sorted(meta_list, key=lambda meta: datetime.strptime(meta['date'][0], '%d %b %Y'), reverse=True)

    return render_template(templates_path + "index.html", metainfos=meta_list)


@blueprint.route("/post/<path>", methods=['GET'])
def post(path):
    path = ROOT + "/mdposts/" + path + ".*"
    content = ""

    for file in glob.glob(path):
        content = codecs.open(file, mode='r', encoding="UTF-8").read()
        content = content.replace("$base", request.url_root)
        print(content)

    md = Markdown(extensions=['meta'])
    html = md.convert(content)
    return render_template(templates_path + "post.html", content=html, metainfos=md.Meta)


@blueprint.route("/sobre", methods=['GET'])
def about():
    return render_template(templates_path + "about.html")
