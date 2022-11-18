# from operator import index
from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPaciente import FormularioPaciente

from web.models import Medicos
from web.models import Pacientes

# Create your views here.

# renderizar es Pintar


def Home(request):
    return render(request, 'index.html')


def MedicosVista(request):
    # debo ultilizar la clase formularioMedico
    formulario = FormularioMedico()
    diccionario = {
        "formulario": formulario
    }
    # Activar la recepción de datos
    if request.method == 'POST':
        # validar si los datos son corretos
        datosRecibidos = FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            # Captura los datos
            datos = datosRecibidos.cleaned_data
            # llevar mis datos hacia la BD
            medicoNuevo = Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"],
            )
            medicoNuevo.save()
            print("Exito en la operacion: ")
            

    return render(request, 'registrosMedicos.html', diccionario)

def PacienteVista(request):
    # debo ultilizar la clase formularioPaciente
    formularioP = FormularioPaciente()
    diccionarioP = {
        "formularioP": formularioP
    }
    # Activar la recepción de datos
    if request.method == 'POST':
        # validar si los datos son corretos
        datosRecibidos2 = FormularioPaciente(request.POST)
        if datosRecibidos2.is_valid():
            # Captura los datos
            datos = datosRecibidos2.cleaned_data
            # llevar mis datos hacia la BD
            pacienteNuevo = Pacientes(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                regimen=datos["regimen"],
                grupoingreso=datos["grupoIngreso"],
                cuotamonetaria=datos["cuotaMonetaria"],
                contacto=datos["contacto"],
                correo=datos["correo"],
            )
            pacienteNuevo.save()
            print("Exito en la operacion: ")
            

    return render(request, 'registroPacientes.html', diccionarioP)