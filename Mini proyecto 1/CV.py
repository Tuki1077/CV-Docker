from flask import Flask, render_template, request, url_for
from jinja2 import Template, FileSystemLoader, Environment
import yaml

file_loader = FileSystemLoader('templates')
enviroment = Environment(loader = file_loader)

app = Flask(__name__)

with open('info.yaml') as inf:
  info_yaml = yaml.load(inf, Loader = yaml.FullLoader)

@app.route('/')
def homepage():
  foo = "bar"
  link = info_yaml ['link']
  nombre = info_yaml['informacion_personal']['nombre_completo']
  return render_template ("homepage.html", link= link, nombre = nombre)

@app.route('/cv')
def PaginaPrincipal():
  html = enviroment.get_template('cv.html')
  pic = url_for('static', filename = info_yaml['fotografia'])
  info = info_yaml['informacion_personal']
  infoNombre = info_yaml['informacion_personal']['nombre_completo']
  infoNancimiento = info_yaml['informacion_personal']['pais_de_nacimiento']
  idiomas = info_yaml['informacion_personal']['idiomas']
  edad = info_yaml['informacion_personal']['edad']
  acercademi= info_yaml['informacion_personal']['acerca_de_mi']
  experiencia = info_yaml['informacion_personal']['experiencia']
  intereses = info_yaml['informacion_personal']['intereses']
  tec = info_yaml ['informacion_profesional']['tecnologias']
  ref_per = info_yaml ['informacion_referencias']['referencia_personal']

  return html.render(pic = pic, info = info, nombre = infoNombre, lugardena = infoNancimiento, idioma = idiomas, ed = edad, acercademi = acercademi, exp = experiencia, interes = intereses, tecnologia = tec, InfPersonal = ref_per)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)