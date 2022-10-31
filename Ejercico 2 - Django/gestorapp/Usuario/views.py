from django.shortcuts import get_object_or_404, redirect, render
from Usuario.forms import UsuarioForm
from Usuario.models import Usuario

def detalleUsuario(req, id) :
    usuario = get_object_or_404(Usuario, pk = id);
    return render(req, 'DetalleUsuario.html', {'usuario': usuario});

def nuevoUsuario(req) :
    if req.method == "POST":
        formaUsuario = UsuarioForm(req.POST);

        if formaUsuario.is_valid():
            formaUsuario.save();
            return redirect('usuarioList');
    else:
        formaUsuario = UsuarioForm();
        return render(req, 'AgregarUsuario.html', {'formaUsuario': formaUsuario})

def editarUsuario(req, id):
    usuario = get_object_or_404(Usuario, pk = id);
    if req.method == "POST":
        formaUsuario = UsuarioForm(req.POST, instance = usuario);

        if formaUsuario.is_valid():
            formaUsuario.save();
            return redirect('usuarioList');
    else:
        formaUsuario = UsuarioForm(instance = usuario);
        return render(req, 'EditarUsuario.html', {'formaUsuario': formaUsuario})

def eliminarUsuario(req, id):
    usuario = get_object_or_404(Usuario, pk = id);
    if usuario:
        usuario.delete();
        return redirect('usuarioList');