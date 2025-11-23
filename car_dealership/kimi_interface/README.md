# Sistema de Validación de Email para Aplicaciones Tkinter

## Descripción

Este proyecto proporciona un sistema robusto y reutilizable para validar direcciones de email en aplicaciones Tkinter. Incluye funciones de validación, utilidades compartidas y ejemplos de implementación en diferentes contextos.

## Características

- ✅ **Validación de email robusta** usando expresiones regulares
- ✅ **Mensajes de error descriptivos** para el usuario
- ✅ **Validación reutilizable** en múltiples clases y contextos
- ✅ **Validación automática** al perder el foco del campo
- ✅ **Validación manual** mediante botones
- ✅ **Validación de otros campos** (teléfono, solo letras, etc.)

## Archivos del Proyecto

### Archivos Principales

1. **`validaciones_utils.py`** - Módulo de utilidades de validación
   - `ValidacionesUtils`: Clase con métodos estáticos para validaciones
   - `crear_validador_email()`: Función auxiliar para crear validadores

2. **`sales_man_interface_mejorado.py`** - Tu clase mejorada con validación de email
   - Integración completa de las validaciones
   - Validación automática y manual
   - Validación de múltiples campos

3. **`ejemplos_uso_validacion.py`** - Ejemplos de uso en diferentes contextos
   - `ClienteInterface`: Gestión de clientes
   - `ProveedorInterface`: Gestión de proveedores  
   - `EmpleadoInterface`: Gestión de empleados

4. **`demo_validacion_email.py`** - Aplicación de demostración ejecutable
   - Interfaz gráfica completa
   - Múltiples pestañas con diferentes ejemplos
   - Validación en tiempo real

## Uso Rápido

### 1. Importar las utilidades

```python
from validaciones_utils import ValidacionesUtils, crear_validador_email
```

### 2. Validación básica de email

```python
# Validación simple
email = "usuario@dominio.com"
if ValidacionesUtils.validar_email(email):
    print("Email válido")
else:
    print("Email inválido")

# Validación con mensaje de error en GUI
if ValidacionesUtils.validar_email_con_gui(email, ventana_principal):
    print("Email válido")
```

### 3. Integración en Tkinter

```python
# Validación automática al perder foco
self.txt_email.bind('<FocusOut>', self.validar_email_perdida_foco)

def validar_email_perdida_foco(self, event=None):
    email = self.txt_email.get()
    ValidacionesUtils.validar_email_con_gui(email, self.parent)
```

### 4. Crear validador reutilizable

```python
# Crear una función de validación para un Entry específico
validador = crear_validador_email(self.txt_email, self.parent)

# Usarla cuando sea necesario
validador()  # Ejecuta la validación
```

## Ejemplos de Implementación

### En tu clase Sales_man_interface

```python
def validate_salesman_info(self):
    """Valida toda la información del vendedor"""
    
    # Validar formato del email
    if not ValidacionesUtils.validar_email(self.txt_email.get()):
        messagebox.showerror("ERROR!!!", 
                           f"El email '{self.txt_email.get()}' no tiene un formato válido.")
        return False
    
    # Resto de validaciones...
    return True
```

### En otras clases

```python
class ClienteInterface:
    def __init__(self, parent_window):
        self.parent = parent_window
        self.setup_ui()
    
    def setup_ui(self):
        self.txt_email = tk.Entry(self.parent)
        self.txt_email.bind('<FocusOut>', self.validar_email_perdida_foco)
    
    def validar_email_perdida_foco(self, event=None):
        email = self.txt_email.get()
        if email.strip():
            ValidacionesUtils.validar_email_con_gui(email, self.parent)
```

## Formatos de Email Válidos

La validación acepta los siguientes formatos:

- ✅ `usuario@dominio.com`
- ✅ `user.name@example.com`
- ✅ `user-name@domain.co.uk`
- ✅ `user_name@sub.domain.com`
- ✅ `123@domain.com`

**No válidos:**
- ❌ `usuario@dominio` (sin extensión)
- ❌ `usuario@` (sin dominio)
- ❌ `@dominio.com` (sin usuario)
- ❌ `usuario dominio.com` (sin @)

## Otras Validaciones Disponibles

Además de emails, el módulo incluye:

```python
# Validar teléfono
ValidacionesUtils.validar_telefono("+1-555-123-4567")

# Validar solo letras
ValidacionesUtils.validar_solo_letras("Juan Pérez")

# Validar campo no vacío
ValidacionesUtils.validar_no_vacio(valor, "Nombre del campo")
```

## Ejecutar la Demo

Para ver el sistema en acción:

```bash
python demo_validacion_email.py
```

Esto abrirá una ventana con:
- Validación básica de email
- Ejemplos en gestión de clientes
- Ejemplos en gestión de proveedores
- Ejemplos en gestión de empleados

## Personalización

### Modificar el patrón de validación

En `validaciones_utils.py`, puedes ajustar el patrón regex:

```python
patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

### Personalizar mensajes de error

```python
messagebox.showerror("Título Personalizado", 
                     "Mensaje de error personalizado", 
                     parent=ventana_padre)
```

## Mejores Prácticas

1. **Validar en múltiples puntos**:
   - Al perder el foco del campo
   - Antes de enviar el formulario
   - Al cambiar entre pestañas

2. **Proporcionar retroalimentación inmediata**:
   - Usar colores para indicar validez
   - Mostrar mensajes descriptivos
   - No esperar al envío del formulario

3. **Validar tanto formato como contenido**:
   - Formato del email (regex)
   - Campo no vacío
   - Longitud adecuada

## Solución de Problemas

### Error de importación
```python
# Asegúrate de que el archivo está en el mismo directorio
from validaciones_utils import ValidacionesUtils
```

### Validación no funciona
- Verifica que el email no esté vacío
- Asegúrate de que el parent window esté correcto
- Comprueba que el bind esté configurado correctamente

### Mensajes de error no aparecen
- Verifica que el parent window sea válido
- Asegúrate de que no haya otro mensbox bloqueando

## Contribuciones

Este sistema está diseñado para ser:
- **Modular**: Cada función tiene una responsabilidad específica
- **Reutilizable**: Puedes usar las funciones en cualquier proyecto
- **Extensible**: Fácil de agregar nuevos tipos de validación
- **Mantenible**: Código limpio y bien documentado

## Licencia

Este código es de dominio público. Puedes usarlo, modificarlo y distribuirlo libremente.